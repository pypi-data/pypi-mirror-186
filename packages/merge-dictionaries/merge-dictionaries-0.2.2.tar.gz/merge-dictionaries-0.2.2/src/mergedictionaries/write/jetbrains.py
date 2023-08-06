#   -------------------------------------------------------------
#   Merge dictionaries :: Publishers :: JetBrains IDEs
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Find application-level dictionaries
#                   from JetBrains IDEs
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from mergedictionaries.sources import jetbrains as jetbrains_source
from mergedictionaries.output import jetbrains as jetbrains_output


def write(words):
    contents = jetbrains_output.dump(words)

    for file_path in jetbrains_source.find_application_level_dictionaries():
        with open(file_path, "w") as fd:
            fd.write(contents)
            fd.write("\n")
