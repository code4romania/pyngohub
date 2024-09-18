from typing import Any, Dict, List

from ngohub.normalization.helpers import convert_date, extract_key


def _normalize_organization_general(org_general_data: Dict) -> Dict:
    normal_data: Dict = {
        "id": extract_key(org_general_data, "id"),
        "created_on": convert_date(extract_key(org_general_data, "createdOn")),
        "updated_on": convert_date(extract_key(org_general_data, "updatedOn")),
        "name": extract_key(org_general_data, "name"),
        "alias": extract_key(org_general_data, "alias"),
        "type": extract_key(org_general_data, "type"),
        "email": extract_key(org_general_data, "email"),
        "phone": extract_key(org_general_data, "phone"),
        "year_created": extract_key(org_general_data, "yearCreated"),
        "cui": extract_key(org_general_data, "cui"),
        "association_registry_number": extract_key(org_general_data, "associationRegistryNumber"),
        "association_registry_part": extract_key(org_general_data, "associationRegistryPart"),
        "association_registry_section": extract_key(org_general_data, "associationRegistrySection"),
        "association_registry_issuer_id": extract_key(org_general_data, "associationRegistryIssuerId"),
        "national_registry_number": extract_key(org_general_data, "nationalRegistryNumber"),
        "raf_number": extract_key(org_general_data, "rafNumber"),
        "short_description": extract_key(org_general_data, "shortDescription"),
        "description": extract_key(org_general_data, "description"),
        "address": extract_key(org_general_data, "address"),
        "logo": extract_key(org_general_data, "logo"),
        "website": extract_key(org_general_data, "website"),
        "facebook": extract_key(org_general_data, "facebook"),
        "instagram": extract_key(org_general_data, "instagram"),
        "twitter": extract_key(org_general_data, "twitter"),
        "linkedin": extract_key(org_general_data, "linkedin"),
        "tiktok": extract_key(org_general_data, "tiktok"),
        "donation_website": extract_key(org_general_data, "donationWebsite"),
        "redirect_link": extract_key(org_general_data, "redirectLink"),
        "donation_sms": extract_key(org_general_data, "donationSMS"),
        "donation_keyword": extract_key(org_general_data, "donationKeyword"),
        "contact": {
            "email": extract_key(extract_key(org_general_data, "contact"), "email"),
            "phone": extract_key(extract_key(org_general_data, "contact"), "phone"),
            "full_name": extract_key(extract_key(org_general_data, "contact"), "fullName"),
        },
        "organization_address": extract_key(org_general_data, "organizationAddress"),
        "city": {
            "id": extract_key(extract_key(org_general_data, "city"), "id"),
            "name": extract_key(extract_key(org_general_data, "city"), "name"),
            "county_id": extract_key(extract_key(org_general_data, "city"), "countyId"),
            "created_on": convert_date(extract_key(extract_key(org_general_data, "city"), "createdOn")),
        },
        "county": {
            "id": extract_key(extract_key(org_general_data, "county"), "id"),
            "name": extract_key(extract_key(org_general_data, "county"), "name"),
            "abbreviation": extract_key(extract_key(org_general_data, "county"), "abbreviation"),
            "region_id": extract_key(extract_key(org_general_data, "county"), "regionId"),
            "created_on": convert_date(extract_key(extract_key(org_general_data, "county"), "createdOn")),
        },
        "organization_city": extract_key(org_general_data, "organizationCity"),
        "organization_county": extract_key(org_general_data, "organizationCounty"),
        "association_registry_issuer": extract_key(org_general_data, "associationRegistryIssuer"),
    }

    return normal_data


def _normalize_organization_activity(org_activity_data: Dict) -> Dict:
    org_domains: List[Dict[str, Any]] = []
    for domain in extract_key(org_activity_data, "domains"):
        org_domains.append(
            {
                "id": extract_key(domain, "id"),
                "name": extract_key(domain, "name"),
                "created_on": convert_date(extract_key(domain, "createdOn")),
                "updated_on": convert_date(extract_key(domain, "updatedOn")),
            }
        )

    is_public_interest_org = extract_key(
        org_activity_data,
        "isPublicIntrestOrganization",
        "isPublicInterestOrganization",
    )
    normal_data: Dict = {
        "id": extract_key(org_activity_data, "id"),
        "created_on": convert_date(extract_key(org_activity_data, "createdOn")),
        "updated_on": convert_date(extract_key(org_activity_data, "updatedOn")),
        "area": extract_key(org_activity_data, "area"),
        "is_part_of_federation": extract_key(org_activity_data, "isPartOfFederation"),
        "is_part_of_coalition": extract_key(org_activity_data, "isPartOfCoalition"),
        "is_part_of_international_organization": extract_key(org_activity_data, "isPartOfInternationalOrganization"),
        "international_organization_name": extract_key(org_activity_data, "internationalOrganizationName"),
        "is_social_service_viable": extract_key(org_activity_data, "isSocialServiceViable"),
        "offers_grants": extract_key(org_activity_data, "offersGrants"),
        "is_public_interest_organization": is_public_interest_org,
        "has_branches": extract_key(org_activity_data, "hasBranches"),
        "federations": extract_key(org_activity_data, "federations"),
        "coalitions": extract_key(org_activity_data, "coalitions"),
        "domains": org_domains,
        "cities": extract_key(org_activity_data, "cities"),
        "branches": extract_key(org_activity_data, "branches"),
        "regions": extract_key(org_activity_data, "regions"),
    }
    return normal_data


def _normalize_organization_legal(org_legal_data: Dict) -> Dict:
    org_directors: List[Dict[str, Any]] = []
    for director in extract_key(org_legal_data, "directors"):
        org_directors.append(
            {
                "id": extract_key(director, "id"),
                "created_on": convert_date(extract_key(director, "createdOn")),
                "updated_on": convert_date(extract_key(director, "updatedOn")),
                "full_name": extract_key(director, "fullName"),
                "email": extract_key(director, "email"),
                "phone": extract_key(director, "phone"),
                "role": extract_key(director, "role"),
            }
        )

    normal_data: Dict = {
        "id": extract_key(org_legal_data, "id"),
        "created_on": convert_date(extract_key(org_legal_data, "createdOn")),
        "updated_on": convert_date(extract_key(org_legal_data, "updatedOn")),
        "others": extract_key(org_legal_data, "others"),
        "organization_statute": extract_key(org_legal_data, "organizationStatute"),
        "non_political_affiliation_file": extract_key(org_legal_data, "nonPoliticalAffiliationFile"),
        "balance_sheet_file": extract_key(org_legal_data, "balanceSheetFile"),
        "legal_reprezentative": {
            "id": extract_key(extract_key(org_legal_data, "legalReprezentative"), "id"),
            "created_on": convert_date(extract_key(extract_key(org_legal_data, "legalReprezentative"), "createdOn")),
            "updated_on": convert_date(extract_key(extract_key(org_legal_data, "legalReprezentative"), "updatedOn")),
            "full_name": extract_key(extract_key(org_legal_data, "legalReprezentative"), "fullName"),
            "email": extract_key(extract_key(org_legal_data, "legalReprezentative"), "email"),
            "phone": extract_key(extract_key(org_legal_data, "legalReprezentative"), "phone"),
            "role": extract_key(extract_key(org_legal_data, "legalReprezentative"), "role"),
        },
        "directors": org_directors,
    }

    return normal_data


def _normalize_organization_financial(org_financial_data: Dict) -> Dict:
    synced_anaf = extract_key(org_financial_data, "synched_anaf", "synced_anaf", "syncedAnaf")
    normal_data: Dict = {
        "id": extract_key(org_financial_data, "id"),
        "created_on": extract_key(org_financial_data, "createdOn"),
        "updated_on": extract_key(org_financial_data, "updatedOn"),
        "type": extract_key(org_financial_data, "type"),
        "number_of_employees": extract_key(org_financial_data, "numberOfEmployees"),
        "year": extract_key(org_financial_data, "year"),
        "total": extract_key(org_financial_data, "total"),
        "status": extract_key(org_financial_data, "status"),
        "report_status": extract_key(org_financial_data, "reportStatus"),
        "synced_anaf": synced_anaf,
        "data": extract_key(org_financial_data, "data"),
    }

    return normal_data


def _normalize_organization_report(org_report_data: Dict) -> Dict:
    org_reports: List[Dict[str, Any]] = []
    org_partners: List[Dict[str, Any]] = []
    org_investors: List[Dict[str, Any]] = []

    for report in extract_key(org_report_data, "reports"):
        org_reports.append(
            {
                "id": extract_key(report, "id"),
                "created_on": convert_date(extract_key(report, "createdOn")),
                "updated_on": convert_date(extract_key(report, "updatedOn")),
                "report": extract_key(report, "report"),
                "numberOfVolunteers": extract_key(report, "numberOfVolunteers"),
                "numberOfContractors": extract_key(report, "numberOfContractors"),
                "year": extract_key(report, "year"),
                "status": extract_key(report, "status"),
            }
        )

    for partner in extract_key(org_report_data, "partners"):
        org_partners.append(
            {
                "id": extract_key(partner, "id"),
                "created_on": convert_date(extract_key(partner, "createdOn")),
                "updated_on": convert_date(extract_key(partner, "updatedOn")),
                "year": extract_key(partner, "year"),
                "number_of_partners": extract_key(partner, "numberOfPartners"),
                "status": extract_key(partner, "status"),
                "path": extract_key(partner, "path"),
            }
        )

    for investor in extract_key(org_report_data, "investors"):
        org_investors.append(
            {
                "id": extract_key(investor, "id"),
                "created_on": convert_date(extract_key(investor, "createdOn")),
                "updated_on": convert_date(extract_key(investor, "updatedOn")),
                "year": extract_key(investor, "year"),
                "number_of_investors": extract_key(investor, "numberOfInvestors"),
                "status": extract_key(investor, "status"),
                "path": extract_key(investor, "path"),
            }
        )

    normal_data: Dict = {
        "id": extract_key(org_report_data, "id"),
        "created_on": extract_key(org_report_data, "createdOn"),
        "updated_on": extract_key(org_report_data, "updatedOn"),
        "reports": org_reports,
        "partners": org_partners,
        "investors": org_investors,
    }

    return normal_data


def normalize_organization_data(org_data: Dict) -> Dict:
    general = _normalize_organization_general(extract_key(org_data, "organizationGeneral"))
    activity = _normalize_organization_activity(extract_key(org_data, "organizationActivity"))
    legal = _normalize_organization_legal(extract_key(org_data, "organizationLegal"))
    financial = _normalize_organization_financial(extract_key(org_data, "organizationFinancial"))
    report = _normalize_organization_report(extract_key(org_data, "organizationReport"))

    normal_data: Dict = {
        "id": extract_key(org_data, "id"),
        "created_on": convert_date(extract_key(org_data, "createdOn")),
        "updated_on": convert_date(extract_key(org_data, "updatedOn")),
        "status": extract_key(org_data, "status"),
        "general": general,
        "activity": activity,
        "legal": legal,
        "financial": financial,
        "report": report,
    }

    return normal_data
