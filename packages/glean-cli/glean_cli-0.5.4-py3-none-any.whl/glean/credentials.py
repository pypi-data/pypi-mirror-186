from dataclasses import dataclass
import json
from os import environ
import os.path
from typing import Optional


@dataclass
class CliCredentials:
    access_key_id: str
    access_key_token: str
    project_id: str


def get_credentials(credentials_filepath: str) -> CliCredentials:
    """Returns the credentials to use, as specified by the user via environment variables or credentials filepath."""
    project_id_from_env = environ.get("GLEAN_PROJECT_ID")
    access_key_id_from_env = environ.get("GLEAN_ACCESS_KEY_ID")
    access_key_token_from_env = environ.get("GLEAN_SECRET_ACCESS_KEY_TOKEN")
    if project_id_from_env and access_key_id_from_env and access_key_token_from_env:
        return CliCredentials(
            project_id=project_id_from_env,
            access_key_id=access_key_id_from_env,
            access_key_token=access_key_token_from_env,
        )
    elif [project_id_from_env, access_key_id_from_env, access_key_token_from_env].count(
        None
    ) < 3:
        raise RuntimeError(
            'Either all or none of these environment variables must be set: "GLEAN_PROJECT_ID", "GLEAN_ACCESS_KEY_ID", "GLEAN_SECRET_ACCESS_KEY_TOKEN"'
        )

    if not os.path.isfile(credentials_filepath):
        raise RuntimeError(f"Credentials file does not exist ({credentials_filepath})")

    with open(credentials_filepath, "r") as f:
        credentials_json = f.read()

    try:
        credentials = json.loads(credentials_json)
        return CliCredentials(**credentials)
    except Exception as e:
        raise RuntimeError("Invalid credentials file.") from e
