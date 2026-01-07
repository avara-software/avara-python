# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InvitationRetrieveResponse"]


class InvitationRetrieveResponse(BaseModel):
    """A pending user invitation in the AutoScribe system"""

    can_create_reports: bool = FieldInfo(alias="canCreateReports")
    """Whether the invited user can generate and sign radiology reports.

    Requires NPI number
    """

    can_manage_studies: bool = FieldInfo(alias="canManageStudies")
    """
    Whether the invited user will have permission to create, update, and manage
    studies
    """

    clinic_id: str = FieldInfo(alias="clinicId")

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

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email: str

    expiry: Optional[datetime] = None

    first_name: str = FieldInfo(alias="firstName")

    has_dashboard_access: bool = FieldInfo(alias="hasDashboardAccess")

    invitation_id: str = FieldInfo(alias="invitationId")

    invited_source: Literal["dashboard", "api"] = FieldInfo(alias="invitedSource")

    inviter_id: Optional[str] = FieldInfo(alias="inviterId", default=None)

    last_name: str = FieldInfo(alias="lastName")

    level: Literal["owner", "admin", "member"]

    status: Literal["sent", "accepted", "rejected", "revoked"]

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    invited_by_api_key_id: Optional[str] = FieldInfo(alias="invitedByApiKeyId", default=None)

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)

    npi_number: Optional[str] = FieldInfo(alias="npiNumber", default=None)
    """
    National Provider Identifier - required for users who can create reports
    (10-digit number)
    """

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    suffix1: Optional[str] = None

    suffix2: Optional[str] = None
