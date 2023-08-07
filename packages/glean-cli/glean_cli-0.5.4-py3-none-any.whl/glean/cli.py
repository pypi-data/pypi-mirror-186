import logging
import os
from typing import Optional, List
import webbrowser

import click
from requests import Session
import ruamel.yaml
from yaspin import yaspin

from glean import VERSION

from glean.credentials import get_credentials
from glean.glean_api import (
    build_details_uri,
    clear_model_cache,
    create_build_from_git_revision,
    create_build_from_local_files,
    login,
    preview_model_uri,
    get_datasources,
    get_tables,
    get_model_and_build_summary,
    export_query,
)
from glean.utils.cli import cli_error_boundary, getenv_bool
from glean.utils.grn import GRN_TYPE_KEY_MODEL, parse_grn


GLEAN_DEBUG = getenv_bool("GLEAN_DEBUG")

# Turning this on will result in secrets getting logged to stdout.
GLEAN_VERBOSE_DEBUG_UNSAFE = getenv_bool("GLEAN_VERBOSE_DEBUG_UNSAFE")


MAX_COLUMN_REGEX_LENGTH = 30
MAX_COLUMN_FILTER_CHARS = 1000


def main():
    with cli_error_boundary(debug=GLEAN_DEBUG):
        cli()


git_revision_option = click.option(
    "--git-revision",
    type=str,
    required=False,
    help="""
    If specified, Glean will pull configuration files from your configured git repository at the provided commit,
    instead of using local files.
    """,
)
git_path_option = click.option(
    "--git-path",
    type=str,
    required=False,
    help="""
    A path within your git repo that will be used as the top-level directory for the Build.
    Only applicable when also using the `--git-revision` flag.
    """,
)
local_path_argument = click.argument(
    "filepath", type=click.Path(exists=True), default="."
)


@click.group(context_settings=dict(max_content_width=130))
@click.version_option(version=VERSION, prog_name="Glean")
@click.option(
    "--credentials-filepath",
    type=str,
    default="~/.glean/glean_access_key.json",
    show_default=True,
    help="Path to your Glean access key credentials. You can also control this by setting a "
    "GLEAN_CREDENTIALS_FILEPATH environment variable.",
    envvar="GLEAN_CREDENTIALS_FILEPATH",
)
@click.option(
    "--allow-dangerous-empty-build",
    is_flag=True,
    default=False,
    help="Allow builds with no config files. WARNING: this will allow a build to delete all of your resources, including non-dataops resources that depend on your dataops resources!",
)
@click.pass_context
def cli(ctx, credentials_filepath, allow_dangerous_empty_build=False):
    """A command-line interface for interacting with Glean."""
    if GLEAN_DEBUG or GLEAN_VERBOSE_DEBUG_UNSAFE:
        _enable_http_logging()

    ctx.ensure_object(dict)
    ctx.obj["allow_dangerous_empty_build"] = allow_dangerous_empty_build
    ctx.obj["credentials"] = get_credentials(os.path.expanduser(credentials_filepath))


@cli.command()
@git_revision_option
@git_path_option
@local_path_argument
@click.pass_context
def preview(ctx, git_revision, git_path, filepath):
    """Validates resource configurations and generates a preview link."""
    click.echo("🏗️  Creating preview build...")
    build_results = _create_build_using_options(
        ctx,
        filepath,
        git_revision=git_revision,
        git_path=git_path,
        deploy=False,
    )
    _echo_build_results(build_results, False)


@cli.command()
@git_revision_option
@git_path_option
@local_path_argument
@click.option(
    "--preview / --no-preview",
    default=True,
    help="Whether to generate a Preview Build before deploying.",
)
@click.pass_context
def deploy(
    ctx: click.Context,
    git_revision: Optional[str],
    git_path: Optional[str],
    filepath: str,
    preview: bool,
):
    """Validates and deploys resource configurations to your project."""
    if preview:
        click.echo("🏗️  Creating preview build...")
        build_results = _create_build_using_options(
            ctx,
            filepath,
            git_revision=git_revision,
            git_path=git_path,
            deploy=False,
        )
        _echo_build_results(build_results, False)
        click.echo("")
        if not click.confirm("Continue with deploy?"):
            exit(1)

    click.echo("🚀 Creating deploy build...")
    build_results = _create_build_using_options(
        ctx,
        filepath,
        git_revision=git_revision,
        git_path=git_path,
        deploy=True,
    )
    _echo_build_results(build_results, True)
    click.echo("")
    click.echo(click.style("✅ Deploy complete.", fg="bright_green"))


@cli.command()
@click.pass_context
def databases(ctx):
    """See your available database connections.

    A database connection can be added in the Settings tab on glean.io."""
    s = Session()
    project_id = login(s, ctx.obj["credentials"])

    datasources = get_datasources(s, project_id)
    _echo_datasources(datasources)


@cli.command()
@click.argument("database")
@click.pass_context
def tables(ctx, database):
    """Specify a database connection and see its available tables."""
    s = Session()
    project_id = login(s, ctx.obj["credentials"])

    datasources = get_datasources(s, project_id)
    if database not in datasources:
        _echo_datasource_not_found(database, datasources)
        exit(1)

    datasource_id = datasources[database]

    tables = get_tables(s, datasource_id)
    table_names = list(tables.keys())
    _echo_tables(table_names, database)


@cli.group()
@click.pass_context
def cache(ctx):
    """Glean stores the results of queries in a cache so that users don't have
    to access the database again."""
    pass


@cache.command("clear")
@click.argument("resource_grn")
@click.pass_context
def cache_clear(ctx, resource_grn):
    """Clears the cache for the associated resource."""
    s = Session()
    login(s, ctx.obj["credentials"])

    grn = parse_grn(resource_grn)
    if not grn.gluid:
        click.echo("GRN must specify an id when clearing cache.")
        exit(1)
    if grn.resource_type != GRN_TYPE_KEY_MODEL:
        click.echo("Cache can only be cleared for models.")
        exit(1)

    clear_model_cache(s, grn.gluid)
    click.echo(f"Successfully cleared cache for {resource_grn}.")


@cli.command()
@click.argument("database")
@click.argument("table")
@click.option(
    "--exclude",
    "-e",
    help="A comma-separated list of columns to exclude from the preview.",
)
@click.option(
    "--include",
    "-i",
    help="A comma-separated list of columns to include in the preview.",
)
@click.option(
    "--regex",
    "-r",
    help="A regular expression to filter column names by. You can use this along with the --include and/or --exclude options to include columns regardless of the regex result.",
)
@click.option(
    "--skip-confirmation",
    is_flag=True,
    help="If set, the generated model configuration file will silently overwrite any existing files with the same name in your current directory.",
)
@click.pass_context
def explore(
    ctx: click.Context,
    database: str,
    table: str,
    exclude: str = "",
    include: str = "",
    regex: str = "",
    skip_confirmation: bool = False,
):
    """Explore your data! Specify a database and table to generate a Glean preview for it.

    DATABASE is the name of a Glean database connection you want to explore.
    TABLE is the name of a table within your DATABASE. Alternatively, it can be a SQL query wrapped in quotes.

    Usage examples:

    $ glean explore database_connection_name table_name

    $ glean explore database_connection_name "SELECT * FROM table_name"

    $ glean explore database_connection_name table_name --regex "[^date]$" --include important_date --exclude extra_info

    """
    s = Session()
    project_id = login(s, ctx.obj["credentials"])

    datasources = get_datasources(s, project_id)
    if database not in datasources:
        _echo_datasource_not_found(database, datasources)
        exit(1)
    datasource_id = datasources[database]

    _limit_column_filters(exclude, include, regex)

    model_spec = {
        "columnsToExclude": exclude.split(",") if exclude else [],
        "columnsToInclude": include.split(",") if include else [],
        "columnsRegex": regex if regex else "",
    }

    if not _infer_if_sql(table):
        tables = get_tables(s, datasource_id)
        if table not in tables:
            _echo_table_not_found(table, tables, database)
            exit(1)

        with yaspin(text="Generating your data model...", color="yellow") as spinner:
            model_spec["schema"] = tables[table]["schema"]
            model_spec["tableName"] = tables[table]["name"]
            model, build_summary = get_model_and_build_summary(
                s, datasource_id, project_id, **model_spec
            )
    else:
        with yaspin(text="Generating your data model...", color="yellow") as spinner:
            model_spec["sqlStatement"] = table
            model, build_summary = get_model_and_build_summary(
                s, datasource_id, project_id, **model_spec
            )

    config = export_query(
        s, "model", model, additional_headers={"Content-Type": "yaml"}
    )
    model_yaml = ruamel.yaml.load(config, Loader=ruamel.yaml.RoundTripLoader)
    if "grn" in model_yaml:
        del model_yaml["grn"]
    config = ruamel.yaml.dump(model_yaml, Dumper=ruamel.yaml.RoundTripDumper)

    filename = model["name"]
    _save_config(config, filename, skip_confirmation=skip_confirmation)

    _echo_build_results(build_summary, False, query_name="modelPreviewBuildFromGleanDb")
    webbrowser.open(preview_model_uri(model["id"], build_summary))


def _infer_if_sql(table: str) -> bool:
    """
    Guesses if the table input is a table or a SQL query.
    """
    return bool(table.count(" ") >= 3 and "select" in table.lower())


def _limit_column_filters(
    exclude: Optional[str], include: Optional[str], regex: Optional[str]
) -> None:
    """
    This limits column filter inputs to a reasonable size.
    There are the same checks server-side; this is for better user error messaging.
    """
    if exclude and include and not regex:
        click.secho(
            "Can't specify both columns to include and columns to exclude without a regex.",
            fg="red",
        )
        exit(1)
    if regex and len(regex) > MAX_COLUMN_REGEX_LENGTH:
        click.secho(
            f"Regex input is too long — it should be {MAX_COLUMN_REGEX_LENGTH} characters or less.",
            fg="red",
        )
        exit(1)
    if include and len(include) > MAX_COLUMN_FILTER_CHARS:
        click.secho(
            f"The list of columns to include should be less than {MAX_COLUMN_FILTER_CHARS} characters.",
            fg="red",
        )
        exit(1)
    if exclude and len(exclude) > MAX_COLUMN_FILTER_CHARS:
        click.secho(
            f"The list of columns to exclude should be less than {MAX_COLUMN_FILTER_CHARS} characters.",
            fg="red",
        )
        exit(1)


def _save_config(
    config: str, name: str, config_type: str = "yml", skip_confirmation: bool = False
) -> None:
    """Confirms with user and writes config file to user's local directory"""
    filename = f"{name}.{config_type}"
    click.echo("")
    click.echo(
        "Saving a model configuration file as "
        + click.style(f"{filename}", bold=True)
        + " in this directory."
    )

    write = True
    if os.path.exists(filename):
        if not skip_confirmation:
            if not click.confirm(
                "A file named "
                + click.style(f"{filename}", bold=True)
                + " already exists. Do you want to overwrite it?"
            ):
                write = False
                click.echo("")
                click.echo(
                    "Your preview build was generated, but a model configuration file was not saved."
                )

    if write:
        with open(filename, "w") as config_file:
            config_file.write(config)

    click.echo("")


def _create_build_using_options(
    ctx: click.Context,
    filepath: str,
    git_revision: Optional[str] = None,
    git_path: Optional[str] = None,
    deploy: bool = False,
    targets: Optional[set] = None,
):
    s = Session()
    project_id = login(s, ctx.obj["credentials"])
    allow_dangerous_empty_build = ctx.obj["allow_dangerous_empty_build"]
    if git_revision:
        return create_build_from_git_revision(
            s,
            project_id,
            git_revision,
            git_path,
            deploy,
            allow_dangerous_empty_build=allow_dangerous_empty_build,
        )
    else:
        return create_build_from_local_files(
            s,
            project_id,
            filepath,
            deploy,
            targets,
            allow_dangerous_empty_build=allow_dangerous_empty_build,
        )


def _echo_tables(table_names: list, datasource: str) -> None:
    click.secho(f"📂 Available Tables From {datasource}", fg="bright_green")
    _echo_list(table_names)


def _echo_table_not_found(table: str, tables: dict, datasource: str) -> None:
    """If table is not found in the available tables, output warning and display available tables."""
    click.echo("")
    click.secho(f"❗{table} was not found in {datasource}'s tables.", fg="red")
    click.echo("")
    _echo_tables(list(tables.keys()), datasource)
    click.echo("")


def _echo_datasources(datasources: dict) -> None:
    click.secho("🗒  Available Database Connections ", fg="bright_green")
    _echo_list(list(datasources.keys()))


def _echo_datasource_not_found(datasource: str, datasources: dict) -> None:
    """If datasource not found, output warning and available datasources."""
    click.echo("")
    click.secho(f"❗{datasource} was not found in your database connections.", fg="red")
    click.echo("")
    _echo_datasources(datasources)
    click.echo("")
    click.echo(
        "You can add another database connection in your Settings tab on glean.io."
    )
    click.echo("")


def _echo_build_results(build_results: dict, deploy: bool, query_name="createBuild"):
    """Outputs user-friendly build results."""
    if "errors" in build_results and build_results["errors"]:
        _echo_build_errors_and_exit(
            [
                e["extensions"]["userMessage"]
                for e in build_results["errors"]
                if "extensions" in e and "userMessage" in e["extensions"]
            ]
        )
    created_build_results = build_results["data"][query_name]

    if created_build_results["errors"]:
        _echo_build_errors_and_exit(created_build_results["errors"])

    click.echo(
        click.style("📦 Build ", fg="bright_green")
        + click.style(created_build_results["id"], bold=True)
        + click.style(" created successfully.", fg="bright_green")
    )
    click.echo("")

    if created_build_results["warnings"]:
        _echo_build_warnings(created_build_results["warnings"])

    _echo_build_resources(created_build_results["resources"], deploy)
    click.echo("")
    click.echo(f"Details: {build_details_uri(build_results, query_name=query_name)}")


def _echo_build_errors_and_exit(errors: List[str]):
    click.echo("")
    click.secho("―――――――――――――――――――――――――――――――――――――――――――――――――", fg="red")
    click.echo("❗ Errors encountered when creating your build")
    click.secho("―――――――――――――――――――――――――――――――――――――――――――――――――", fg="red")
    if not errors:
        errors = ["Something went wrong, please contact Glean for support."]
    _echo_list(errors, color="red")
    click.echo("")
    click.secho("Build failed.", fg="red")
    exit(1)


def _echo_build_warnings(warnings: List[str]):
    click.echo("")
    click.secho("―――――――――――――――――――――――――――――――――――――――――――――――――", fg="yellow")
    click.echo(" ⚠️  Warnings encountered when creating your build")
    click.secho("―――――――――――――――――――――――――――――――――――――――――――――――――", fg="yellow")
    if not warnings:
        warnings = ["Warning message missing, please contact Glean for support."]
    _echo_list(warnings, color="yellow")
    click.echo("")


def _echo_list(items: List[str], color="white"):
    for item in items:
        lines = item.split("\n")
        click.echo(click.style("*", fg=color) + "  " + lines[0])
        for line in lines[1:]:
            click.echo("   " + line)


def _echo_resources_with_status(resources: dict, status: str, title: str):

    models = resources[status]["models"]
    saved_views = resources[status]["savedViews"]
    dashboards = resources[status]["dashboards"]
    color_palettes = resources[status]["colorPalettes"]

    combinedResources = models + saved_views + dashboards + color_palettes

    if combinedResources:
        click.echo(title)
        _echo_list(
            [
                click.style("Model - ", fg="bright_black")
                + click.style(r["name"], fg="white")
                for r in models
            ]
        )
        _echo_list(
            [
                click.style("View - ", fg="bright_black")
                + click.style(r["name"], fg="white")
                for r in saved_views
            ]
        )
        _echo_list(
            [
                click.style("Dashboard - ", fg="bright_black")
                + click.style(r["name"], fg="white")
                for r in dashboards
            ]
        )
        _echo_list(
            [
                click.style("Color Palette - ", fg="bright_black")
                + click.style(r["name"], fg="white")
                for r in color_palettes
            ]
        )
        click.echo()


def _echo_build_resources(resources: dict, deploy: bool):

    added = click.style("Added:" if deploy else "Will add:", bold=True, fg="green")
    _echo_resources_with_status(resources, "added", added)

    updated = click.style(
        "Updated:" if deploy else "Will update:", bold=True, fg="cyan"
    )
    _echo_resources_with_status(resources, "changed", updated)

    deleted = click.style("Deleted:" if deploy else "Will delete:", bold=True, fg="red")
    _echo_resources_with_status(resources, "deleted", deleted)

    not_modified = click.style("Unchanged:", bold=True)
    _echo_resources_with_status(resources, "unchanged", not_modified)


def _enable_http_logging():
    # From: https://docs.python-requests.org/en/master/api/#api-changes
    from http.client import HTTPConnection

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    if GLEAN_VERBOSE_DEBUG_UNSAFE:
        HTTPConnection.debuglevel = 1
