#!/usr/bin/env python3
import argparse
import json
import pathlib
import urllib.request
from typing import Dict

script_path = pathlib.Path(__file__).parent.absolute()

__version__ = "0.0.1"
__author__ = "https://gitlab.com/olaf.tomaszewski"


def args_parser_init():
    """Get user inputs"""
    parser = argparse.ArgumentParser(description="""Converting tools old meta.json to new meta.json
    More info here:
                    https://intelliseq.atlassian.net/wiki/spaces/DEV/pages/238518273/Zmiany+w+inputach""",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-m', '--input-meta-json', type=str, required=True,
                        help='An old meta.json file to convert')
    parser.add_argument('-j', '--input-dict-json', type=str, required=True,
                        help='Json file containing translated new keys and removed old keys in meta.json conversion')
    parser.add_argument('-o', '--output-meta-json', type=str, required=True,
                        help='Output converted meta.json file')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(__version__))

    args = parser.parse_args()
    return args


def load_json_and_print_correct_formatting(json_to_load, input_json) -> Dict:
    output_dict = json.load(json_to_load)
    print(f"{input_json} is correctly formatted .json file")
    return output_dict


def check_json_error(input_json: str) -> Dict:
    """Load json to program. If there's an error print details with traceback"""
    try:
        if input_json.startswith("https://"):
            with urllib.request.urlopen(input_json) as json_url:
                output_dict = load_json_and_print_correct_formatting(json_url, input_json)
        else:
            with open(input_json) as json_file:
                output_dict = load_json_and_print_correct_formatting(json_file, input_json)
        return output_dict
    except ValueError as ex:
        print(f"{ex.with_traceback(ex.__traceback__)} in {input_json} file!")
        exit()


def get_inputs_to_modify(meta_dict: Dict) -> Dict:
    """Get all dict-type inputs instead of variants"""
    return dict(filter(lambda x: isinstance(x[1], dict)
                                 and (x[0].startswith("input")
                                      or x[0].startswith("variant") and "input" in x[0]), meta_dict.items()))


def get_outputs_to_modify(meta_dict: Dict) -> Dict:
    """Get all outputs parameters"""
    return dict(filter(lambda x: isinstance(x[1], dict)
                                 and x[0].startswith("output"), meta_dict.items()))


def remove_old_keys_from_entry(element_to_change, to_remove_dict, remove_from):
    for key_to_remove in to_remove_dict[remove_from]:
        if '.' in key_to_remove:
            sub_dict, sub_value = key_to_remove.split('.')
            element_to_change.get(sub_dict, {}).pop(sub_value, None)
        else:
            element_to_change.pop(key_to_remove, None)
    return element_to_change


def rename_old_keys_from_entry(element_to_change, to_rename_dict, rename_from):
    current_rename_dict = to_rename_dict[rename_from]
    for key_to_rename in current_rename_dict:
        if '.' in key_to_rename:
            sub_dict, sub_value = key_to_rename.split('.')
            value_to_rename = element_to_change.get(sub_dict, {}).pop(sub_value, None)
        else:
            value_to_rename = element_to_change.pop(key_to_rename, None)

        if value_to_rename:
            if '.' in current_rename_dict[key_to_rename]:
                sub_dict, sub_value = current_rename_dict[key_to_rename].split('.')
                element_to_change[sub_dict] = element_to_change.get(sub_dict, {})
                element_to_change[sub_dict][sub_value] = value_to_rename
            else:
                element_to_change[current_rename_dict[key_to_rename]] = value_to_rename

    return element_to_change


def rename_old_keys(to_change_dict, to_rename_dict, rename_from):
    for entry in to_change_dict.keys():
        element_to_change = to_change_dict[entry]
        rename_old_keys_from_entry(element_to_change, to_rename_dict, rename_from)
    return to_change_dict


def remove_old_keys(to_change_dict, to_remove_dict, remove_from):
    for entry in to_change_dict.keys():
        element_to_change = to_change_dict[entry]
        remove_old_keys_from_entry(element_to_change, to_remove_dict, remove_from)
    return to_change_dict


def save_to_json(meta_dict, output_meta_json):
    with open(output_meta_json, 'w') as json_file:
        json.dump(meta_dict, json_file)


def get_workflows_to_modify(meta_dict):
    return dict(filter(lambda x: "input" not in x[0]
                                 and "output" not in x[0]
                                 and "groups" not in x[0], meta_dict.items()))


def fix_workflows_reference(old_workflows_keys, workflows_dict, meta_dict):
    for key in old_workflows_keys:
        meta_dict.pop(key, None)

    return {**workflows_dict, **meta_dict}


def get_groups_to_modify(meta_dict):
    return dict(filter(lambda x: isinstance(x[1], dict)
                                 and (x[0].startswith("groups")
                                      or x[0].startswith("variant") and "groups" in x[0]), meta_dict.items()))


def update_workflows(meta_dict, workflows_dict, to_rename_dict, to_remove_dict):
    workflows_variants = [key for key in workflows_dict.keys() if 'variant' in key]

    for key in list(to_rename_dict['workflows'].keys()):
        for variant in workflows_variants:
            if f"_{key}" in variant:
                prefix = variant.split('_')[0]
                to_rename_dict['workflows'][variant] = f"{prefix}_{to_rename_dict['workflows'][key]}"

    for key in to_remove_dict['workflows']:
        for variant in workflows_variants:
            if f"_{key}" in variant:
                to_remove_dict['workflows'].append(variant)

    old_workflows_keys = list(workflows_dict.keys())
    workflows_dict = rename_old_keys_from_entry(workflows_dict, to_rename_dict, rename_from='workflows')
    workflows_dict = remove_old_keys_from_entry(workflows_dict, to_remove_dict, remove_from='workflows')

    meta_dict = fix_workflows_reference(old_workflows_keys, workflows_dict, meta_dict)

    return meta_dict


def main():
    args = args_parser_init()
    meta_dict = check_json_error(args.input_meta_json)
    translate_dict = check_json_error(args.input_dict_json)

    workflows_dict = get_workflows_to_modify(meta_dict)
    inputs_dict = get_inputs_to_modify(meta_dict)
    outputs_dict = get_outputs_to_modify(meta_dict)
    groups_dict = get_groups_to_modify(meta_dict)

    to_rename_dict = translate_dict['rename']
    to_remove_dict = translate_dict['remove']

    meta_dict = update_workflows(meta_dict, workflows_dict, to_rename_dict, to_remove_dict)

    inputs_dict = rename_old_keys(inputs_dict, to_rename_dict, rename_from='inputs')
    inputs_dict = remove_old_keys(inputs_dict, to_remove_dict, remove_from='inputs')

    outputs_dict = rename_old_keys(outputs_dict, to_rename_dict, rename_from='outputs')
    outputs_dict = remove_old_keys(outputs_dict, to_remove_dict, remove_from='outputs')

    for group in groups_dict.keys():
        group_type = groups_dict[group]
        group_type = rename_old_keys(group_type, to_rename_dict, rename_from='groups')
        group_type = remove_old_keys(group_type, to_remove_dict, remove_from='groups')

    save_to_json(meta_dict, args.output_meta_json)


if __name__ == "__main__":
    main()
