# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StudyReportMetadataParam", "Height", "Weight"]


class Height(TypedDict, total=False):
    unit: Required[Literal["in", "cm"]]

    value: Required[float]


class Weight(TypedDict, total=False):
    unit: Required[Literal["lbs", "kg"]]

    value: Required[float]


class StudyReportMetadataParam(TypedDict, total=False):
    """Metadata for a study report including patient demographics and scan information"""

    age: str

    date_of_birth: Annotated[str, PropertyInfo(alias="dateOfBirth")]

    facility_name: Annotated[str, PropertyInfo(alias="facilityName")]

    height: Height

    mrn: str

    patient_name: Annotated[str, PropertyInfo(alias="patientName")]

    referring_physician_name: Annotated[str, PropertyInfo(alias="referringPhysicianName")]

    scan_date: Annotated[str, PropertyInfo(alias="scanDate")]

    scan_time: Annotated[str, PropertyInfo(alias="scanTime")]

    scan_type: Annotated[str, PropertyInfo(alias="scanType")]

    sex: Literal["male", "female", "other"]

    weight: Weight
