import pytest

from ngohub import NGOHub
from tests.test_end_to_end.schemas import PROFILE_SCHEMA


@pytest.mark.investigation_needed
def test_user_returns_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_profile(user_token=pytest.ngo_admin_token)

    assert PROFILE_SCHEMA.validate(response)
    assert response["email"] == pytest.ngo_admin_username


def test_admin_returns_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_profile(user_token=pytest.admin_token)

    assert PROFILE_SCHEMA.validate(response)
    assert response["email"] == pytest.admin_username
