import pytest

from ngohub import NGOHub
from ngohub.models.user import UserProfile
from tests.test_end_to_end.schemas import PROFILE_SCHEMA, USER_SCHEMA


def test_user_returns_raw_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_profile(user_token=pytest.ngo_admin_token)

    assert PROFILE_SCHEMA.validate(response)
    assert response["email"] == pytest.ngo_admin_username


def test_admin_returns_raw_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_profile(user_token=pytest.admin_token)

    assert PROFILE_SCHEMA.validate(response)
    assert response["email"] == pytest.admin_username


def test_user_returns_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_profile(user_token=pytest.ngo_admin_token)

    assert isinstance(response, UserProfile)
    assert response.email == pytest.ngo_admin_username
    assert response.role == "admin"
    assert response.organization is not None
    assert response.organization.id == pytest.ngo_id


def test_admin_returns_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_profile(user_token=pytest.admin_token)

    assert isinstance(response, UserProfile)
    assert response.email == pytest.admin_username
    assert response.role == "super-admin"
    assert response.organization is None


def test_get_user_returns_user():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_user_raw(admin_token=pytest.admin_token, user_id=pytest.ngo_admin_id)

    assert USER_SCHEMA.validate(response)
    assert response["email"] == pytest.ngo_admin_username
    assert response["id"] == pytest.ngo_admin_id
