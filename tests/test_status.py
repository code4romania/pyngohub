from ngohub.status import get_file_url, get_health, get_version


def test_health_returns_ok():
    assert get_health() == "OK"


def test_version_returns_version_revision():
    response = get_version()
    assert "version" in response
    assert "revision" in response


def test_file_returns_path():
    file_path = "test.txt"
    response = get_file_url(file_path)

    assert f"amazonaws.com/{file_path}?AWSAccessKeyId=" in response
