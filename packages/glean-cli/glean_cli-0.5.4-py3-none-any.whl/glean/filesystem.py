import os
import pathlib
from string import Template
from typing import Optional, Dict

from click import ClickException

from glean.utils.validate_config import is_valid_glean_config_file


VALID_FILE_EXTENSIONS = set([".json", ".yml", ".yaml"])


def build_spec_from_local(
    path: str, project_id: str, targets: Optional[set] = None
) -> dict:
    # Maps parent_directory -> filename -> file contents
    inline_files = []

    for root, subdirs, filenames in os.walk(path):
        for filename in filenames:
            if pathlib.Path(filename).suffix not in VALID_FILE_EXTENSIONS:
                continue
            if targets:
                if filename not in targets:
                    continue
            with open(os.path.join(root, filename), "r") as f:
                raw_contents = f.read()

                # Check that the file is a valid config file. Otherwise, ignore it.
                if not is_valid_glean_config_file(filename, raw_contents):
                    continue

                # Right now, changing the filepath of a config file changes its generated ID.
                # So, we set parentDirectory here to mimic the format that the server uses
                # when pulling from a git repo.
                path_suffix = f"/{path}" if path else ""
                parent_directory = root.replace(
                    path, f"/tmp/repos/{project_id}{path_suffix}"
                )
                try:
                    file_contents = Template(raw_contents).substitute(**os.environ)
                except KeyError as e:
                    raise ClickException(
                        f"No value found for environment variable substitution in {filename}: {str(e)}"
                    )

                inline_files.append(
                    {
                        "parentDirectory": parent_directory,
                        "filename": filename,
                        "fileContents": file_contents,
                    }
                )
    return {"inlineConfigFiles": inline_files}
