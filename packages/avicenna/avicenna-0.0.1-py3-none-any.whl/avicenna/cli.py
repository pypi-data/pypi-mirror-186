import argparse
from argparse import Namespace, ArgumentParser
import sys
import logging
from io import TextIOWrapper
from typing import Dict, Iterable

from avicenna import Avicenna, __version__ as avicenna_version


def main(*args: str, stdout=sys.stdout, stderr=sys.stderr):
    parser = create_parser()

    args = parser.parse_args(args or sys.argv[1:])

    if args.version:
        print(f"Avicenna version {avicenna_version}", file=stdout)
        sys.exit(0)

    level_mapping = {
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }

    if hasattr(args, "log_level"):
        logging.basicConfig(stream=stderr, level=level_mapping[args.log_level])

    grammar_file = read_files(args.grammar)
    ensure_grammar_present(stderr, parser, args, grammar_file)

    try:
        avicenna = Avicenna(
            grammar=args.grammar,
            evaluation_function=args.prop,
            initial_inputs=args.initial_inputs,
        )
        avicenna.execute()
    except KeyboardInterrupt:
        sys.exit(0)


def create_parser():
    parser = argparse.ArgumentParser(
        prog="Avicenna",
        description="The avicenna command line interface",
    )

    parser.add_argument(
        "-v", "--version", help="Print the Avicenna version number", action="store_true"
    )

    parser.add_argument(
        "-g",
        "--grammar",
        dest="grammar",
        type=argparse.FileType("r", encoding="UTF-8"),
        help="""The grammar or input format of the program input. Grammars must declare a rule for a
                non-terminal "<start>" (the start symbol) expanding to a single other non-terminal.
                Python extension files can specify a grammar by declaring a variable `grammar` of type
                `Dict[str, List[str]]`, or (preferably) by specifying a function `grammar()` returning
                Dict objects of that type.""",
    )

    parser.add_argument(
        "-p",
        "--program",
        dest="prop",
        help="The evaluation function, that observes whether the behavior in question occurred."
        " The evaluation function returns a boolean value - True when the behavior is observed, False otherwise",
    )

    parser.add_argument(
        "-i",
        "--inputs",
        dest="initial_inputs",
        help="The initial system inputs that should be used to learn the program's behavior."
        " The initial inputs need to consist of at least one bug-triggering and at least one benign input.",
    )

    parser.add_argument(
        "-l",
        "--log-level",
        choices=["ERROR", "WARNING", "INFO", "DEBUG"],
        help="set the logging level",
    )

    return parser


def read_files(grammar_file: TextIOWrapper) -> Dict[str, str]:
    return {grammar_file.name: grammar_file.read()}


def ensure_grammar_present(
    stderr, parser: ArgumentParser, args: Namespace, files: Dict[str, str]
) -> None:
    if all(not file.endswith(".py") for file in files):
        parser.print_usage(file=stderr)
        print(
            "avicenna error: You must specify a grammar by `--grammar` "
            "with a file `.py` ending.",
            file=stderr,
        )

        exit(-1)


if __name__ == "__main__":
    exit(main())
