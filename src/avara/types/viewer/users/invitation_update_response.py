# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InvitationUpdateResponse"]


class InvitationUpdateResponse(BaseModel):
    """A pending user invitation in the Viewer system"""

    can_manage_studies: bool = FieldInfo(alias="canManageStudies")
    """Whether the invited user will have permission to manage studies"""

    clinic_id: str = FieldInfo(alias="clinicId")
    """UUID of the clinic this invitation belongs to"""

    clinic_role: Literal[
        "Radiologist",
        "Cardiologist",
        "Neurologist",
        "Urologist",
        "Gynecologist",
        "Endocrinologist",
        "Doctor",
        "Surgeon",
        "Physician",
        "Physician Assistant",
        "Nurse Practitioner",
        "Registered Nurse",
        "Patient Care Coordinator",
        "Front Desk Operator",
        "Imaging Technologist",
        "PACS Administrator",
        "Software Engineer",
        "Revenue Cycle Manager",
        "Administrative Director",
        "Administrative Assistant",
        "Other",
    ] = FieldInfo(alias="clinicRole")
    """Clinical or organizational role for the invited user"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the invitation was created"""

    email: str
    """Email address the invitation was sent to"""

    expiry: Optional[datetime] = None
    """When the invitation expires, null if no expiration"""

    first_name: str = FieldInfo(alias="firstName")
    """Invited user's first name"""

    has_dashboard_access: bool = FieldInfo(alias="hasDashboardAccess")
    """Whether the invited user will have dashboard access"""

    invitation_id: str = FieldInfo(alias="invitationId")
    """Unique invitation identifier. Format: inv\\__{32-hex-chars}"""

    invited_source: Literal["dashboard", "api"] = FieldInfo(alias="invitedSource")
    """How the invitation was created - 'dashboard' or 'api'"""

    inviter_id: str = FieldInfo(alias="inviterId")
    """User ID of the person who sent the invitation.

    Format: usr\\__{32-hex-chars}. Null if invited via API
    """

    last_name: str = FieldInfo(alias="lastName")
    """Invited user's last name"""

    level: Literal["owner", "admin", "member"]
    """Access level for the invited user. 'admin' or 'member' when created via API"""

    status: Literal["sent", "accepted", "rejected", "revoked"]
    """Invitation status: 'sent', 'accepted', 'rejected', or 'revoked'"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the invitation was last updated"""

    user_id: str = FieldInfo(alias="userId")
    """User ID if this invitation has been accepted and linked to a user account.

    Null while pending
    """

    invited_by_api_key_id: Optional[str] = FieldInfo(alias="invitedByApiKeyId", default=None)
    """UUID of the API key used to send this invitation. Null if sent via dashboard"""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """Invited user's middle name (optional)"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Invited user's phone number (optional)"""

    suffix1: Optional[str] = None
    """Name suffix (e.g., 'Jr.', 'MD') - optional"""

    suffix2: Optional[str] = None
    """Additional name suffix - optional"""
