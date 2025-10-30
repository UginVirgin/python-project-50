lint:
	uv run ruff check

run:
	uv run python3 -m gendiff.scripts.gendiff -f plain tests/fixtures/file1_nested.json tests/fixtures/file2_nested.json