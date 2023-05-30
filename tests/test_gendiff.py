import pytest
from gendiff import generate_diff
from tests.fixtures.stylish_result import STYLISH_RESULT
from tests.fixtures.plain_result import PLAIN_RESULT

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


def test_generate_diff(paths):
    result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
    result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
    result_diff_recursive_json = str(generate_diff(paths["rec_json1"], paths["rec_json2"]))
    result_diff_recursive_yml = str(generate_diff(paths["rec_yml1"], paths["rec_yml2"]))
    assert result_diff_recursive_json == STYLISH_RESULT
    assert result_diff_recursive_yml == STYLISH_RESULT
    assert result_diff_json == PLAIN_RESULT
    assert result_diff_yml == PLAIN_RESULT
