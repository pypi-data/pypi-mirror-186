#   -------------------------------------------------------------
#   Merge dictionaries :: Output :: JetBrains XML format
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Find application-level dictionaries
#                   from JetBrains IDEs
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from io import StringIO
from sys import version_info
from xml.etree import ElementTree


def get_xml_tree(words):
    root = ElementTree.Element("application")
    component = ElementTree.SubElement(
        root,
        "component",
        attrib={
            "name": "CachedDictionaryState",
        },
    )

    words_element = ElementTree.SubElement(component, "words")
    for word in words:
        word_element = ElementTree.SubElement(words_element, "w")
        word_element.text = word

    return ElementTree.ElementTree(root)


def dump(words):
    root = get_xml_tree(words)

    if version_info >= (3, 9):
        ElementTree.indent(root)

    output = StringIO()
    root.write(output, encoding="unicode")
    contents = output.getvalue()
    output.close()

    return contents
