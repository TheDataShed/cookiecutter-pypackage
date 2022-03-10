{% set is_open_source = cookiecutter.open_source_license != 'Not
open source' -%} {% for _ in cookiecutter.project_name %}={% endfor
%} {{ cookiecutter.project_name }} {% for _ in
cookiecutter.project_name %}={% endfor %}

[![Made by The Data Shed](.github/ds-badge.svg)](https://thedatashed.co.uk)

[![Security Status](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

{% if is_open_source %}

[![Pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)(https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})]

[![Travis](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)(https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}]

[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("*", "-") }}/badge/?version=latest)
(https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)]

{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}

[![Updates](https://pyup.io/repos/github/>{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }}/shield.svg)(https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }})
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %} _ Free software: {{
cookiecutter.open_source_license }} _ Documentation: <https://>{{
cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

# Features

-   TODO
