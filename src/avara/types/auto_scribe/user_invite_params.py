# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserInviteParams"]


class UserInviteParams(TypedDict, total=False):
    can_create_reports: Required[Annotated[bool, PropertyInfo(alias="canCreateReports")]]

    can_manage_studies: Required[Annotated[bool, PropertyInfo(alias="canManageStudies")]]

    clinic_role: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="clinicRole"),
        ]
    ]
    """User's clinical or organizational role"""

    email: Required[str]
    """User's email address for login and notifications"""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """User's first name"""

    has_dashboard_access: Required[Annotated[bool, PropertyInfo(alias="hasDashboardAccess")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """User's last name"""

    level: Required[Literal["admin", "member"]]

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
    """User's middle name (optional)"""

    npi_number: Annotated[str, PropertyInfo(alias="npiNumber")]

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """User's phone number (10-15 digits, optional)"""

    suffix1: str
    """Name suffix (e.g., 'Jr.', 'Sr.', 'III') - optional"""

    suffix2: str
    """Additional name suffix (optional)"""
