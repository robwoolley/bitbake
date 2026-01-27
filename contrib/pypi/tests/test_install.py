import subprocess
import sys

def test_imports():
    import bb
    import bs4
    import ply
    import bitbake_setup

def test_console_script():
    result = subprocess.run(
        ["bitbake-setup", "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert result.returncode == 0
