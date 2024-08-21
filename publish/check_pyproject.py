import argparse
import http
import logging
import os
import sys
import tomllib
from http.client import HTTPResponse, HTTPSConnection

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def read_pyproject(git_tag: str):
    if git_tag.startswith("v"):
        git_tag = git_tag[1:]

    project_pypi_host: str = "pypi.org"
    project_pypi_url: str = "project/NGOHub"

    pyproject_path = os.path.abspath(os.path.join(os.pardir, "pyproject.toml"))

    with open(pyproject_path, "rb") as f:
        pyproject_contents = tomllib.load(f)

    project_version: str = pyproject_contents["project"]["version"]

    if project_version != git_tag:
        logger.info(f"Tag {git_tag} does not match the version from `pyproject.toml` {project_version}")
        return 1

    current_version_url: str = f"/{project_pypi_url}/{project_version}/"
    conn: HTTPSConnection = http.client.HTTPSConnection(project_pypi_host)
    conn.request("GET", url=current_version_url)
    response: HTTPResponse = conn.getresponse()

    if response.status != http.HTTPStatus.NOT_FOUND:
        logger.info("A tag with this version already exists on pypi")
        return 1

    return 0


if __name__ == "__main__":
    """
    Read the contents of the `pyproject.toml` file and return 0 if the version is tagged and does not exist in pypi.
    Returns 1 otherwise.
    """
    parser = argparse.ArgumentParser(
        prog="Check tag version",
        description=(
            "Read the contents of the `pyproject.toml` file and return 0 if the version is tagged and does not exist in pypi."
            "Returns 1 otherwise."
        ),
    )

    parser.add_argument("-t", "--tag")

    args = parser.parse_args()

    tag: str = args.tag
    if not tag:
        raise ValueError("No tag provided")

    exit_code = read_pyproject(tag)
    sys.exit(str(exit_code))
