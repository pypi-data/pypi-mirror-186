from functools import lru_cache
from typing import List, Set

import numpy
import pandas
from fuzzingbook.GrammarFuzzer import is_nonterminal, Grammar
from isla.language import DerivationTree

from avicenna.features import (
    Feature,
    FeatureWrapper,
    STANDARD_FEATURES,
    ExistenceFeature,
)


class Collector:
    def __init__(self, grammar, features=None):
        if features is None:
            features = STANDARD_FEATURES
        self._grammar: Grammar = grammar
        self._features: Set[FeatureWrapper] = features
        self.all_features = self.get_all_features()

    def get_all_features(self):
        assert len(self._features) != 0

        features = []
        for feature_class in self._features:
            features = features + feature_class.extract_from_grammar(
                grammar=self._grammar
            )
        assert len(features) != 0, "Could not extract any features."
        return features

    def collect_features(self, input_list: List[DerivationTree]):
        data = []
        for sample in input_list:
            assert isinstance(
                sample, DerivationTree
            ), "Inputs is not a derivation tree."
            parsed_features = {"input": sample.to_string()}
            # initiate dictionary
            for feature in self.all_features:
                # initialization
                parsed_features[feature.name] = feature.initialization_value()

            self.feature_collection(sample, parsed_features)
            data.append(parsed_features)

        return pandas.DataFrame.from_records(data)

    def feature_collection(self, tree: DerivationTree, feature_table):
        (node, children) = tree

        # Get features that correspond to this node
        # Get all one-dimensional features, e.g., Existence Feature of a single non-terminal,
        # the length or the numerical representation of a non-terminal.
        corresponding_features_1d = self.get_corresponding_feature(node, node)

        for corresponding_feature in corresponding_features_1d:
            assert feature_table[corresponding_feature.name] is not None, (
                f"Feature {corresponding_feature.name} is " f"not in the feature table"
            )
            value = corresponding_feature.evaluate(tree, feature_table)
            if value is not None:
                feature_table[corresponding_feature.name] = value

        # Get features that correspond to this node
        # Get all two-dimensional features, e.g., the Existence of a Derivation Sequences A-> BD
        expansion = "".join([child[0] for child in children])
        corresponding_features_2d = self.get_corresponding_feature(node, expansion)

        for corresponding_feature in corresponding_features_2d:
            assert feature_table[corresponding_feature.name] is not None, (
                f"Feature {corresponding_feature.name} is " f"not in the feature table"
            )
            value = corresponding_feature.evaluate(tree, feature_table)
            if value is not None:
                feature_table[corresponding_feature.name] = value

        for child in children:
            if is_nonterminal(child[0]):
                self.feature_collection(child, feature_table)

    @lru_cache
    def get_corresponding_feature(
        self, feature_rule: str, feature_key: str
    ) -> List[Feature]:
        feature_list = []
        for feature in self.all_features:
            if feature.rule == feature_rule and feature.key == feature_key:
                feature_list.append(feature)

        # assert len(feature_list) != 0
        return feature_list


def get_all_features_n(features_set: Set[FeatureWrapper], grammar: Grammar):
    assert len(features_set) != 0, "No Feature Classes were given."

    features = []
    for feature_class in features_set:
        features = features + feature_class.extract_from_grammar(grammar=grammar)
    assert len(features) != 0, "Could not extract any features."
    return features
