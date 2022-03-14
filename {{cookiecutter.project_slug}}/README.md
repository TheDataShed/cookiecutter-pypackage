{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

[![Made by The Data Shed](docs/ds-badge.svg)](https://thedatashed.co.uk)

[![Security Status](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

{% if is_open_source %}

<p align="center">
<a href="https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}">
    <img src="https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions">
    <img src="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">
</a>


{% if cookiecutter.add_pyup_badge == 'y' %}
<a href="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/">
<img src="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg" alt="Updates">
</a>
{% endif %}

</p>
{% else %}
{% if cookiecutter.add_pyup_badge == 'y' %}
<p>
<a href="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/">
<img src="https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg" alt="Updates">
</a>
</p>
{% endif %}
{% endif %}

{{ cookiecutter.project_short_description }}

{%- if is_open_source %}
-   Free software: {{ cookiecutter.open_source_license }}
{%- endif %}

## Documentation

Is generated using `mkdocs` and will update on release as long as the pages option is turned on
for the repo, and setting the branch to build from as the root directory of `gh-pages`

- [Documentation](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }})


## Getting started

Activate your virtualenv:

```bash
source venv/bin/activate
# Run your tests
pytest
# Run on multple versions
tox
# See other commands in the make file like building docs etc...
```

### Bumping versions:

```bash
# On main
bump2version <patch | minor | major>
git push
git push --tags
```



## Features

-   TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [KingMichaelPark/cookiecutter-pypackage](https://github.com/KingMichaelPark/cookiecutter-pypackage) project template.
