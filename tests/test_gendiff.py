import pytest
from gendiff import generate_diff


def get_result(path):
    with open(path) as file:
        return file.read().strip()


@pytest.fixture
def format_name():
    format_name = {
        "stylish": "stylish",
        "plain": "plain",
        "json": "json"
    }
    return format_name


@pytest.mark.parametrize("file1, file2, expected",
                         [("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json",
                          get_result("tests/fixtures/simple_result.txt")),
                          ("tests/fixtures/file1.yml",
                           "tests/fixtures/file2.yml",
                          get_result("tests/fixtures/simple_result.txt")),
                          ("tests/fixtures/recursive1.json",
                           "tests/fixtures/recursive2.json",
                          get_result("tests/fixtures/stylish_result.txt")),
                          ("tests/fixtures/recursive1.yml",
                           "tests/fixtures/recursive2.yml",
                          get_result("tests/fixtures/stylish_result.txt")),
                          ])
def test_generate_diff_simple(file1, file2, expected):
    assert generate_diff(file1, file2, "stylish") == expected


@pytest.mark.parametrize("file1, file2, expected",
                         [("tests/fixtures/recursive1.json",
                           "tests/fixtures/recursive2.json",
                          get_result("tests/fixtures/plain_result.txt")),
                          ("tests/fixtures/recursive1.yml",
                           "tests/fixtures/recursive2.yml",
                          get_result("tests/fixtures/plain_result.txt")),
                          ])
def test_generate_diff_plain(file1, file2, expected):
    assert generate_diff(file1, file2, "plain") == expected


@pytest.mark.parametrize("file1, file2, expected",
                         [("tests/fixtures/recursive1.json",
                           "tests/fixtures/recursive2.json",
                          get_result("tests/fixtures/json_result.txt")),
                          ("tests/fixtures/recursive1.yml",
                           "tests/fixtures/recursive2.yml",
                          get_result("tests/fixtures/json_result.txt")),
                          ])
def test_generate_diff_json(file1, file2, expected):
    assert generate_diff(file1, file2, "json") == expected
