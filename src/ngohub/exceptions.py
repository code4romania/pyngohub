class HubError(Exception):
    """The base exception for all Hub issues"""

    pass


class OrganizationError(HubError):
    """The base exception for all Hub Organization issues"""

    pass


class ClosedOrganizationRegistrationError(OrganizationError):
    """New organizations cannot be registered anymore"""

    pass


class DisabledOrganizationError(OrganizationError):
    """The requested organization has been disabled from the platform"""

    pass


class DuplicateOrganizationError(OrganizationError):
    """An organization with the same NGO Hub ID already exists"""

    pass


class MissingOrganizationError(OrganizationError):
    """The requested organization does not exist"""

    pass


class UserError(HubError):
    """The base exception for all Hub User issues"""

    pass


class MissingUserError(UserError):
    """The requested user does not exist"""

    pass


class HubHTTPError(HubError):
    """The base exception for all Hub HTTP/network issues"""

    def __init__(self, message: str, status_code: int, path: str, reason: str):
        self.message = message
        self.status_code = status_code
        self.path = path
        self.reason = reason

        super().__init__(message)


class HubBadRequestError(HubHTTPError):
    """The request was malformed"""

    def __init__(self, message: str, path: str):
        super().__init__(message, 400, path, "Bad request")


class HubDecodeError(HubHTTPError):
    """Failed to decode response"""

    def __init__(self, message: str):
        super().__init__(message, 500, "", "Internal server error")
