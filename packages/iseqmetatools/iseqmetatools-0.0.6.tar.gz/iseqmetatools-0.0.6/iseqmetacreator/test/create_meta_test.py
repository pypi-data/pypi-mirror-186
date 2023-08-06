#!/usr/bin/env python3

from iseqmetacreator import create_meta
from os import path
from numpy.testing import assert_equal

base_dir = path.join(path.dirname(path.realpath(__file__)), "../resources")


def test_organize_authors():
    authors = {"maria.paleczny@intelliseq.pl": "marysiaa"}
    expected = "marysiaa (e-mail: maria.paleczny@intelliseq.pl)"
    result = create_meta.organize_authors(authors)
    assert result == expected


def test_use_fields_json():
    result = create_meta.use_fields_json({'name': 'some_value', 'description': '', 'type': 'Int'}, "inputs")
    assert "max" in result["constraints"]
    assert "min" in result["constraints"]
    assert "constraints.min" not in result


def test_make_fields_1():
    wdl = path.join(base_dir, "wdls/dummy-module1.wdl")
    wdl_json = create_meta.read_wdl(wdl)
    jsons = create_meta.make_fields(wdl_json, wdl)
    assert len(jsons) > 0
    assert 'input_bam' in jsons
    assert 'input_gvcf_gz' in jsons
    assert 'output_bco' in jsons


def test_make_fields_2():
    wdl = path.join(base_dir, "wdls/dummy-task1.wdl")
    jsons = create_meta.make_fields(create_meta.read_wdl(wdl), wdl)
    assert len(jsons) > 0
    assert 'input_bam' in jsons
    assert 'output_out1' in jsons


def test_make_fields_3():
    wdl = path.join(base_dir, "wdls/dummy-task2.wdl")
    jsons = create_meta.make_fields(create_meta.read_wdl(wdl), wdl)
    assert len(jsons) > 0
    assert 'output_out2' in jsons


def test_make_fields_defaults():
    wdl = path.join(base_dir, "wdls/dummy-task1.wdl")
    jsons = create_meta.make_fields(create_meta.read_wdl(wdl), wdl)
    sample_id = jsons["input_sample_id"]["description"]
    output_bco = jsons["output_bco"]["description"]
    
    assert sample_id == "no_id_provided"
    assert output_bco == ""


def test_define_type():
    assert_equal(
        create_meta.define_type(
            {'type': {'innerType': {'name': 'Array', 'subtype': ['File'], 'kind': 'Type'}, 'kind': 'OptionalType'},
             'name': 'other_bams', 'expression': {'values': [], 'kind': 'ArrayLiteral'}, 'kind': 'Declaration'}),
        "Array[File]"
    )
    assert_equal(
        create_meta.define_type(
            {'type': {'innerType': {'name': 'Array', 'subtype': ['String'], 'kind': 'Type'}, 'kind': 'OptionalType'},
             'name': 'target_genes', 'expression': None, 'kind': 'Declaration'},
        ), 'Array[String]'
    )
    assert_equal(
        create_meta.define_type({'type': 'String', 'name': 'sample_id', 'expression': 'no_id_provided', 'kind': 'Declaration'}),
        'String'
    )
    assert_equal(
        create_meta.define_type({'type': 'Boolean', 'name': 'run_vcf_uniq', 'expression': False, 'kind': 'Declaration'}),
        'Boolean'
    )
    assert_equal(
        create_meta.define_type({'type': 'File', 'name': 'bpm_manifest_file', 'expression': None, 'kind': 'Declaration'}),
        'File'
    )
    assert_equal(
        create_meta.define_type({'type': 'Int', 'name': 'waiting_time', 'expression': 100000, 'kind': 'Declaration'}),
        'Int'
    )
    assert_equal(
        create_meta.define_type({'type': 'Float', 'name': 'vaf_filter_threshold', 'expression': 0.05, 'kind': 'Declaration'}),
        'Float'
    )
    
    # outputs
    assert_equal(
        create_meta.define_type(
            {'type': 'File', 'name': 'vcf', 'expression': {'lhs': 'gtc_to_vcf', 'rhs': 'vcf', 'kind': 'MemberAccess'},
             'kind': 'WorkflowOutputDeclaration'}),
        'File'
    )
    assert_equal(
        create_meta.define_type(
            {'type': {'innerType': {'name': 'Array', 'subtype': ['File'], 'kind': 'Type'}, 'kind': 'OptionalType'},
             'name': 'fastqc_zips', 'expression': {'lhs': 'fq_qc', 'rhs': 'fastqc_zip', 'kind': 'MemberAccess'},
             'kind': 'WorkflowOutputDeclaration'}),
        "Array[File]"
    )
    assert_equal(
        create_meta.define_type({'type': {'name': 'Array', 'subtype': ['File'], 'kind': 'Type'}, 'name': 'report_pdf',
                     'expression': {'lhs': 'report_mobigen', 'rhs': 'mobigen_report_pdf', 'kind': 'MemberAccess'},
                     'kind': 'WorkflowOutputDeclaration'}),
        'Array[File]'
    )


def test_remove_inputs():
    result = create_meta.remove_inputs(
        [{'type': 'String', 'name': 'module_name', 'expression': 'pgx_genotyping_report', 'kind': 'Declaration'},
         {'type': 'File', 'name': 'interval',
          'expression': {'name': 'select_first',
                         'params': [{'values': ['interval_list_resources', 'interval_list'], 'kind': 'ArrayLiteral'}],
                         'kind': 'FunctionCall'}, 'kind': 'Declaration'},
         {'type': 'String', 'name': 'sample_id', 'expression': 'no_id_provided', 'kind': 'Declaration'}])
    expected = [{'type': 'String', 'name': 'sample_id', 'expression': 'no_id_provided', 'kind': 'Declaration'}]
    
    assert result == expected

