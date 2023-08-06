#!/usr/bin/env python3

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from ..spreadsheetutils import *


def test_get_workflows():
    test_data = {
        "author": "https://gitlab.com/olaf.tomaszewski",
        "copyright": "Copyright 2019-2021 Intelliseq",
        "name": "example name",
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)",
        },
        "input_fastqs": {
            "index": 2,
            "paired": True,
            "multiselect": True,
            "name": "Fastq files",
            "type": "Array[File]",
            "description": "Choose list of paired gzipped fastq files both left and right [.fq.gz or .fastq.gz]",
            "extension": [".fq.gz", ".fastq.gz"],
        },
    }

    expected = ["author", "copyright", "name"]
    expected.sort()

    result = get_workflows(test_data)
    result.sort()

    assert result == expected


def test_get_inputs():
    test_data = {
        "description": "example description",
        "changes": {"2.0.1": "", "2.0.0": "", "1.2.0": "", "1.1.0": "", "1.0.0": ""},
        "groupOutputs": {"logs": {"hReadableName": "Logs", "description": ""}},
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)",
        },
        "input_fastqs": {
            "index": 2,
            "paired": True,
            "multiselect": True,
            "name": "Fastq files",
            "type": "Array[File]",
            "description": "Choose list of paired gzipped fastq files both left and right [.fq.gz or .fastq.gz]",
            "extension": [".fq.gz", ".fastq.gz"],
        },
    }

    expected = ["input_sample_id", "input_fastqs"]
    expected.sort()

    result = get_inputs(test_data)
    result.sort()

    assert result == expected


def test_get_outputs():
    test_data = {
        "copyright": "Copyright 2019-2021 Intelliseq",
        "name": "example name",
        "input_sample_id": {
            "index": 1,
            "name": "Sample id",
            "multiselect": False,
            "type": "String",
            "description": "Enter a sample name (or identifier)",
        },
        "variant6_input_phenotypes_description": {"hidden": True},
        "variant7_input_phenotypes_description": {"hidden": True},
        "output_html_report": {
            "name": "Report from genetic analysis in Polish",
            "type": "File",
            "copy": True,
            "description": "Report with results of the genetic analysis, html format, Polish version",
        },
        "output_docx_report": {
            "name": "Report from genetic analysis in Polish",
            "type": "File",
            "copy": True,
            "description": "Report with results of the genetic analysis, docx format, Polish version",
        },
    }

    expected = ["output_html_report", "output_docx_report"]
    expected.sort()

    result = get_outputs(test_data)
    result.sort()

    assert result == expected


def test_remove_surrounding_whitespaces():
    test_data = [
        {
            "  readonly_name ": "abc ",
            "name ": "abc workflow",
            " description": "  ",
            " readonly_type ": "File ",
            " groupId": "",
            "workflow_variant": " germline",
        },
        {
            "readonly_name": " sample_id",
            "name": "Sample id",
            "description": " Enter a sample name (or identifier). ",
            "readonly_type": "String",
            "groupId": "",
            "workflow_variant": "germline, pgx-genotyping-report, mobigen, panel-hpo, fq-qc, vcf-to-acmg-report, somatic, sv-calling, iontorrent, prs, mito ",
        },
        {
            "readonly_name ": "name  ",
            " name": "Name  ",
            "  description": "Description ",
            "  readonly_type": " String",
            " groupId": "id  ",
            "workflow_variant": " somatic",
        },
    ]

    expected = [
        {
            "readonly_name": "abc",
            "name": "abc workflow",
            "description": "",
            "readonly_type": "File",
            "groupId": "",
            "workflow_variant": "germline",
        },
        {
            "readonly_name": "sample_id",
            "name": "Sample id",
            "description": "Enter a sample name (or identifier).",
            "readonly_type": "String",
            "groupId": "",
            "workflow_variant": "germline, pgx-genotyping-report, mobigen, panel-hpo, fq-qc, vcf-to-acmg-report, somatic, sv-calling, iontorrent, prs, mito",
        },
        {
            "readonly_name": "name",
            "name": "Name",
            "description": "Description",
            "readonly_type": "String",
            "groupId": "id",
            "workflow_variant": "somatic",
        },
    ]

    result = remove_surrounding_whitespaces(test_data)

    for row in result:
        assert row in expected
