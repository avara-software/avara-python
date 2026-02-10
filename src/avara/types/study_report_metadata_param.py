# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StudyReportMetadataParam", "Height", "Weight"]


class Height(TypedDict, total=False):
    """
    Patient's height with unit (e.g., {value: 70, unit: 'inches'} or {value: 178, unit: 'cm'})
    """

    unit: Required[Literal["in", "cm"]]
    """Height unit"""

    value: Required[float]


class Weight(TypedDict, total=False):
    """
    Patient's weight with unit (e.g., {value: 150, unit: 'lbs'} or {value: 68, unit: 'kg'})
    """

    unit: Required[Literal["lbs", "kg"]]
    """Weight unit"""

    value: Required[float]


class StudyReportMetadataParam(TypedDict, total=False):
    """Patient demographics and scan information for report generation"""

    age: str
    """Patient's age at time of scan (e.g., '34.5 years', '2 months')"""

    date_of_birth: Annotated[str, PropertyInfo(alias="dateOfBirth")]
    """Patient's date of birth. Format: YYYY-MM-DD (e.g., '1990-05-20')"""

    facility_name: Annotated[str, PropertyInfo(alias="facilityName")]
    """Name of the medical facility where the scan was performed"""

    height: Height
    """
    Patient's height with unit (e.g., {value: 70, unit: 'inches'} or {value: 178,
    unit: 'cm'})
    """

    mrn: str
    """Medical Record Number - unique patient identifier"""

    patient_name: Annotated[str, PropertyInfo(alias="patientName")]
    """Full name of the patient"""

    referring_physician_name: Annotated[str, PropertyInfo(alias="referringPhysicianName")]
    """Name of the physician who referred the patient for this scan"""

    scan_date: Annotated[str, PropertyInfo(alias="scanDate")]
    """Date the scan was performed. Format: YYYY-MM-DD (e.g., '2024-01-15')"""

    scan_time: Annotated[str, PropertyInfo(alias="scanTime")]
    """Time the scan was performed. Format: HH:MM (e.g., '14:30')"""

    scan_type: Annotated[str, PropertyInfo(alias="scanType")]
    """Type of scan or imaging modality (e.g., 'MRI', 'CT', 'X-Ray', 'Ultrasound')"""

    sex: Literal["male", "female", "other"]
    """Patient's biological sex"""

    weight: Weight
    """
    Patient's weight with unit (e.g., {value: 150, unit: 'lbs'} or {value: 68, unit:
    'kg'})
    """
