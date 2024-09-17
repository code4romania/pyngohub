import os

import pytest
from dotenv import find_dotenv, load_dotenv
from pycognito import Cognito


def pytest_configure():
    if not os.environ.get("SKIP_TEST_ENV_FILE"):
        load_dotenv(find_dotenv(filename=".env.test"))

    pytest.ngohub_api_url = os.environ["NGO_HUB_API_URL"]

    pytest.app_login_link = os.environ["APP_LOGIN_LINK"]

    pytest.ngo_id = os.environ["NGO_ID"]
    pytest.ngo_admin_id = os.environ["NGO_ADMIN_ID"]
    pytest.ngo_user_id = os.environ["NGO_USER_ID"]
    pytest.ngo_user_id_no_app = os.environ["NGO_USER_ID_NO_APP"]

    pytest.ngo_other_id = os.environ["NGO_OTHER_ID"]
    pytest.ngo_other_admin_id = os.environ["NGO_OTHER_ADMIN_ID"]
    pytest.ngo_other_user_id = os.environ["NGO_OTHER_USER_ID"]

    pytest.admin_username = os.environ["NGOHUB_API_ACCOUNT"]
    pytest.ngo_admin_username = os.environ["NGOHUB_NGO_ACCOUNT"]

    pytest.admin_token = _authenticate_with_ngohub(
        user_pool_id=os.environ["AWS_COGNITO_USER_POOL_ID"],
        client_id=os.environ["AWS_COGNITO_CLIENT_ID"],
        client_secret=os.environ["AWS_COGNITO_CLIENT_SECRET"],
        user_pool_region=os.environ["AWS_COGNITO_REGION"],
        username=os.environ["NGOHUB_API_ACCOUNT"],
        api_key=os.environ["NGOHUB_API_KEY"],
    )

    pytest.ngo_admin_token = _authenticate_with_ngohub(
        user_pool_id=os.environ["AWS_COGNITO_USER_POOL_ID"],
        client_id=os.environ["AWS_COGNITO_CLIENT_ID"],
        client_secret=os.environ["AWS_COGNITO_CLIENT_SECRET"],
        user_pool_region=os.environ["AWS_COGNITO_REGION"],
        username=os.environ["NGOHUB_NGO_ACCOUNT"],
        api_key=os.environ["NGOHUB_NGO_KEY"],
    )


def _authenticate_with_ngohub(
    user_pool_id: str,
    client_id: str,
    client_secret: str,
    user_pool_region: str,
    username: str,
    api_key: str,
) -> str:
    u = Cognito(
        user_pool_id=user_pool_id,
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        user_pool_region=user_pool_region,
    )
    u.authenticate(password=api_key)

    return u.access_token


class FakeHTTPSConnection:
    def __init__(self, status):
        self.status = status

    def request(self, *args, **kwargs):
        pass

    def getresponse(self):
        return FakeHTTPResponse(self.status)


class FakeHTTPResponse:
    def __init__(self, status):
        self.status = status

    @staticmethod
    def read():
        return b"OK"
