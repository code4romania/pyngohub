from schema import Regex, Schema

NOMENCLATURE_CITIES_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
            "countyId": int,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "county": {
                "id": int,
                "name": str,
                "abbreviation": str,
                "regionId": int,
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            },
        }
    ]
)

NOMENCLATURE_COUNTIES_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
            "abbreviation": str,
            "regionId": int,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        }
    ]
)

NOMENCLATURE_ISSUERS_SCHEMA = NOMENCLATURE_SKILLS_SCHEMA = NOMENCLATURE_FACULTIES_SCHEMA = (
    NOMENCLATURE_REGIONS_SCHEMA
) = NOMENCLATURE_DOMAINS_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        }
    ]
)

NOMENCLATURE_FEDERATIONS_SCHEMA = NOMENCLATURE_COALITIONS_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
            "abbreviation": str,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        }
    ]
)

NOMENCLATURE_PRACTICE_DOMAINS_SCHEMA = NOMENCLATURE_SERVICE_DOMAINS_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
            "group": str,
        }
    ]
)

NOMENCLATURE_BENEFIARIES_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
        }
    ]
)
