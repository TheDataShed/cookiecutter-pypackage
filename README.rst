======================
Cookiecutter PyPackage
======================

.. image:: https://pyup.io/repos/github/KingMichaelPark/cookiecutter-pypackage/shield.svg
    :target: https://pyup.io/repos/github/KingMichaelPark/cookiecutter-pypackage/
    :alt: Updates

.. image:: https://travis-ci.org/KingMichaelPark/cookiecutter-pypackage.svg?branch=master
    :target: https://travis-ci.org/github/KingMichaelPark/cookiecutter-pypackage
    :alt: Build Status

.. image:: https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest
    :target: https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/KingMichaelPark/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing: `pytest`
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python  3.7, 3.8, 3.9
* Mkdocs docs: Documentation ready for generation with, for example, `Read the Docs`_
  Tagged releases get built a github pages build automatically.
* Pre-commit hooks inline with what is python standard. `Flake8, Black, Isort, Bandit, Docstrings Check` as
  well as pre-commit hooks for code quality and git commit message quality.
* commitzen: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)
* Uses `pyenv` to auto use the most recent stable python version and `pyenv virtualenv` to keep dependencies
  isolated. (Will install missing version if missing)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/KingMichaelPark/cookiecutter-pypackage.svg
    :target: https://travis-ci.org/KingMichaelPark/cookiecutter-pypackage
    :alt: Linux build status on Travis CI

Windows:

.. image:: https://ci.appveyor.com/api/projects/status/github/audreyr/cookiecutter-pypackage?branch=master&svg=true
    :target: https://ci.appveyor.com/project/audreyr/cookiecutter-pypackage/branch/master
    :alt: Windows build status on Appveyor

Quickstart
----------

This cookiecutter makes use of the following packages
that you need to have installed and configred for a seamless
installation:

1. [pyenv](https://github.com/pyenv/pyenv)
2. [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Once configured you should install `cookiecutter` and `pre-commit`




Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter pre-commit

Generate a Python package project::

    cookiecutter https://github.com/KingMichaelPark/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -e .["dev,docs"]``)
* Register_ your project with PyPI.
* Run the Travis CLI command ``travis encrypt --add deploy.password`` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* Release your package by pushing a new tag to master.
* This fork uses requirements in the setup.cfg file until [PEP621](https://peps.python.org/pep-0621/) is merged.
  I prefer having all requirements in one file split into groups.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html


Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

