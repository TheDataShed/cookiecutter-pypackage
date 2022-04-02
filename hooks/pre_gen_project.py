import os
import re
import subprocess
import sys
from pathlib import Path
from shutil import which


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    return which(name) is not None


def check_valid_module_name():
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    module_name = "{{ cookiecutter.project_slug}}"

    if not re.match(MODULE_REGEX, module_name):
        print(
            f"""
        ERROR: The project slug ({module_name}) is not a valid Python module name.
        Please do not use a - and use _ instead
        """
        )

        # Exit to cancel project
        sys.exit(1)


def check_correct_python_version_available(version="{{ cookiecutter.python_version }}"):
    results = subprocess.check_output(
        "pyenv versions --skip-aliases --bare".split()
    ).decode("utf-8")
    for result in results.split("\n"):
        if result.endswith(version):
            break
    else:
        print(f"Missing python version: {version}")
        curdir = Path.cwd()
        pyenv_root = os.getenv("PYENV_ROOT")
        if pyenv_root:
            pyenv_dir = Path(pyenv_root)
            os.chdir(pyenv_dir)
            subprocess.call("git pull".split())
            os.chdir(curdir)
            subprocess.call(f"pyenv install {version}".split())

            # Install/upgrade dependencies if missing
            pyenv_ver_pip = pyenv_dir / "versions" / version / "bin" / "pip"
            subprocess.call(f"{pyenv_ver_pip} install --upgrade pre-commit pip".split())

        else:
            print("Can't find PYENV_ROOT, please make sure it's set up")
            exit()


if __name__ == "__main__":
    check_valid_module_name()
    if not is_tool("pyenv"):
        print(
            """
        You need to have installed pyenv and pyenv-virtualenv
        to use this cookiecutter. Please add the scripts to auto-activate
        your shell.

        Links:
        https://github.com/pyenv/pyenv
        https://github.com/pyenv/pyenv-virtualenv

        """
        )
        sys.exit(1)
    check_correct_python_version_available()
