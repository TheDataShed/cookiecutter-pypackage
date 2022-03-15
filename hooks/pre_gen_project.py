import re
import subprocess
import sys
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
        subprocess.call(f"pyenv install {version}".split())


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
