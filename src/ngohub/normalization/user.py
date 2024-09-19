from typing import Any, Dict

from ngohub.models.user import User


def normalize_user(user_data: Dict[str, Any]) -> User:
    normal_data = User(
        id=user_data["id"],
        created_on=user_data["createdOn"],
        updated_on=user_data["updatedOn"],
        cognito_id=user_data["cognitoId"],
        name=user_data["name"],
        email=user_data["email"],
        phone=user_data["phone"],
        role=user_data["role"],
        status=user_data["status"],
        organization_id=user_data["organizationId"],
    )

    return normal_data
