import pytest
from gendiff import generate_diff
from tests.fixtures.stylish_result import STYLISH_RESULT
from tests.fixtures.simple_result import SIMPLE_RESULT
from tests.fixtures.plain_result import PLAIN_RESULT
from tests.fixtures.json_result import JSON_RESULT


@pytest.fixture
def paths():
    paths = {
        "json1": "tests/fixtures/file1.json",
        "json2": "tests/fixtures/file2.json",
        "yml1": "tests/fixtures/file1.yml",
        "yml2": "tests/fixtures/file2.yml",
        "rec_json1": "tests/fixtures/recursive1.json",
        "rec_json2": "tests/fixtures/recursive2.json",
        "rec_yml1": "tests/fixtures/recursive1.yml",
        "rec_yml2": "tests/fixtures/recursive2.yml",
    }
    return paths


def get_result(path):
    with open(path) as file:
        result = file.read()
    return result


@pytest.fixture
def format_name():
    format_name = {
        "stylish": "stylish",
        "plain": "plain",
        "json": "json"
    }
    return format_name


def test_generate_diff(paths, format_name):
    result_diff_json = generate_diff(
        paths["json1"],
        paths["json2"],
        format_name["stylish"],
    )
    result_diff_yml = generate_diff(
        paths["yml1"],
        paths["yml2"],
        format_name["stylish"],
    )
    result_diff_recursive_json = generate_diff(
        paths["rec_json1"],
        paths["rec_json2"],
        format_name["stylish"],
    )
    result_diff_recursive_yml = generate_diff(
        paths["rec_yml1"],
        paths["rec_yml2"],
        format_name["stylish"],
    )
    result_diff_plain_json = generate_diff(
        paths["rec_json1"],
        paths["rec_json2"],
        format_name["plain"],
    )
    result_diff_plain_yml = generate_diff(
        paths["rec_yml1"],
        paths["rec_yml2"],
        format_name["plain"],
    )
    result_diff_json_json = generate_diff(
        paths["rec_json1"],
        paths["rec_json2"],
        format_name["json"],
    )
    result_diff_json_yml = generate_diff(
        paths["rec_yml1"],
        paths["rec_yml2"],
        format_name["json"],
    )
    assert result_diff_json == SIMPLE_RESULT
    assert result_diff_yml == SIMPLE_RESULT
    assert result_diff_recursive_json == STYLISH_RESULT
    assert result_diff_recursive_yml == STYLISH_RESULT
    assert result_diff_plain_json == PLAIN_RESULT
    assert result_diff_plain_yml == PLAIN_RESULT
    assert result_diff_json_json == JSON_RESULT
    assert result_diff_json_yml == JSON_RESULT
