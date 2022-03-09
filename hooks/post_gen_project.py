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
    subprocess.call(["git", "branch", "-m", "main"])

    print("Finished with git initialisation and virtualenv creation.")
    print("Please run make local-config to complete the installation")
