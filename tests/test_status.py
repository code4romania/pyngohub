from ngohub.core import NGOHub


def test_health_returns_ok():
    hub = NGOHub("/")
    assert hub.get_health() == "OK"


def test_version_returns_version_revision():
    hub = NGOHub("/")
    response = hub.get_version()
    assert "version" in response
    assert "revision" in response


def test_file_returns_path():
    hub = NGOHub("/")
    file_path = "test.txt"
    response = hub.get_file_url(file_path)

    assert f"amazonaws.com/{file_path}?AWSAccessKeyId=" in response
