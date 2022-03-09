#!/usr/bin/env python
import os
import subprocess
from sys import platform

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    # Run the rest of the setup here
    subprocess.call(["git", "init"])
    subprocess.call(["git", "config", "--user.email", "{{ cookiecutter.email }}"])
    subprocess.call(["git", "config", "--user.name", "{{ cookiecutter.name }}"])
    subprocess.call(["python", "-m", "venv", "venv"])

    if platform in ("linux", "linux2", "darwin"):
        # Unix
        subprocess.call(["./venv/Scripts/activate.bat"])
    elif platform == "win32":
        subprocess.call(["source", "venv/bin/activate"])

    subprocess.call(["pip", "install", "-r", "requirements_dev.txt", "--upgrade"])
    subprocess.call(["pre-commit install"])
    print("""
Finished initialising git
Finished creating a virtualenv in venv/
Finished installing dev dependencies
Finished installing pre-commit hooks
""")
