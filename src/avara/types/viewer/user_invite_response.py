# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserInviteResponse"]


class UserInviteResponse(BaseModel):
    """A user in the Viewer system with study management permissions"""

    can_manage_studies: bool = FieldInfo(alias="canManageStudies")

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

    first_name: str = FieldInfo(alias="firstName")

    has_dashboard_access: bool = FieldInfo(alias="hasDashboardAccess")

    invited_source: Literal["dashboard", "api"] = FieldInfo(alias="invitedSource")

    last_login_at: Optional[datetime] = FieldInfo(alias="lastLoginAt", default=None)

    last_name: str = FieldInfo(alias="lastName")

    level: Literal["owner", "admin", "member"]

    user_id: str = FieldInfo(alias="userId")

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    suffix1: Optional[str] = None

    suffix2: Optional[str] = None
