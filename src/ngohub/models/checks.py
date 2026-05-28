from dataclasses import dataclass

from ngohub.models.core import BaseDataclass
from ngohub.models.organization import OrganizationApplication
from ngohub.models.user import User


@dataclass
class CheckOrganizationUserApplication(BaseDataclass):
    user: User | None
    application: OrganizationApplication | None
    has_access: bool | None

    def __init__(self) -> None:
        self.user = None
        self.application = None
        self.has_access = None
