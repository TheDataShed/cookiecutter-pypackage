"""Console script for {{cookiecutter.project_slug}}."""
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(*args):
    """
    Console script for {{cookiecutter.project_slug}}.

    {%- if cookiecutter.docstrings_style == 'sphinx' %}
    :param *args: A list of args to pass.
    :type *args: Optional[list]

    :return: A status message
    :rtype: int
    {%- else %}
    Args:
        *args (Optional[list]): A list of args to pass.

    Returns:
        int: A status message.

    {%- endif %}
    """
    len(args)
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0

{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main(*args):
    """
    Console script for {{cookiecutter.project_slug}}.

    :param args: A list of args to pass.
    :type args: Optional[list]

    :return: A status message
    :rtype: int
    """
    len(args)
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
