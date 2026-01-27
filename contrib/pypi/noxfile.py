#!/usr/bin/env python3

import glob
import nox
from pathlib import Path

nox.options.sessions = ["lint", "tests", "build"]

@nox.session
def lint(session):
    session.install("ruff", "mypy")
    session.run("ruff", "check", "src/bitbake_setup")
    # Ignore mypy for now as there are too many errors in imported modules
    # session.run("mypy", "src/bitbake_setup")

@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest")

@nox.session
def build(session):
    session.install("build", "twine")
    session.run("python", "-m", "build")

    # Verify the wheel installs cleanly
    wheels = list(Path("dist").glob("*.whl"))
    session.install(str(wheels[0]))
    session.run("bitbake-setup", "--help")