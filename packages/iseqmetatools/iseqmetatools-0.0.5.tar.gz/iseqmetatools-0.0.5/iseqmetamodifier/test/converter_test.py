#!/usr/bin/env python3

from iseqmetamodifier import converter


def test_get_workflows_to_modify():
    test_data = {
        "author": "https://gitlab.com/olaf.tomaszewski",
        "copyright": "Copyright 2019-2021 Intelliseq",
        "name": "example name",
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)"
        },
        "input_fastqs": {
            "index": 2,
            "paired": True,
            "multiselect": True,
            "name": "Fastq files",
            "type": "Array[File]",
            "description": "Choose list of paired gzipped fastq files both left and right [.fq.gz or .fastq.gz]",
            "extension": [
                ".fq.gz",
                ".fastq.gz"
            ]
        }
    }

    expected = {
        "author": "https://gitlab.com/olaf.tomaszewski",
        "copyright": "Copyright 2019-2021 Intelliseq",
        "name": "example name"
    }
    result = converter.get_workflows_to_modify(test_data)

    assert result == expected


def test_get_groups_to_modify():
    test_data = {
        "description": "example description",
        "changes": {
            "2.0.1": "",
            "2.0.0": "",
            "1.2.0": "",
            "1.1.0": "",
            "1.0.0": ""
        },
        "groups": {
            "gene_panel": {
                "hReadableName": "Gene panel",
                "description": "Fill the inputs below to generate the gene panel",
                "rules": "Fill at least one input",
                "minInputs": 1
            },
            "target_regions": {
                "hReadableName": "Target regions",
                "description": "Fill the input below to specify regions that will be analyzed",
                "minInputs": 1
            }
        },
        "groups_outputs": {
            "logs": {
                "hReadableName": "Logs",
                "description": ""
            }
        },
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)"
        }}

    expected = {
        "groups": {
            "gene_panel": {
                "hReadableName": "Gene panel",
                "description": "Fill the inputs below to generate the gene panel",
                "rules": "Fill at least one input",
                "minInputs": 1
            },
            "target_regions": {
                "hReadableName": "Target regions",
                "description": "Fill the input below to specify regions that will be analyzed",
                "minInputs": 1
            }
        },
        "groups_outputs": {
            "logs": {
                "hReadableName": "Logs",
                "description": ""
            }
        }}
    result = converter.get_groups_to_modify(test_data)

    assert result == expected


def test_get_inputs_to_modify():
    test_data = {
        "description": "example description",
        "changes": {
            "2.0.1": "",
            "2.0.0": "",
            "1.2.0": "",
            "1.1.0": "",
            "1.0.0": ""
        },
        "groups_outputs": {
            "logs": {
                "hReadableName": "Logs",
                "description": ""
            }
        },
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)"
        },
        "input_fastqs": {
            "index": 2,
            "paired": True,
            "multiselect": True,
            "name": "Fastq files",
            "type": "Array[File]",
            "description": "Choose list of paired gzipped fastq files both left and right [.fq.gz or .fastq.gz]",
            "extension": [
                ".fq.gz",
                ".fastq.gz"
            ]
        }
    }

    expected = {
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)"
        },
        "input_fastqs": {
            "index": 2,
            "paired": True,
            "multiselect": True,
            "name": "Fastq files",
            "type": "Array[File]",
            "description": "Choose list of paired gzipped fastq files both left and right [.fq.gz or .fastq.gz]",
            "extension": [
                ".fq.gz",
                ".fastq.gz"
            ]
        }
    }

    result = converter.get_inputs_to_modify(test_data)

    assert result == expected


def test_get_outputs_to_modify():
    test_data = {
        "copyright": "Copyright 2019-2021 Intelliseq",
        "name": "example name",
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)"
        },
        "variant6_input_phenotypes_description": {
            "hidden": True
        },
        "variant7_input_phenotypes_description": {
            "hidden": True
        },
        "output_html_report": {
            "name": "Report from genetic analysis in Polish",
            "type": "File",
            "copy": True,
            "description": "Report with results of the genetic analysis, html format, Polish version"
        },
        "output_docx_report": {
            "name": "Report from genetic analysis in Polish",
            "type": "File",
            "copy": True,
            "description": "Report with results of the genetic analysis, docx format, Polish version"
        }
    }

    expected = {
        "output_html_report": {
            "name": "Report from genetic analysis in Polish",
            "type": "File",
            "copy": True,
            "description": "Report with results of the genetic analysis, html format, Polish version"
        },
        "output_docx_report": {
            "name": "Report from genetic analysis in Polish",
            "type": "File",
            "copy": True,
            "description": "Report with results of the genetic analysis, docx format, Polish version"
        }
    }

    result = converter.get_outputs_to_modify(test_data)

    assert result == expected
