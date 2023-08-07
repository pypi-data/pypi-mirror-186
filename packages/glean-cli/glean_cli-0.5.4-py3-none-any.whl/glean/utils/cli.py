from os import environ
from contextlib import contextmanager


def getenv_bool(key: str) -> bool:
    return environ.get(key, "false").lower() in ["true", "t", "1", "*"]


@contextmanager
def cli_error_boundary(debug=False):
    try:
        yield
    except Exception as err:
        if debug:
            # will raise the whole stack trace
            raise
        else:
            # just print the error description
            print(f"Unexpected Error: {type(err).__name__}: {err}")
            exit(1)
