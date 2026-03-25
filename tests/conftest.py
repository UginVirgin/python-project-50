from pathlib import Path
import pytest


@pytest.fixture
def get_fixture_path():
    fixtures_path = Path(__file__).parent / 'fixtures'
    def _get(filename):
        return str(fixtures_path / filename)
    return _get

@pytest.fixture
def read_fixture():
    fixtures_dir = Path(__file__).parent / 'fixtures'
    def _read(filename):
        with open(fixtures_dir / filename) as f:
            return f.read().strip()
    return _read
