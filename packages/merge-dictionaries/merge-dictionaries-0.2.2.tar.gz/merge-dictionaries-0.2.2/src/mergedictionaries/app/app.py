#!/usr/bin/env python3

#   -------------------------------------------------------------
#   Merge dictionaries
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Merge dictionaries from various sources,
#                   mainly IDEs, and allow to propagate them.
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import argparse
import os
import sys

import yaml

from mergedictionaries import write, output, sources


#   -------------------------------------------------------------
#   Extract words
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_dictionary_formatters():
    return {
        "JetBrains": output.jetbrains.dump,
    }


#   -------------------------------------------------------------
#   Configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_configuration_path():
    return os.environ["HOME"] + "/.config/merge-dictionaries.conf"


def parse_configuration():
    try:
        with open(get_configuration_path()) as fd:
            return yaml.safe_load(fd)
    except OSError:
        return {}


#   -------------------------------------------------------------
#   Application entry point
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def parse_arguments():
    parser = argparse.ArgumentParser(description="Merge dictionaries.")

    parser.add_argument(
        "--extract",
        action="store_const",
        dest="task",
        const="extract",
        help="Extract all words from found dictionaries",
    )
    parser.add_argument(
        "--format", action="store", help="Specifies the output format", default="text"
    )

    parser.add_argument(
        "--merge",
        action="store_const",
        dest="task",
        const="merge",
        help="Merge all found dictionaries",
    )

    return parser.parse_args()


class Application:
    def __init__(self):
        self.context = {"git": {}}

    def run(self):
        args = parse_arguments()

        if args.task is None:
            print("No task has been specified.", file=sys.stderr)
            sys.exit(1)

        self.context["config"] = parse_configuration()
        self.context["args"] = args

        if args.task == "extract":
            self.run_extract_all_words(args.format)
        elif args.task == "merge":
            self.run_merge()

    def get_dictionary_writers(self):
        return [
            lambda words: write.jetbrains.write(words),
            lambda words: write.git.write(
                words, self.context["config"].get("git", []), self.context["git"]
            ),
        ]

    def run_merge(self):
        words = self.extract_all_words()

        for method in self.get_dictionary_writers():
            method(words)

        self.on_exit()

    def get_words_sources(self):
        return [
            lambda: sources.git.extract_words_from_all_dictionaries(
                self.context["config"].get("git", []), self.context["git"]
            ),
            lambda: sources.jetbrains.extract_words_from_all_dictionaries(),
            lambda: sources.hunspell.extract_words_from_all_dictionaries(),
        ]

    def extract_all_words(self):
        return sorted(
            {word for method in self.get_words_sources() for word in method()}
        )

    def run_extract_all_words(self, words_format):
        words = self.extract_all_words()

        # Trivial case
        if words_format == "text" or words_format == "hunspell":
            if words_format == "hunspell":
                print(len(words))

            for word in words:
                print(word)

            self.on_exit()
            sys.exit(0)

        # We need a specific formatter
        formatters = get_dictionary_formatters()
        if words_format not in formatters:
            print(f"Unknown format: {words_format}", file=sys.stderr)
            self.on_exit()
            sys.exit(2)

        print(formatters[words_format](words))
        self.on_exit()
        sys.exit(0)

    def on_exit(self):
        """Events to run before exiting to cleanup resources."""
        sources.git.on_exit(self.context["git"])


def run():
    app = Application()
    app.run()
