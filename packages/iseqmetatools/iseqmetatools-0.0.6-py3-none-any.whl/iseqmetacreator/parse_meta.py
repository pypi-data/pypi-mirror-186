#!/usr/bin/env python3

import argparse
__version__ = '1.0.1'

# wdl parser downloaded from here https://raw.githubusercontent.com/openwdl/wdl/main/versions/draft-2/parsers/python/wdl_parser.py
# wget https://raw.githubusercontent.com/openwdl/wdl/main/versions/draft-2/parsers/python/wdl_parser.py
from iseqmetacreator import wdl_parser

import base64
import json
import os.path
import re

def read_wdl(file):
    with open(file, 'r') as wdl:
        return wdl.read()

def read_meta(file):
    meta = wdl_parser.parse(read_wdl(file)).ast().attributes['body'][0].attributes['body'][0].attributes['map']
    return meta

def key_value(meta):
    d = {}
    for element in meta:
        key = element.attributes['key'].__dict__['source_string']
        value = element.attributes['value'].__dict__['source_string']
        if value[0] == "{":
            value = json.loads(value)
        next
        d[key] = fix_types(value)
    return d

def fix_types(value):
    if type(value) == str:
        if len(value) > 0 and value[0] == "{":
            return fix_types(key_value(value))
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False
        if re.match(r'^-?\d+(?:\.\d+)$', value):
            return float(value)
        if value.isdigit():
            return int(value)
        return value
    if type(value) == dict:
        result = {}
        for x, y in value.items():
            result[x] = fix_types(y)
        return result
    if type(value) == list:
        return [fix_types(x) for x in value]
    if type(value) == int or type(value) == float or value == True or value == False:
        return value
    raise Exception("Unknown type: " + type(value).__name__ + "(" + str(value) + ")")

def output_path(args):
    return "/".join([(os.path.dirname(args.path)), "meta.json"])

def save_json(meta, args):
    out = output_path(args)
    with open(out, 'w') as final_json:
        json.dump(meta, final_json, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Script to parse meta in wdl and make json. ')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(__version__))
    #INPUTS
    parser.add_argument('-p', '--path', help="Path to wdl.")
    args = parser.parse_args()

    #DO
    save_json(key_value(read_meta(args.path)), args)
    # PRINTS
    print(f'Meta.json appeared here {output_path(args)}')

    #TESTS
    assert fix_types({ "foo": "bar" }) == { "foo": "bar" }
    assert fix_types("true") == True
    assert fix_types({'index': 2, 'required': 'true'}) == {'index': 2, 'required': True}


if __name__ == '__main__':
    main()
