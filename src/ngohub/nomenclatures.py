from http.client import HTTPResponse
from typing import Any, Dict, List

from ngohub.core import json_response, ngohub_api_get


def get_nomenclature(nomenclature: str) -> Any:
    response: HTTPResponse = ngohub_api_get(f"/nomenclatures/{nomenclature}")

    return json_response(response)


def get_cities_nomenclatures(search: str = None, county_id: int = None, city_id: int = None) -> List[Dict[str, Any]]:
    mandatory_params: List[Any] = [search, county_id]
    if all(param is None for param in mandatory_params):
        raise ValueError("Please provide at least one of the following: county_id, search")

    search_query: List[str] = []
    if search:
        search_query.append(f"search={search}")
    if county_id:
        search_query.append(f"countyId={county_id}")
    if city_id:
        search_query.append(f"cityId={city_id}")

    return get_nomenclature(f"cities?{'&'.join(search_query)}")


def get_counties_nomenclatures() -> List[Dict[str, Any]]:
    return get_nomenclature("counties")


def get_domains_nomenclatures():
    return get_nomenclature("domains")


def get_regions_nomenclatures():
    return get_nomenclature("regions")


def get_federations_nomenclatures():
    return get_nomenclature("federations")


def get_coalitions_nomenclatures():
    return get_nomenclature("coalitions")


def get_faculties_nomenclatures():
    return get_nomenclature("faculties")


def get_skills_nomenclatures():
    return get_nomenclature("skills")


def get_practice_domains_nomenclatures():
    return get_nomenclature("practice-domains")


def get_service_domains_nomenclatures():
    return get_nomenclature("service-domains")


def get_beneficiaries_nomenclatures():
    return get_nomenclature("beneficiaries")


def get_issuers_nomenclatures():
    return get_nomenclature("issuers")
