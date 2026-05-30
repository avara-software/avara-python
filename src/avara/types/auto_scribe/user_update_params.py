# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.clinic_role import ClinicRole
from ..shared.assignable_user_level import AssignableUserLevel

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    can_create_reports: Annotated[bool, PropertyInfo(alias="canCreateReports")]

    can_manage_studies: Annotated[bool, PropertyInfo(alias="canManageStudies")]

    clinic_role: Annotated[Optional[ClinicRole], PropertyInfo(alias="clinicRole")]
    """A user's clinical or organizational role within the clinic."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """User's first name"""

    has_dashboard_access: Annotated[bool, PropertyInfo(alias="hasDashboardAccess")]
    """Whether the user can access the dashboard interface. Required for admin users"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """User's last name"""

    level: AssignableUserLevel
    """User access level assignable via the API.

    'admin' can manage users/settings, 'member' has standard access. 'owner' is
    dashboard-only and cannot be assigned via the API.
    """

    middle_name: Annotated[Optional[str], PropertyInfo(alias="middleName")]

    npi_number: Annotated[Optional[str], PropertyInfo(alias="npiNumber")]

    phone_number: Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]

    suffix1: Optional[str]

    suffix2: Optional[str]
