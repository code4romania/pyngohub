import pytest

from ngohub.nomenclatures import (
    get_beneficiaries_nomenclatures,
    get_cities_nomenclatures,
    get_coalitions_nomenclatures,
    get_counties_nomenclatures,
    get_domains_nomenclatures,
    get_faculties_nomenclatures,
    get_federations_nomenclatures,
    get_issuers_nomenclatures,
    get_practice_domains_nomenclatures,
    get_regions_nomenclatures,
    get_service_domains_nomenclatures,
    get_skills_nomenclatures,
)
from tests.schemas import (
    NOMENCLATURE_BENEFIARIES_SCHEMA,
    NOMENCLATURE_CITIES_SCHEMA,
    NOMENCLATURE_COALITIONS_SCHEMA,
    NOMENCLATURE_COUNTIES_SCHEMA,
    NOMENCLATURE_DOMAINS_SCHEMA,
    NOMENCLATURE_FACULTIES_SCHEMA,
    NOMENCLATURE_FEDERATIONS_SCHEMA,
    NOMENCLATURE_ISSUERS_SCHEMA,
    NOMENCLATURE_PRACTICE_DOMAINS_SCHEMA,
    NOMENCLATURE_REGIONS_SCHEMA,
    NOMENCLATURE_SERVICE_DOMAINS_SCHEMA,
    NOMENCLATURE_SKILLS_SCHEMA,
)


def test_cities_nomenclatures_errors_if_no_params():
    with pytest.raises(ValueError):
        get_cities_nomenclatures()


def test_cities_nomenclatures_returns_empty_response():
    response = get_cities_nomenclatures(search="UNKNOWN")

    assert response == []


def test_cities_nomenclatures_schema():
    response = get_cities_nomenclatures(county_id=1, city_id=1)

    assert len(response) == 1
    assert NOMENCLATURE_CITIES_SCHEMA.validate(response)


def test_counties_nomenclatures_schema():
    response = get_counties_nomenclatures()

    assert NOMENCLATURE_COUNTIES_SCHEMA.validate(response)


def test_domains_nomenclatures_schema():
    response = get_domains_nomenclatures()

    assert NOMENCLATURE_DOMAINS_SCHEMA.validate(response)


def test_regions_nomenclatures_schema():
    response = get_regions_nomenclatures()

    assert NOMENCLATURE_REGIONS_SCHEMA.validate(response)


def test_federations_nomenclatures_schema():
    response = get_federations_nomenclatures()

    assert NOMENCLATURE_FEDERATIONS_SCHEMA.validate(response)


def test_coalitions_nomenclatures_schema():
    response = get_coalitions_nomenclatures()

    assert NOMENCLATURE_COALITIONS_SCHEMA.validate(response)


def test_faculties_nomenclatures_schema():
    response = get_faculties_nomenclatures()

    assert NOMENCLATURE_FACULTIES_SCHEMA.validate(response)


def test_skills_nomenclatures_schema():
    response = get_skills_nomenclatures()

    assert NOMENCLATURE_SKILLS_SCHEMA.validate(response)


def test_practice_domains_nomenclatures_schema():
    response = get_practice_domains_nomenclatures()

    assert NOMENCLATURE_PRACTICE_DOMAINS_SCHEMA.validate(response)


def test_service_domains_nomenclatures_schema():
    response = get_service_domains_nomenclatures()

    assert NOMENCLATURE_SERVICE_DOMAINS_SCHEMA.validate(response)


def test_beneficiaries_nomenclatures_schema():
    response = get_beneficiaries_nomenclatures()

    assert NOMENCLATURE_BENEFIARIES_SCHEMA.validate(response)


def test_issuers_nomenclatures_schema():
    response = get_issuers_nomenclatures()

    assert NOMENCLATURE_ISSUERS_SCHEMA.validate(response)
