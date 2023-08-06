from typing import List, Dict, Iterable, Union, Set, Callable
import logging
from time import perf_counter
import pandas
from sklearn.metrics import precision_score, recall_score, f1_score
from itertools import chain
from pathlib import Path

from isla import language
from isla.language import ISLaUnparser
from isla.solver import ISLaSolver
from isla.language import DerivationTree
from fuzzingbook.Parser import EarleyParser
from fuzzingbook.Grammars import Grammar, is_valid_grammar

from avicenna.helpers import (
    Timetable,
    register_termination,
    CustomTimeout,
    time,
    run_islearn,
    constraint_eval,
)
from avicenna.fuzzer.generator import Generator
from avicenna.learner import InputElementLearner


class Avicenna(Timetable):
    def __init__(
        self,
        grammar: Grammar,
        evaluation_function: Callable[[DerivationTree], bool],
        initial_inputs: List[str],
        working_dir: Path = Path("/tmp").resolve(),
        activated_patterns: List[str] = None,
        max_iterations: int = 10,
        max_excluded_features: int = 3,
        pattern_file: Path = None,
    ):

        super().__init__(working_dir)
        self._start_time = None
        self._grammar: Grammar = grammar
        self._activated_patterns = activated_patterns
        self._evaluation_function = evaluation_function
        self._max_iterations: int = max_iterations
        self._max_excluded_features: int = max_excluded_features - 1
        self._iteration = 0
        self._timeout: int = 3600  # timeout in seconds
        self._new_inputs: Union[List[DerivationTree], None] = None
        self._initial_inputs = initial_inputs
        self._data = None
        self._all_data = None
        self._learned_invariants: Dict[str, List[float]] = {}
        self._best_candidates: Dict[str, List[float]] = {}
        if pattern_file is not None:
            logging.info(f"Loading pattern file from location: {str(pattern_file)}")
            self._pattern_file = pattern_file
        self._feature_table = None
        self._infeasible_constraints: Set = set()

        try:
            assert is_valid_grammar(self._grammar)
        except TypeError:
            logging.info("Invalid grammar provided. Exiting.")
            exit(-1)

    def _initialize(self):
        # Initializing Data Frame
        self._all_data = pandas.DataFrame(columns=["input", "oracle"])

        derivation_trees = [
            language.DerivationTree.from_parse_tree(
                next(EarleyParser(self._grammar).parse(inp))
            )
            for inp in self._initial_inputs
        ]

        exec_oracle = self._get_execution_outcome(derivation_trees)

        positive_samples = []
        negative_samples = []
        for i, inp in enumerate(derivation_trees):
            if exec_oracle[i] is True:
                positive_samples.append(inp)
            else:
                negative_samples.append(inp)

        logging.debug(f"Positive samples: {positive_samples}")
        assert (
            len(positive_samples) != 0
        ), "No failure-inducing input hase been given. Exiting"
        logging.info(
            f"{len(positive_samples)} failure inducing and {len(negative_samples)} benign inputs given."
        )

        if exec_oracle.count(True) < 50 or exec_oracle.count(False) < 50:
            logging.info("Generating additional inputs.")
            generator = Generator(50, 50, self._grammar, self._evaluation_function)
            pos_inputs, neg_inputs = generator.generate_mutation(positive_samples)
            positive_samples += pos_inputs
            negative_samples += neg_inputs

        logging.info(
            f"Generated additional {len(positive_samples)} failure inducing and "
            f"{len(negative_samples)} "
            "benign inputs given."
        )

        self._new_inputs = positive_samples + negative_samples

    def generate(self):
        logging.info("Starting AVICENNA.")
        register_termination(self._timeout)
        try:
            self._start_time = perf_counter()
            self._initialize()
            while True:
                logging.info("Starting Iteration " + str(self._iteration))
                self._loop()
                self._iteration = self._iteration + 1
                yield self._best_candidates
        except CustomTimeout:
            logging.exception("Terminate due to timeout")
        return self._finalize()

    @time
    def execute(self):
        logging.info("Starting AVICENNA.")
        register_termination(self._timeout)
        try:
            self._start_time = perf_counter()
            self._initialize()
            while self._do_more_iterations():
                logging.info("Starting Iteration " + str(self._iteration))
                self._loop()
                self._iteration = self._iteration + 1
        except CustomTimeout:
            logging.exception("Terminate due to timeout")
        return self._finalize()

    def _do_more_iterations(self):
        # stop if there are no new samples
        # if 0 == self.__last_new_samples:
        #    return False
        # stop after 10 iterations
        if -1 == self._max_iterations:
            return True
        if self._iteration >= self._max_iterations:
            logging.info("Terminate due to maximal iterations reached")
            return False
        return True

    def _loop(self):
        # Execute inputs samples to obtain the behavior outcome
        execution_outcome = self._get_execution_outcome(input_samples=self._new_inputs)

        # Combining with the already existing data
        self._add_new_data(self._new_inputs, execution_outcome)

        # Extract the most important non-terminals that are responsible for the program behavior
        excluded_non_terminals = self._get_exclusion_set(
            input_samples=self._all_data["input"].tolist(),
            exec_oracle=execution_outcome,
        )

        # Run islearn to learn new constraints
        new_constraints = self._learn_new_constraints(excluded_non_terminals)

        # Evaluate Invariants
        current_best_invariants = self._evaluate_constraints(new_constraints)

        # Compare to previous invariants to get the best global invariant
        self._best_candidates = self._get_best_global_invariant(current_best_invariants)

        # best_invariants = self._get_best_invariants(new_constraints)
        negated_constraints = self._negating_constraints(list(self._best_candidates))

        # Generate new input samples form the learned constraints
        self._new_inputs = self._generate_new_inputs(
            negated_constraints + list(self._best_candidates)
        )

    @time
    def _learn_new_constraints(self, excluded_non_terminals: Set[str]) -> List[str]:
        positive_inputs = self._all_data.loc[
            self._all_data["oracle"].astype(str) == "True"
        ]["input"].tolist()
        negative_inputs = self._all_data.loc[
            self._all_data["oracle"].astype(str) == "False"
        ]["input"].tolist()

        assert len(positive_inputs) != 0 and len(negative_inputs) != 0

        new_constraints = list()
        try:
            new_constraints = run_islearn(
                grammar=self._grammar,
                prop=self._evaluation_function,
                positive_trees=positive_inputs,
                negative_trees=negative_inputs,
                activated_patterns=self._activated_patterns,
                excluded_features=excluded_non_terminals,
                pattern_file=self._pattern_file,
            )
        except ValueError as e:
            logging.info(e)
            logging.info(f"Could not learn any constraints")

        if len(new_constraints) == 0:
            logging.info(f"Could not learn any constraints")
            new_constraints = self._best_candidates

        # assert len(new_constraints) != 0, "No new candidate constraints were learned. Exiting."
        if len(new_constraints) == 0:
            new_constraints = self._learn_new_constraints(set())
        return new_constraints

    @time
    def _get_exclusion_set(
        self, input_samples: List[DerivationTree], exec_oracle: Iterable[bool]
    ) -> Set[str]:
        logging.info("Determining the most important non-terminals.")

        learner = InputElementLearner(
            grammar=self._grammar,
            prop=self._evaluation_function,
            input_samples=input_samples,
            generate_more_inputs=False,
        )
        learner.learn()
        relevant, irrelevant = learner.get_exclusion_sets()

        logging.info(f"Determined: {relevant} to be the most relevant features.")
        logging.info(f"Excluding: {irrelevant} from candidate consideration.")

        return irrelevant

    def _negating_constraints(self, constraints: List):
        negated_constraints = []
        for constraint in constraints:
            negated_constraints.append("not(" + constraint + ")")

        return negated_constraints

    @time
    def _generate_new_inputs(self, best_constraints: List[str]):
        logging.info("Generating new inputs to refine constraints.")

        # Exclude all infeasible constraints:
        num_constraints = len(best_constraints)
        for constraint in best_constraints:
            if constraint in self._infeasible_constraints:
                best_constraints.remove(constraint)

        logging.info(
            f"Using {len(best_constraints)} (of {num_constraints}) constraints to generate new inputs"
        )

        inputs: List[DerivationTree] = []
        for constraint in best_constraints:
            try:
                solver = ISLaSolver(
                    grammar=self._grammar,
                    formula=constraint,
                    max_number_free_instantiations=20,
                    max_number_smt_instantiations=20,
                    enable_optimized_z3_queries=False,
                )

                new_inputs: List[DerivationTree] = []

                for _ in range(20):
                    new_inputs.append(solver.solve())

                if len(new_inputs) == 0:
                    # Solver was not able to generate inputs:
                    self._add_infeasible_constraints(constraint)

                inputs = inputs + new_inputs
            except Exception as e:
                logging.info("Error: " + str(e))
                self._add_infeasible_constraints(constraint)

        assert len(inputs) != 0, "No new inputs were generated. Exiting."
        logging.info(f"{len(inputs)} new inputs have been generated.")
        return inputs

    def _add_infeasible_constraints(self, constraint):
        self._infeasible_constraints.add(constraint)
        logging.info("Removing infeasible constraint")
        logging.debug(f"Infeasible constraint: {constraint}")

    def _get_best_invariants(self, new_constraints):
        # constraints = list(map(lambda p: f"" + ISLaUnparser(p[0]).unparse(), new_constraints.items()))

        logging.info(f"In total, {len(new_constraints)} constraints were learned.\n")
        logging.info(
            "\n".join(
                map(
                    lambda p: f"{p[1]}: " + ISLaUnparser(p[0]).unparse() + "\n",
                    new_constraints.items(),
                )
            )
        )

        best_invariant, (specificity, sensitivity) = next(iter(new_constraints.items()))
        logging.info(
            f"Best invariant (*estimated* specificity {specificity:.2f}, sensitivity: {sensitivity:.2f}):"
        )
        logging.info(ISLaUnparser(best_invariant).unparse())

        self._learned_invariants[best_invariant] = [specificity, sensitivity]

        return best_invariant

    def _finalize(self):
        logging.info("Avicenna finished")
        logging.info("The best learned failure invariant(s):")

        best = dict()
        best_f1 = 0
        for constraint in self._best_candidates.items():
            p0, p1 = constraint
            if p1[2] >= best_f1:
                best_f1 = p1[2]
                best[p0] = p1

        logging.info("\n".join(map(lambda p: f"{p[1]}: " + p[0] + "\n", best.items())))

        return best

    def _add_new_data(self, inputs: List[DerivationTree], exec_oracle: List[bool]):
        df = pandas.DataFrame(
            list(zip(inputs, exec_oracle)), columns=["input", "oracle"]
        )

        if self._all_data is None:
            self._all_data = df.drop_duplicates()
        else:
            self._all_data = pandas.concat(
                [self._all_data, df], sort=False
            ).drop_duplicates()

    @time
    def _get_execution_outcome(self, input_samples: List[DerivationTree]) -> List[bool]:
        logging.debug("Executing input samples.")

        exec_oracle = []
        for inp in input_samples:
            exec_oracle.append(self._evaluation_function(inp))

        return exec_oracle

    @time
    def _evaluate_constraints(self, new_constraints):
        eval_data: Dict[str, List[float]] = {}

        # Let's parse all the generated inputs
        x_eval = [inp for inp in self._all_data["input"]]

        combined_constraints = new_constraints
        if self._best_candidates is not None:
            combined_constraints = chain(self._best_candidates, new_constraints)

        for constraint in combined_constraints:
            constraint_data = constraint_eval(
                x_eval,
                constraint,
                prop=self._evaluation_function,
                grammar=self._grammar,
            )

            precision = precision_score(
                constraint_data["oracle"].astype(bool),  # TODO Reformat
                constraint_data["predicted"].astype(bool),
                pos_label=True,
                average="binary",
            )
            precision = round(precision * 100, 3)

            recall = recall_score(
                constraint_data["oracle"].astype(bool),
                constraint_data["predicted"].astype(bool),
                pos_label=True,
                average="binary",
            )
            recall = round(recall * 100, 3)

            f1 = f1_score(
                constraint_data["oracle"].astype(bool),
                constraint_data["predicted"].astype(bool),
                pos_label=True,
                average="binary",
            )

            logging.debug(f"Results for f{constraint}")
            logging.debug(f"The constraint achieved a precision of {precision} %")
            logging.debug(f"The constraint achieved a recall of {recall} %")
            logging.debug(f"The constraint achieved a f1-score of {round(f1, 3)}")

            eval_data[constraint] = [precision, recall, f1]

        sorted_data = sorted(
            eval_data.items(), key=lambda item: item[1][2], reverse=True
        )

        sorted_comp = {}
        for s in sorted_data:
            sorted_comp[s[0]] = s[1]

        best_five = list(sorted_comp.keys())[0:4]  # TODO Abstract
        # for i in best_five:
        #    print(i)

        # self._best_invariant = list(sorted_comp.keys())[0]  # TODO Select the global best Invariant
        return sorted_comp

    def _get_best_global_invariant(self, current_best_invariants):

        if self._iteration != 0:
            combined_data = self._best_candidates | current_best_invariants
        else:
            combined_data = current_best_invariants

        sorted_data = sorted(
            combined_data.items(), key=lambda item: item[1][2], reverse=True
        )
        best_global_constraints = {}
        for i in list(sorted_data)[0:4]:
            best_global_constraints[i[0]] = combined_data[i[0]]

        logging.info(f"Top five learned constraints:\n")
        logging.info(
            "\n".join(
                map(
                    lambda p: f"{p[1]}: " + p[0] + "\n", best_global_constraints.items()
                )
            )
        )

        return best_global_constraints

    def iteration_identifier_map(self):
        return {"iteration": self._iteration}
