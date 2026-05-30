# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.clinic_role import ClinicRole
from ..shared.invited_source import InvitedSource
from ..shared.assignable_user_level import AssignableUserLevel

__all__ = ["UserInviteResponse"]


class UserInviteResponse(BaseModel):
    """Response for inviting a user to Viewer.

    Level is restricted to admin/member since owners cannot be invited via API.
    """

    can_manage_studies: bool = FieldInfo(alias="canManageStudies")
    """Whether the user has permission to create, update, and manage studies"""

    clinic_role: ClinicRole = FieldInfo(alias="clinicRole")
    """A user's clinical or organizational role within the clinic."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the user was created"""

    email: str
    """User's email address for login and notifications"""

    first_name: str = FieldInfo(alias="firstName")
    """User's first name"""

    has_dashboard_access: bool = FieldInfo(alias="hasDashboardAccess")
    """Whether the user can access the dashboard interface. Required for admin users"""

    invited_source: InvitedSource = FieldInfo(alias="invitedSource")
    """
    How a user/invitation was created - via the dashboard UI ('dashboard') or the
    API ('api').
    """

    last_login_at: Optional[datetime] = FieldInfo(alias="lastLoginAt", default=None)
    """Timestamp of user's last login, null if never logged in"""

    last_name: str = FieldInfo(alias="lastName")
    """User's last name"""

    level: AssignableUserLevel
    """User access level assignable via the API.

    'admin' can manage users/settings, 'member' has standard access. 'owner' is
    dashboard-only and cannot be assigned via the API.
    """

    user_id: str = FieldInfo(alias="userId")
    """Unique user identifier. Format: usr\\__{32-hex-chars}"""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """User's middle name (optional)"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """User's phone number (10-15 digits, optional)"""

    suffix1: Optional[str] = None
    """Name suffix (e.g., 'Jr.', 'Sr.', 'III') - optional"""

    suffix2: Optional[str] = None
    """Additional name suffix (optional)"""
