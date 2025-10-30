import pytest

from gendiff.scripts.gendiff import generate_diff, stylish


@pytest.mark.parametrize("file1, file2, expected_result", [
    (
        "tests/fixtures/file1.json", 
     "tests/fixtures/file2.json", 
     "tests/expected_result_json.txt"
     ),
     (
        "tests/fixtures/file1.yaml", 
     "tests/fixtures/file2.yaml", 
     "tests/expected_result_yaml.txt"
     )
])
def test_gendiff(file1, file2, expected_result):
    diff = generate_diff(file1, file2)
    stylish_diff = stylish(diff)
    expected_result = read_file(expected_result)
    assert stylish_diff == expected_result


def read_file(file):
    with open(file, "r") as f:
        return f.read().strip()
