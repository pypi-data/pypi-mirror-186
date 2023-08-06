#!/usr/bin/env python3

import argparse
import os
import os.path
import json
import re
import subprocess

__version__ = '1.3.1'

# wdl parser downloaded from here:
# https://raw.githubusercontent.com/openwdl/wdl/main/versions/draft-2/parsers/python/wdl_parser.py
# wget https://raw.githubusercontent.com/openwdl/wdl/main/versions/draft-2/parsers/python/wdl_parser.py

from iseqmetacreator import wdl_parser

CONFIG = {}


def load_json(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def get_blame_data(path: str, show_email="") -> list:
    cmd_names = f'git blame -c {show_email} {path}'
    result = subprocess.check_output(cmd_names, shell=True, encoding='utf-8').split("\n")
    names = []
    for line in result:
        line_ = line.split("\t")
        if len(line_) > 1:
            name = line.split("\t")[1].replace("(", "").strip()
            names.append(name)
    
    return names


def create_author_dict(emails: list, names: list) -> dict:
    zipped = zip(emails, names)
    result = {}
    for items in zipped:
        if items[0] not in result and items[1] not in result.values():
            result[items[0]] = items[1]
    return result


def organize_authors(authors: dict) -> str:
    result = []
    for email, name in authors.items():
        result.append(str(name) + " (e-mail: " + str(email) + ")")
    return ", ".join(result)


def get_authors(path: str) -> str:
    try:
        names = get_blame_data(path)
        emails = get_blame_data(path, "--show-email")
        return organize_authors(create_author_dict(emails, names))
    except:
        return {}

def load_config(templates_path=None):
    if templates_path is None:
        base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
        templates_path = os.path.join(base_dir, "resources/fields")
    
    inputs = load_json(f"{templates_path}/inputs-fields.json")
    CONFIG["inputs"] = inputs["general_fields"]
    CONFIG["inputs_default"] = inputs["default_explanations"]
    CONFIG["excluded_input_fields"] = inputs["excluded_input_fields"]
    
    outputs = load_json(f"{templates_path}/outputs-fields.json")
    CONFIG["outputs"] = outputs["general_fields"]
    CONFIG["outputs_default"] = outputs["default_explanations"]
    
    CONFIG["workflows"] = load_json(f"{templates_path}/workflows-fields.json")["general_fields"]


load_config()


def read_wdl(file: str) -> dict:
    with open(file, 'r') as wdl:
        return wdl_to_json(wdl_parser.parse(wdl.read()))


def wdl_to_json(val):
    if type(val) == wdl_parser.ParseTree:
        return wdl_to_json(val.ast())
    
    if type(val) == wdl_parser.Ast:
        result = {}
        
        for key in val.attributes:
            result[key] = wdl_to_json(val.attributes[key])
        if "map" in result:
            return result["map"]
        result["kind"] = val.name
        return result
    
    if type(val) == wdl_parser.AstList:
        result = []
        for e in val:
            result.append(wdl_to_json(e))
        
        if len(result) > 0 and "key" in result[0] and "value" in result[0]:
            final_result = {}
            for e in result:
                final_result[e["key"]] = wdl_to_json(e["value"])
            return final_result
        
        return result
    
    if type(val) == wdl_parser.Terminal:
        return wdl_to_json(val.__dict__['source_string'])
    
    if isinstance(val, str):
        if len(val) > 0 and val[0] == "{":
            return wdl_to_json(json.loads(val))
        if val == "true":
            return True
        if val == "false":
            return False
        if re.match(r'^-?\d+\.\d+$', val):
            return float(val)
        if val.isdigit():
            return int(val)
        return val
    
    if val is None:
        return None
    
    if isinstance(val, dict):
        result = {}
        for key, value in val.items():
            result[key] = wdl_to_json(value)
        return result
    
    return val


def obligatory_fields(item: dict) -> dict:
    if isinstance(item, dict):
        result = {"name": item['name'],
                  "description": "",
                  "type": define_type(item)}
    else:
        raise Exception(f"Item is not a dictionary, item is {type(item)}")
    return result


def define_extensions(input_file: dict):
    if "defined" not in input_file["name"] and "File" in input_file["type"]:
        
        simple_extensions = ["json", "bai", "bam", "bed", "tsv", "txt", "csv", "gtc", "bpm", "egt", "interval_list",
                             "gtf"]
        for item in simple_extensions:
            if item in input_file["name"]:
                return ["." + item]
        
        if "bed" in input_file["name"]:
            return [".bed", ".bed.gz"]
        if "fastq" in input_file["name"]:
            return [".fq.gz", ".fastq.gz"]
        if "gvcf_tbi" in input_file["name"]:
            return [".gvcf.gz.tbi", ".g.vcf.gz.tbi"]
        if "gvcf" in input_file["name"]:
            return [".gvcf.gz", ".g.vcf.gz"]
        if "tbi" in input_file["name"]:
            return [".vcf.gz.tbi"]
        if "vcf" in input_file["name"]:
            return [".vcf.gz"]
        if "tar_gz" in input_file["name"]:
            return [".tar.gz"]
        if "counts" in input_file["name"]:
            return [".tsv", ".txt"]
        if "sample_mapping" in input_file["name"]:
            return [".tsv", ".txt"]        
        raise Exception("Cannot generate extensions for File: " + str(
            input_file) + ". Please add additional value in function define_extensions. ")
    
    return None


def remove_inputs(inputs: list) -> list:
    result = []
    for i in inputs:
        if 'type' in i:
            not_excluded = True
            for excluded_name in CONFIG["excluded_input_fields"]:
                if excluded_name in i["name"]:
                    not_excluded = False
                    break
            if "expression" in i and "select_first" in str(i["expression"]):
                not_excluded = False
            
            if not_excluded:
                result.append(i)
    return result


def make_inputs(inputs: list) -> dict:
    inputs = remove_inputs(inputs)
    result = {}
    index = 1
    
    for item in inputs:
        processed = obligatory_fields(item)
        
        processed["index"] = index
        extension = define_extensions(item)
        if extension is not None:
            processed["extensions"] = extension
        use_fields_json(processed, "inputs")
        result[f"input_{item['name']}"] = processed
        index = index + 1
    return result


def make_outputs(outputs: dict) -> dict:
    result = {}
    for output in outputs:
        processed_output = obligatory_fields(output)
        use_fields_json(processed_output, "outputs")
        
        result[f"output_{output['name']}"] = processed_output
    return result


def get_wdl_name(wdl_path: str) -> str:
    return os.path.basename(wdl_path).replace(".wdl", "")


def create_explanation(field: dict, wdl_path=None) -> str:
    if field['field_explanation'] == "hard":
        return field['field_example']
    if field["field_name"] == "author":
        return get_authors(wdl_path)
    if field["field_name"] == "name":
        return get_wdl_name(wdl_path)
    
    example = str(field["field_example"])
    data_type = type(field["field_example"]).__name__
    
    if field["obligatory"]:
        obligatory = "OBLIGATORY field"
    else:
        obligatory = "OPTIONAL field. Remove it if it is not used"
    explanation = f"{obligatory}. {field['field_explanation']}. Example: '{example}'. Type: {data_type}."
    return explanation


def general_fields(wdl_path) -> dict:
    gen_fields = CONFIG["workflows"]
    result = {}
    for item in gen_fields:
        result[item["field_name"]] = create_explanation(item, wdl_path)
    return result


def merge_jsons(outputs: dict, inputs: dict, gen_fields: dict) -> dict:
    gen_fields.update(inputs)
    gen_fields.update(outputs)
    return gen_fields


def define_type(inputs):
    # input String, input File, input Int, input Float, input Boolean
    if isinstance(inputs["type"], str) or isinstance(inputs["type"], int) or isinstance(inputs["type"], float):
        return inputs["type"]
    if 'innerType' in inputs["type"]:
        # input Array[File]
        # input Arrat[String]
        # output Array[File]
        # outpuy Array[String]
        if 'subtype' in inputs["type"]['innerType'] and 'name' in inputs["type"]['innerType']:
            typ = inputs["type"]['innerType']['name']
            subtype = inputs["type"]['innerType']['subtype']
            return f"{typ}[{str(subtype[0])}]"
        # output File
        if 'subtype' not in inputs["type"]['innerType'] and 'name' not in inputs["type"]['innerType']:
            return inputs["type"]['innerType']
    # output Array[File]
    if 'innerType' not in inputs["type"] and 'name' in inputs["type"] and 'subtype' in inputs["type"]:
        typ = inputs["type"]['name']
        subtype = inputs["type"]['subtype']
        return f"{typ}[{str(subtype[0])}]"
    raise Exception("Cannot extract type: " + str(inputs))


def extract_inputs_and_outputs_from_workflow(wdl_json):
    inputs = []
    outputs = []
    
    for item in wdl_json['body'][0]['body']:
        if 'kind' in item.keys():
            if item['kind'] == 'WorkflowOutputs':
                outputs = item['outputs']
            else:
                inputs.append(item)
    
    return inputs, outputs


def extract_inputs_and_outputs_from_last_task(wdl_json):
    task = wdl_json['body'][-1]
    
    inputs = []
    for item in task['declarations']:
        inputs.append(item)
    
    assert task['sections'][-1]['kind'] == 'Outputs'
    
    outputs = []
    for item in task['sections'][-1]['attributes']:
        outputs.append(item)
    
    return inputs, outputs


def has_single_workflow(wdl_json):
    return 'body' in wdl_json and len(wdl_json['body']) == 1 and wdl_json['body'][0]['kind'] == 'Workflow'


def has_task_at_end(wdl_json):
    return 'body' in wdl_json and len(wdl_json['body']) > 0 and wdl_json['body'][-1]['kind'] == 'Task'


def make_fields(wdl_json, path):
    if has_single_workflow(wdl_json):
        inputs, outputs = extract_inputs_and_outputs_from_workflow(wdl_json)
    elif has_task_at_end(wdl_json):
        inputs, outputs = extract_inputs_and_outputs_from_last_task(wdl_json)
    else:
        assert False
    return merge_jsons(make_outputs(outputs), make_inputs(inputs), general_fields(path))


def load_general_fields(input_or_output):
    return CONFIG[input_or_output]


def use_fields_json(item: dict, input_or_output: str) -> dict:
    fields = load_general_fields(input_or_output)
    for field in fields:
        
        if item["type"] in field["list_of_types_with_this_field"]:
            if field["field_explanation"] != "auto-complete":
                item[field["field_name"]] = create_explanation(field)
            
            default = f"{input_or_output}_default"
            if item["name"] in CONFIG[default].keys():
                item["description"] = CONFIG[default][item["name"]]
            if "." in field["field_name"]:
                before_dot = field["field_name"].split(".")[0]
                after_dot = field["field_name"].split(".")[1]
                if before_dot not in item:
                    item[before_dot] = {
                        after_dot: item[field["field_name"]]
                    }
                else:
                    item[before_dot][after_dot] = item[field["field_name"]]
                del item[field["field_name"]]
    return item


def main():
    parser = argparse.ArgumentParser(
        description='Script makes json with metadata in the same directory as wdl is - meta.json, based on wdl code. ')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(__version__))
    # INPUTS
    parser.add_argument('-p', '--path', help="Path to wdl.")
    parser.add_argument('-t', '--templates_path',
                        help="Path to directory, containing configuration jsons (workflow, inputs, outputs). Default: "
                             "src/main/wdl/tasks/meta-test")
    arguments = vars(parser.parse_args())

    wdl_json = read_wdl(arguments['path'])
    result = make_fields(wdl_json, arguments['path'])
    
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
