#!/usr/bin/python3
import xml.etree.ElementTree as ET
def serialize_to_xml(dictionary, filename):
    for key,value in dictionary.items():
        elem=ET.Element("data")
        if isinstance(value,dict):
            child=serialize_to_xml(key,value)
            elem.append(child)
        else:
            child=ET.SubElement(elem,key)
            child.text=str(value)
    return elem

def deserialize_from_xml(filename):
    root=ET.parse(filename)
    return root