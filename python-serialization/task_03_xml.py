#!/usr/bin/python3
"""Serialize and deserialize dictionaries to and from XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The file to save the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # ensure everything is string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The file containing XML data.
    Returns:
        dict: The reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
