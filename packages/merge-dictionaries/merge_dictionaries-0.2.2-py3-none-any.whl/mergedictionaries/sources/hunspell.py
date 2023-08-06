#   -------------------------------------------------------------
#   Merge dictionaries :: Sources :: Hunspell
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Find Hunspell personal dictionaries
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os


def get_hunspell_environment_variables():
    return [
        "DICTIONARY",
        "LC_ALL",
        "LC_MESSAGES",
        "LANG",
    ]


def resolve_personal_dictionary_paths_from_environment():
    names = {"default"}

    for variable in get_hunspell_environment_variables():
        if variable in os.environ:
            names.add(os.environ[variable])

    dictionary_paths = [
        os.path.join(os.environ["HOME"], f".hunspell_{name}") for name in names
    ]

    if "WORDLIST" in os.environ:
        dictionary_paths.append(os.environ["WORDLIST"])

    return dictionary_paths


def find_personal_dictionaries():
    return [
        file
        for file in resolve_personal_dictionary_paths_from_environment()
        if os.path.exists(file)
    ]


def extract_words(dictionary_path):
    return [word.strip() for word in open(dictionary_path)]


def extract_words_from_all_dictionaries():
    return {
        word
        for dictionary_path in find_personal_dictionaries()
        for word in extract_words(dictionary_path)
    }
