import http
import json
import logging
import os
import socket
import urllib.parse
from http.client import HTTPResponse, HTTPSConnection
from typing import Dict, Optional

from ngohub.exceptions import NGOHubDecodeException, NGOHubHTTPException

logger = logging.getLogger(__name__)

NGO_HUB_API_URL: str = os.environ.get("NGO_HUB_API_URL")


def decode_raw_response(response: HTTPResponse) -> str:
    try:
        string_response: str = response.read().decode("utf-8")
    except UnicodeDecodeError:
        raise NGOHubDecodeException(f"Failed to decode response: {response.read()}")

    return string_response


def json_response(response: HTTPResponse) -> Dict:
    string_response: str = decode_raw_response(response)

    try:
        dict_response = json.loads(string_response)
    except json.JSONDecodeError:
        raise NGOHubDecodeException(f"Failed to decode JSON response: {response.read()}")

    return dict_response


def ngohub_api_request(
    request_method: str,
    path: str,
    token: str,
    params: Optional[Dict],
) -> HTTPResponse:
    """
    Perform a request to the NGO Hub API and return a JSON response, or raise NGOHubHTTPException
    """
    if not NGO_HUB_API_URL:
        raise ValueError("Environment variable NGO_HUB_API_URL can't be empty")

    if not path.startswith("/"):
        path = f"/{path}"

    conn: HTTPSConnection = http.client.HTTPSConnection(NGO_HUB_API_URL)

    headers: Dict = {
        "Content-Type": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    encoded_params = None
    if params:
        encoded_params = urllib.parse.urlencode(params)

    try:
        conn.request(method=request_method, url=path, body=encoded_params, headers=headers)
    except socket.gaierror as e:
        raise NGOHubHTTPException(f"Failed to make request to '{path}': {e}")

    try:
        response: HTTPResponse = conn.getresponse()
    except ConnectionError as e:
        raise NGOHubHTTPException(f"Failed to get response from '{path}': {e}")

    if response.status != http.HTTPStatus.OK:
        logger.info(path)
        raise NGOHubHTTPException(f"{response.status} while retrieving '{path}'. Reason: {response.reason}")

    return response


def ngohub_api_get(path: str, token: str = None) -> HTTPResponse:
    return ngohub_api_request("GET", path, token, params=None)


def ngohub_api_post(path: str, params: Dict, token: str = None) -> HTTPResponse:
    return ngohub_api_request("POST", path, token, params)


def ngohub_api_patch(path: str, params: Dict, token: str = None) -> HTTPResponse:
    return ngohub_api_request("PATCH", path, token, params)


def ngohub_api_delete(path: str, token: str = None) -> HTTPResponse:
    return ngohub_api_request("DELETE", path, token, params=None)


class NGOHub:
    pass
