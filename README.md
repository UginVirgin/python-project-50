### Hexlet tests and linter status:
[![Actions Status](https://github.com/UginVirgin/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/UginVirgin/python-project-50/actions)

asciinema rec:
https://asciinema.org/a/auvug1kF0sb4MPtwAVIca0Il3

Sonar Badges:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=UginVirgin_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=UginVirgin_python-project-50)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=UginVirgin_python-project-50)](https://sonarcloud.io/summary/new_code?id=UginVirgin_python-project-50)

[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-light.svg)](https://sonarcloud.io/summary/new_code?id=UginVirgin_python-project-50)

# GenDiff

CLI tool for comparing configuration files (JSON, YAML) and generating difference reports in various formats.

## Features

- ✅ Supports JSON and YAML files
- ✅ Three output formats: stylish (default), plain, and JSON
- ✅ Deep comparison of nested structures
- ✅ Easy to integrate into CI/CD pipelines

## Installation

### Prerequisites
- Python 3.13 or higher
- pip (Python package manager)

### Install from source

```bash
# Clone repository
git clone https://github.com/UginVirgin/python-project-50.git
cd python-project-50

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install package
pip install -e .
```

## Usage

### Command line

```bash
# Basic comparison (stylish format)
gendiff file1.json file2.json

# Plain text format
gendiff -f plain file1.json file2.json

# JSON format
gendiff -f json file1.json file2.json

# Help
gendiff --help
```

### As Python module

```python
from gendiff.scripts.gendiff import generate_diff

# Get diff in stylish format (default)
diff = generate_diff('file1.json', 'file2.json')
print(diff)

# Get diff in plain format
diff = generate_diff('file1.json', 'file2.json', 'plain')
```

## Output examples

### Stylish format (default)
```diff
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### Plain format
```
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From '50' to '20'
Property 'verbose' was added with value: true
```

## Development

### Setup for development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Check code style
flake8 gendiff/ tests/
black --check gendiff/ tests/
```
