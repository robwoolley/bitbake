# Development Instructions

## Requirements

- Python >= 3.9
- pip >= 19 (for installation)
- git (for SCM-based versioning)

## Automated testing

To lint the `bitbake-setup` pypi packaging, run the ruff tool.
```bash
ruff check bin/bitbake-setup contrib/pypi
```

The steps to build, and test the `bitbake-setup` pypi packaging have been automated with the `bitbake-selftest` tool.  This tool automatically creates a Python virtual environment for you.

Run the bitbake-selftest
```bash
BB_SKIP_PYPI_TESTS=no bin/bitbake-selftest -v bb.tests.setup.PyPIPackagingTest
```

## Manual Steps

### Create the development sandbox

To create the development sandbox run:
```bash
contrib/pypi/package-bitbake-setup.py
cd packaging_workshop
```

### Testing

Install the tests in the workspace:
```bash
python3 -m pip install -e '.[test]'
```

Run pytest in the workspace:
```bash
pytest tests
```

### Linting

Install the linting tools in the workspace:
```bash
python3 -m pip install -e '.[lint]'
```

Run the linting tools in the workspace:
```bash
ruff check src/bitbake_setup
```

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

# Installing

```bash
python3 -m pip install dist/bitbake_setup-0.0.0-py3-none-any.whl
```
