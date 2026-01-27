# Development Instructions

## Requirements

- Python >= 3.9
- pip >= 19 (for installation)
- git (for SCM-based versioning)

## Automated testing

The steps to lint, build, and test the bitbake-setup pypi packaging have been automated with the nox tool.  This tool automatically creates a Python virtual environment for you.

To run the linters do:
```bash
nox -s lint
```

To run the build do:
```bash
nox -s build
```

To run the tests do:
```bash
nox -s tests
```

## Manual Steps

### Building

To install the development tools manually run:
```bash
python3 -m pip install -e '.[dev]'
```

To build a wheel (.whl) then use:
```bash
python3 -m build
```

This produces a wheel (.whl) file in the dist directory.  This may be installed using pip.

### Testing

```bash
python3 -m pip install -e '.[test]'
pytest
```

### Linting

```bash
python3 -m pip install -e '.[lint]'

ruff check src/bitbake_setup
```