import json
import os
from typing import Optional, Tuple, Dict

import click
from click import ClickException
from requests import Session

from glean.credentials import CliCredentials
from glean.filesystem import build_spec_from_local
from glean import VERSION

GLEAN_BASE_URI = os.environ.get("GLEAN_CLI_BASE_URI", default="https://glean.io")


def login(session: Session, credentials: CliCredentials):
    """Authenticates the session with the provided credentials.

    :return The user's project ID, if successfully logged in.
    :raises ClickException if the login is not successful.
    """
    r = session.post(
        GLEAN_BASE_URI + "/auth/login-cli",
        data={
            "accessKeyId": credentials.access_key_id,
            "accessKeyToken": credentials.access_key_token,
        },
        headers={"Glean-CLI-Version": VERSION},
    )
    # TODO(dse): Show custom error message from server, if present.
    if r.status_code >= 500:
        raise ClickException("Unexpected error initiating your Glean session.")
    elif r.status_code >= 400:
        raise ClickException("Your access key is invalid.")
    if not r.ok:
        raise ClickException("Unexpected error initiating your Glean session.")

    return credentials.project_id


def create_build_from_git_revision(
    session: Session,
    project_id: str,
    git_revision: Optional[str],
    git_path: Optional[str],
    deploy: bool,
    allow_dangerous_empty_build: bool = False,
):
    """Creates a build based on a git revision and returns the result."""
    build_spec = {"configFilesFromGit": {"revision": git_revision, "path": git_path}}
    return _create_build(
        session, project_id, build_spec, deploy, allow_dangerous_empty_build
    )


def create_build_from_local_files(
    session: Session,
    project_id: str,
    path: str,
    deploy: bool,
    targets: Optional[set],
    allow_dangerous_empty_build: bool = False,
):
    """Creates a build using local files and returns the result."""
    build_spec = build_spec_from_local(path, project_id, targets)
    return _create_build(
        session, project_id, build_spec, deploy, allow_dangerous_empty_build
    )


def get_model_and_build_summary(
    session: Session,
    datasource_id: str,
    project_id: str,
    **kwargs,
) -> Tuple[dict, dict]:
    build_summary = _model_build_from_db(
        session,
        project_id,
        datasource_id,
        add_all_columns_as_attributes=True,
        **kwargs,
    )

    if "errors" in build_summary:
        click.secho("Error encountered when creating your build: ", fg="red")
        error = build_summary["errors"][0]
        if "extensions" in error:
            if "userMessage" in error["extensions"]:
                raise RuntimeError(error["extensions"]["userMessage"])
        raise RuntimeError(error.get("message", "Unknown error"))

    model = build_summary["data"]["modelPreviewBuildFromGleanDb"]["resources"]["added"][
        "modelBundles"
    ][0]["model"]
    return model, build_summary


def get_datasources(s: Session, project_id: str) -> dict:
    """Queries and formats datasources"""
    query = _get_data_connections(s, project_id)
    data_sources = {d["name"]: d["id"] for d in query["data"]["dataConnections"]}
    return data_sources


def clear_model_cache(s: Session, model_id: str) -> str:
    """Clears the cache for the specified model"""
    return _graphql_query(
        s,
        """
        mutation UpdateModelFreshnessKey($id: String!) {
            updateModelFreshnessKey(id: $id)
        }
        """,
        {"id": model_id},
    )


def _parse_table_data(table_data: dict) -> Dict[str, Dict[str, str]]:
    """Formats table names for output, and returns tables names and schemas"""
    tables = table_data["data"]["getAvailableGleanDbTables"]
    tables_by_name = {}
    for table in tables:
        name = (
            table["schema"] + "." + table["name"] if table["schema"] else table["name"]
        )
        tables_by_name[name] = {"schema": table["schema"], "name": table["name"]}
    return tables_by_name


def _create_build(
    session, project_id, build_spec, deploy, allow_dangerous_empty_build=False
):
    return _graphql_query(
        session,
        """
        mutation CreateBuild($projectId: String!, $buildSpec: BuildSpecInput!, $deploy: Boolean!, $allowEmptyBuild: Boolean) {
            createBuild( projectId: $projectId, buildSpec: $buildSpec, deploy: $deploy, allowEmptyBuild: $allowEmptyBuild) {
                id,
                resources {
                    added { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                    changed { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                    unchanged { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                    deleted { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                },
                warnings,
                errors
            }
        }
        """,
        {
            "projectId": project_id,
            "buildSpec": build_spec,
            "deploy": deploy,
            "allowEmptyBuild": allow_dangerous_empty_build,
        },
    )


def _get_data_connections(session: Session, project_id: str) -> dict:
    query = _graphql_query(
        session,
        """
        query dataConnections($projectId: String!){
            dataConnections(projectId: $projectId){
                id,
                name
            }
        }
        """,
        {"projectId": project_id},
    )
    return query


def _get_table_data(session: Session, datasource_id: str) -> dict:
    query = _graphql_query(
        session,
        """
        query getAvailableGleanDbTables($datasourceId: String!){
            getAvailableGleanDbTables (datasourceId: $datasourceId){
                name,
                schema
            }
        }
        """,
        {"datasourceId": datasource_id},
    )
    return query


def _model_build_from_db(
    session: Session,
    project_id: str,
    datasource_id: str,
    **kwargs,
) -> dict:
    """
    Queries modelPreviewBuildFromGleanDb controller.
    Returns relevant fields from model needed to generate a data ops config, as well the names of other resources for formatting purposes
    """

    add_all_columns_as_attributes = True
    table_name = kwargs.get("tableName")
    schema = kwargs.get("schema")
    sql_statement = kwargs.get("sqlStatement")
    columns_to_exclude = kwargs.get("columnsToExclude")
    columns_to_include = kwargs.get("columnsToInclude")
    columns_regex = kwargs.get("columnsRegex")

    query = _graphql_query(
        session,
        """
        mutation modelPreviewBuildFromGleanDb(
            $datasourceId: String!,
            $projectId: String!,
            $tableName: String,
            $schema: String,
            $sqlStatement: String,
            $columnsToExclude: [String]
            $columnsToInclude: [String]
            $columnsRegex: String
            $addAllColumnsAsAttributes: Boolean,
            ) {
            modelPreviewBuildFromGleanDb(
                datasourceId: $datasourceId,
                projectId: $projectId
                tableName: $tableName,
                schema: $schema,
                sqlStatement: $sqlStatement,
                columnsToExclude: $columnsToExclude,
                columnsToInclude: $columnsToInclude,
                columnsRegex: $columnsRegex,
                addAllColumnsAsAttributes: $addAllColumnsAsAttributes,
                ) {
                id,
                resources {
                    added {
                        models { name, id }
                        modelBundles {
                            model {
                                id,
                                project,
                                createdAt,
                                updatedAt,
                                name,
                                createdById,
                                isPrivate,
                                markedPrivateBy,
                                dataOpsRevision,
                                sourceDataTable,
                                attributes,
                                metrics,
                                cacheTtlSec,
                                description
                            }
                        },
                        savedViews { name },
                        dashboards { name },
                        colorPalettes { name }
                    }
                    changed { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                    unchanged { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                    deleted { models { name }, savedViews { name }, dashboards { name }, colorPalettes { name } }
                },
                warnings,
                errors
            }
        }
        """,
        {
            "datasourceId": datasource_id,
            "projectId": project_id,
            "tableName": table_name,
            "schema": schema,
            "sqlStatement": sql_statement,
            "columnsToExclude": columns_to_exclude,
            "columnsToInclude": columns_to_include,
            "columnsRegex": columns_regex,
            "addAllColumnsAsAttributes": add_all_columns_as_attributes,
        },
    )
    return query


def get_tables(s: Session, datasource_id: str) -> Dict[str, Dict[str, str]]:
    """Queries and formats table from datasource"""
    query = _get_table_data(s, datasource_id)
    tables = _parse_table_data(query)
    return tables


preview_uri = lambda build_results, query_name="createBuild": click.style(
    f"{GLEAN_BASE_URI}/app/?build={build_results['data'][query_name]['id']}",
    underline=True,
)

build_details_uri = lambda build_results, query_name="createBuild": click.style(
    f"{GLEAN_BASE_URI}/app/p/builds/{build_results['data'][query_name]['id']}",
    underline=True,
)

preview_model_uri = (
    lambda model_id, build_results, query_name="modelPreviewBuildFromGleanDb": f"{GLEAN_BASE_URI}/app/m/{model_id}?build={build_results['data'][query_name]['id']}"
)


def _graphql_query(session: Session, query: str, variables: dict):
    r = session.post(
        GLEAN_BASE_URI + "/graphql/",
        json={"query": query, "variables": variables},
        headers={"Glean-CLI-Version": VERSION},
    )
    if r.status_code == 504:
        raise ClickException(
            f"The Glean CLI client has timed out but your request is still running on our server. Please check your project's build page in a few minutes to see build results: {GLEAN_BASE_URI}/app/p/data-ops"
        )
    elif r.status_code != 200:
        raise ClickException("Unexpected error received from the Glean server.")

    results = r.json()
    graphql_exceptions = results.get("errors")
    if (
        graphql_exceptions
        and type(graphql_exceptions[0]) is dict
        and graphql_exceptions[0].get("message")
    ):
        error = graphql_exceptions[0]["message"]
        raise ClickException(
            f"Unexpected error received from the Glean server:\n  {error}"
        )

    return results


def export_query(
    session: Session, endpoint: str, data: dict, additional_headers: dict = {}
):
    """POST request to export controllers"""
    r = session.post(
        GLEAN_BASE_URI + f"/export/{endpoint}",
        data=json.dumps(data),
        headers={"Glean-CLI-Version": VERSION, **additional_headers},
    )
    if r.status_code != 200:
        raise ClickException("Unexpected error received from the Glean server.")
    return r.text
