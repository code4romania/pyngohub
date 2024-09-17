from schema import Or, Regex, Schema

VERSION_REVISION_SCHEMA = Schema(
    {
        "version": Regex(r"\d+\.\d+\.\d+"),
        "revision": Regex(r"[0-9a-f]{40}"),
    }
)

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

ORGANIZATION_SCHEMA = ORGANIZATION_PROFILE_SCHEMA = Schema(
    {
        "id": int,
        "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        "status": str,
        "organizationGeneral": {
            "id": int,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "name": str,
            "alias": str,
            "type": str,
            "email": str,
            "phone": str,
            "yearCreated": int,
            "cui": str,
            "associationRegistryNumber": None,
            "associationRegistryPart": None,
            "associationRegistrySection": None,
            "associationRegistryIssuerId": None,
            "nationalRegistryNumber": None,
            "rafNumber": str,
            "shortDescription": str,
            "description": str,
            "address": str,
            "logo": str,
            "website": str,
            "facebook": str,
            "instagram": str,
            "twitter": str,
            "linkedin": str,
            "tiktok": str,
            "donationWebsite": str,
            "redirectLink": str,
            "donationSMS": str,
            "donationKeyword": str,
            "contact": {
                "email": str,
                "phone": str,
                "fullName": str,
            },
            "organizationAddress": None,
            "city": {
                "id": int,
                "name": str,
                "countyId": int,
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            },
            "county": {
                "id": int,
                "name": str,
                "abbreviation": str,
                "regionId": int,
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            },
            "organizationCity": None,
            "organizationCounty": None,
            "associationRegistryIssuer": None,
        },
        "organizationActivity": {
            "id": int,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "area": str,
            "isPartOfFederation": bool,
            "isPartOfCoalition": bool,
            "isPartOfInternationalOrganization": bool,
            "internationalOrganizationName": None,
            "isSocialServiceViable": bool,
            "offersGrants": bool,
            "isPublicIntrestOrganization": bool,
            "hasBranches": bool,
            "federations": [],
            "coalitions": [],
            "domains": [
                {
                    "id": int,
                    "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "name": str,
                }
            ],
            "cities": [],
            "branches": [],
            "regions": [],
        },
        "organizationLegal": {
            "id": int,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "others": None,
            "organizationStatute": str,
            "nonPoliticalAffiliationFile": str,
            "balanceSheetFile": str,
            "legalReprezentative": {
                "id": int,
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "fullName": str,
                "email": str,
                "phone": str,
                "role": str,
            },
            "directors": [
                {
                    "id": int,
                    "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "fullName": str,
                    "email": str,
                    "phone": Or(None, str),  # noqa
                    "role": Or(None, str),  # noqa
                }
            ],
        },
        "organizationFinancial": [
            {
                "id": int,
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "type": str,
                "numberOfEmployees": Or(None, int),  # noqa2
                "year": int,
                "total": Or(None, int),  # noqa
                "status": str,
                "reportStatus": str,
                "synched_anaf": bool,
                "data": Or(None, str),  # noqa
            }
        ],
        "organizationReport": {
            "id": int,
            "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
            "reports": [
                {
                    "id": int,
                    "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "report": None,
                    "numberOfVolunteers": int,
                    "numberOfContractors": int,
                    "year": int,
                    "status": str,
                }
            ],
            "partners": [
                {
                    "id": int,
                    "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "year": int,
                    "numberOfPartners": int,
                    "status": str,
                    "path": None,
                }
            ],
            "investors": [
                {
                    "id": int,
                    "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                    "year": int,
                    "numberOfInvestors": int,
                    "status": str,
                    "path": None,
                }
            ],
        },
    }
)

APPLICATION_LIST_SCHEMA = Schema(
    [
        {
            "id": int,
            "name": str,
        }
    ]
)

ORGANIZATION_APPLICATIONS_SCHEMA = Schema(
    [
        {
            "id": int,
            "logo": Or(None, str),  # noqa
            "name": str,
            "shortDescription": str,
            "loginLink": str,
            "website": str,
            "status": str,
            "ongStatus": Or(None, str),  # noqa
            "createdOn": Or(None, Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z")),  # noqa
            "type": str,
            "applicationLabel": Or(None, str),  # noqa
        }
    ]
)

ORGANIZATION_USERS_SCHEMA = Schema(
    {
        "items": [
            {
                "id": int,
                "name": str,
                "email": str,
                "phone": str,
                "status": Or("active", "restricted", "pending"),
                "availableApps": [
                    {
                        "id": int,
                        "name": str,
                        "type": Or("independent", "simple", "standalone"),
                    },
                ],
                "availableAppsIDs": [int],
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "organizationId": int,
                "organizationAlias": str,
            },
        ],
        "meta": {
            "itemCount": int,
            "totalItems": int,
            "itemsPerPage": int,
            "totalPages": int,
            "currentPage": int,
        },
    }
)


PROFILE_SCHEMA = Schema(
    {
        "id": int,
        "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
        "cognitoId": str,
        "name": str,
        "email": str,
        "phone": str,
        "role": str,
        "status": str,
        "organization": Or(
            None,
            {
                "id": int,
                "createdOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "updatedOn": Regex(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z"),
                "status": str,
            },
        ),
    }
)
