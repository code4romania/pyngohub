import pytest

from ngohub import NGOHub
from ngohub.exceptions import HubHTTPException
from ngohub.models.organization import OrganizationApplication
from tests.test_end_to_end.schemas import (
    APPLICATION_LIST_SCHEMA,
    ORGANIZATION_APPLICATIONS_SCHEMA,
    ORGANIZATION_PROFILE_SCHEMA,
    ORGANIZATION_SCHEMA,
)


def test_organization_profile():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_organization_profile(ngo_token=pytest.ngo_admin_token)

    assert ORGANIZATION_PROFILE_SCHEMA.validate(response)


def test_organization_profile_returns_401():
    hub = NGOHub(pytest.ngohub_api_url)

    with pytest.raises(HubHTTPException):
        hub.get_raw_organization_profile(ngo_token="invalid_token")


def test_organization():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_organization(admin_token=pytest.admin_token, organization_id=10)

    assert ORGANIZATION_SCHEMA.validate(response)


def test_application_list():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_application_list(admin_token=pytest.admin_token)

    assert APPLICATION_LIST_SCHEMA.validate(response)


def test_organization_applications():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.get_raw_organization_applications(admin_token=pytest.admin_token, organization_id=pytest.ngo_id)

    assert ORGANIZATION_APPLICATIONS_SCHEMA.validate(response)


def test_check_missing_organization_returns_empty():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_organization_user_has_application(
        admin_token=pytest.admin_token,
        organization_id=0,
        user_id=0,
        login_link=pytest.app_login_link,
    )

    assert response.user is None
    assert response.application is None
    assert response.has_access is None


def test_check_missing_user_returns_empty():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_organization_user_has_application(
        admin_token=pytest.admin_token,
        organization_id=pytest.ngo_id,
        user_id=0,
        login_link=pytest.app_login_link,
    )

    assert response.user is None
    assert response.application is not None
    assert response.has_access is None


def test_check_organization_wrong_admin_does_not_have_application():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_organization_user_has_application(
        admin_token=pytest.admin_token,
        organization_id=pytest.ngo_id,
        user_id=pytest.ngo_other_admin_id,
        login_link=pytest.app_login_link,
    )

    assert response.user is None
    assert response.application is not None
    assert response.has_access is None


def test_check_organization_admin_has_application():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_organization_user_has_application(
        admin_token=pytest.admin_token,
        organization_id=pytest.ngo_id,
        user_id=pytest.ngo_admin_id,
        login_link=pytest.app_login_link,
    )

    assert response.user is not None
    assert response.application is not None
    assert response.has_access is True


def test_check_organization_user_without_app_doesnt_have_application():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_organization_user_has_application(
        admin_token=pytest.admin_token,
        organization_id=pytest.ngo_id,
        user_id=pytest.ngo_user_id_no_app,
        login_link=pytest.app_login_link,
    )

    assert response.user is not None
    assert response.application is not None
    assert response.has_access is False


def test_check_organization_user_with_app_has_application():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_organization_user_has_application(
        admin_token=pytest.admin_token,
        organization_id=pytest.ngo_id,
        user_id=pytest.ngo_user_id,
        login_link=pytest.app_login_link,
    )

    assert response.user is not None
    assert response.application is not None
    assert response.has_access is True


def test_check_user_organization_doesnt_have_missing_application():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_user_organization_has_application(
        ngo_token=pytest.ngo_admin_token,
        login_link="https://random-a3qlpo8tqsyxa0utl.com",
    )

    assert response is None


def test_check_user_organization_has_application():
    hub = NGOHub(pytest.ngohub_api_url)
    response = hub.check_user_organization_has_application(
        ngo_token=pytest.ngo_admin_token,
        login_link=pytest.app_login_link,
    )

    assert isinstance(response, OrganizationApplication)
    assert response.login_link.startswith(pytest.app_login_link)
