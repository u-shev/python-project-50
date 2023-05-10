import pytest
from gendiff import generate_diff


@pytest.fixture
def paths():
    paths = {
            "json1": "tests/fixtures/file1.json",
            "json2": "tests/fixtures/file2.json",
            "yml1": "tests/fixtures/file1.yml",
            "yml2": "tests/fixtures/file2.yml",
            }
    return paths


#@pytest.fixture
#def result():
#    with open("tests/fixtures/result") as file:
#        result = file.read()
#        return result


def test_generate_diff(paths):
    result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
    result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
    assert result_diff_json == '{\n - follow: false\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: true\n}'
    assert result_diff_yml == '{\n - follow: false\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: true\n}'
