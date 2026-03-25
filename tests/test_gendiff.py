import pytest
from gendiff.scripts.gendiff import generate_diff

@pytest.mark.parametrize("file1, file2, formatter, expected_result", [
    (
        "file1.json",
        "file2.json",
        "json",
        "expected_result_json.txt"
    ),
    (
        "file1.json",
        "file2.json",
        "plain",
        "expected_result_plain.txt"
    ),
    (
        "file1.json",
        "file2.json",
        "stylish",
        "expected_result_stylish.txt"
    ),
    (
        "file1_nested.json",
        "file2_nested.json",
        "json",
        "expected_result_nested_json.txt"
    ),
    (
        "file1_nested.json",
        "file2_nested.json",
        "plain",
        "expected_result_nested_plain.txt"
    ),
    (
        "file1_nested.json",
        "file2_nested.json",
        "stylish",
        "expected_result_nested_stylish.txt"
    ),
    (
        "file1.yaml",
        "file2.yaml",
        "json",
        "expected_result_json.txt"
    ),
])

def test_gendiff(get_fixture_path, read_fixture, file1, file2, formatter, expected_result):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_result_read = read_fixture(expected_result)

    result = generate_diff(file1_path, file2_path, formatter)

    assert result == expected_result_read

