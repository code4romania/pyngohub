
import http
import json
import logging
import socket
import urllib.parse
from http.client import HTTPResponse, HTTPSConnection
from typing import Dict, Optional

from ngohub.exceptions import HubDecodeException, HubHTTPException


logger = logging.getLogger(__name__)


class HTTPClientResponse:
    """
    HTTP responses with some helper methods
    """

    def __init__(self, raw_response: HTTPResponse):
        self.raw_response: HTTPResponse = raw_response

    def to_str(self) -> str:
        try:
            string_response: str = self.raw_response.read().decode("utf-8")
        except UnicodeDecodeError:
            raise HubDecodeException(f"Failed to decode response: {self.raw_response.read()}")

        return string_response

    def to_dict(self) -> Dict:
        string_response: str = self.to_str()

        try:
            dict_response = json.loads(string_response)
        except json.JSONDecodeError:
            raise HubDecodeException(f"Failed to decode JSON response: {self.raw_response.read()}")

        return dict_response


class HTTPClient:
    """
    HTTP client for interacting with an HTTP API
    """
    
    def __init__(self, api_base_url: str, *, auth_type="Bearer", auth_header="Authorization"):
        self.api_base_url = api_base_url or ""
        self.auth_type = auth_type
        self.auth_header = auth_header

    def _api_request(
        self,
        request_method: str,
        path: str,
        token: str,
        params: Optional[Dict],
    ) -> HTTPClientResponse:
        """
        Perform a request to the NGO Hub API and return a JSON response, or raise HubHTTPException
        """
        if not self.api_base_url:
            raise ValueError("The API base URL cannot be empty")

        if not path.startswith("/"):
            path = f"/{path}"

        conn: HTTPSConnection = http.client.HTTPSConnection(self.api_base_url)

        headers: Dict = {
            "Content-Type": "application/json",
        }
        if token:
            headers[self.auth_header] = f"{self.auth_type} {token}"

        encoded_params = None
        if params:
            encoded_params = urllib.parse.urlencode(params)

        try:
            conn.request(method=request_method, url=path, body=encoded_params, headers=headers)
        except socket.gaierror as e:
            raise HubHTTPException(f"Failed to make request to '{path}': {e}")

        try:
            response: HTTPResponse = conn.getresponse()
        except ConnectionError as e:
            raise HubHTTPException(f"Failed to get response from '{path}': {e}")

        if response.status != http.HTTPStatus.OK:
            logger.info(path)
            raise HubHTTPException(f"{response.status} while retrieving '{path}'. Reason: {response.reason}")

        return HTTPClientResponse(response)


    def api_get(self, path: str, token: str = None) -> HTTPClientResponse:
        return self._api_request("GET", path, token, params=None)


    def api_post(self, path: str, params: Dict, token: str = None) -> HTTPClientResponse:
        return self._api_request("POST", path, token, params)


    def api_patch(self, path: str, params: Dict, token: str = None) -> HTTPClientResponse:
        return self._api_request("PATCH", path, token, params)


    def api_delete(self, path: str, token: str = None) -> HTTPClientResponse:
        return self._api_request("DELETE", path, token, params=None)

