# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    can_manage_studies: Annotated[bool, PropertyInfo(alias="canManageStudies")]

    clinic_role: Annotated[
        Optional[
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
            ]
        ],
        PropertyInfo(alias="clinicRole"),
    ]

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """User's first name"""

    has_dashboard_access: Annotated[bool, PropertyInfo(alias="hasDashboardAccess")]
    """Whether the user can access the dashboard interface. Required for admin users"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """User's last name"""

    level: Literal["admin", "member"]

    middle_name: Annotated[Optional[str], PropertyInfo(alias="middleName")]

    phone_number: Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]

    suffix1: Optional[str]

    suffix2: Optional[str]
