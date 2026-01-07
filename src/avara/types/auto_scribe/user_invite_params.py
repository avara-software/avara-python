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

    email: Required[str]

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    has_dashboard_access: Required[Annotated[bool, PropertyInfo(alias="hasDashboardAccess")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]

    level: Required[Literal["admin", "member"]]

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]

    npi_number: Annotated[str, PropertyInfo(alias="npiNumber")]

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]

    suffix1: str

    suffix2: str
