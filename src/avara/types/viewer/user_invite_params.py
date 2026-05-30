# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.clinic_role import ClinicRole
from ..shared.assignable_user_level import AssignableUserLevel

__all__ = ["UserInviteParams"]


class UserInviteParams(TypedDict, total=False):
    can_manage_studies: Required[Annotated[bool, PropertyInfo(alias="canManageStudies")]]

    clinic_role: Required[Annotated[ClinicRole, PropertyInfo(alias="clinicRole")]]
    """A user's clinical or organizational role within the clinic."""

    email: Required[str]
    """User's email address for login and notifications"""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """User's first name"""

    has_dashboard_access: Required[Annotated[bool, PropertyInfo(alias="hasDashboardAccess")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """User's last name"""

    level: Required[AssignableUserLevel]
    """User access level assignable via the API.

    'admin' can manage users/settings, 'member' has standard access. 'owner' is
    dashboard-only and cannot be assigned via the API.
    """

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """User's middle name (optional)"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """User's phone number (10-15 digits, optional)"""

    suffix1: str
    """Name suffix (e.g., 'Jr.', 'Sr.', 'III') - optional"""

    suffix2: str
    """Additional name suffix (optional)"""
