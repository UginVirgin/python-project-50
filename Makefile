lint:
	uv run ruff check

run:
	uv run python3 -m gendiff.scripts.main -f plain tests/fixtures/file1_nested.json tests/fixtures/file2_nested.json

run-stylish:
	uv run python3 -m gendiff.scripts.main -f stylish tests/fixtures/file1_nested.json tests/fixtures/file2_nested.json