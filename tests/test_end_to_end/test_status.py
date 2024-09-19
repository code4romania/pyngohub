import pytest

from ngohub.core import NGOHub
from tests.test_end_to_end.schemas import VERSION_REVISION_SCHEMA


def test_raw_health_returns_ok():
    hub = NGOHub(pytest.ngohub_api_url)

    assert hub.get_raw_health() == "OK"


def test_health_returns_true():
    hub = NGOHub(pytest.ngohub_api_url)

    assert hub.is_healthy() is True


def test_raw_version_returns_version_revision_dict():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_version()

    assert VERSION_REVISION_SCHEMA.validate(response)


def test_version_returns_version_revision():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_version()

    assert response.version is not None
    assert response.revision is not None


def test_file_returns_path():
    hub = NGOHub(pytest.ngohub_api_url)
    file_path = "test.txt"
    response = hub.get_file_url(file_path)

    assert f"amazonaws.com/{file_path}?AWSAccessKeyId=" in response
