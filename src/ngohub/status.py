from http.client import HTTPResponse
from typing import Dict

from ngohub.core import decode_raw_response, json_response, ngohub_api_get


def get_health() -> str:
    response: HTTPResponse = ngohub_api_get("/health/")

    return decode_raw_response(response)


def get_version() -> Dict:
    response: HTTPResponse = ngohub_api_get("/version/")

    return json_response(response)


def get_file_url(path: str) -> str:
    response: HTTPResponse = ngohub_api_get(f"/file?path={path}")

    return decode_raw_response(response)
