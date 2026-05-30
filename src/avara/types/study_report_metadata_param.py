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

    value: Required[float]


class Weight(TypedDict, total=False):
    """
    Patient's weight with unit (e.g., {value: 150, unit: 'lbs'} or {value: 68, unit: 'kg'})
    """

    unit: Required[Literal["lbs", "kg"]]

    value: Required[float]


class StudyReportMetadataParam(TypedDict, total=False):
    """Patient demographics and scan information for report generation"""

    age: str
    """Patient's age at study date (e.g., '34.5 years', '2 months')"""

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

    procedure: str
    """Procedure or study type (e.g., 'MRI Brain with Contrast').

    Maps to database scan_type and dictation report_header.scan_type.
    """

    referring_physician_name: Annotated[str, PropertyInfo(alias="referringPhysicianName")]
    """Name of the physician who referred the patient for this scan"""

    sex: Literal["male", "female", "other"]
    """Patient's biological sex. Options: 'male', 'female', 'other'"""

    study_date: Annotated[str, PropertyInfo(alias="studyDate")]
    """Study date (YYYY-MM-DD).

    Maps to database scan_date and dictation report_header.scan_date.
    """

    study_time: Annotated[str, PropertyInfo(alias="studyTime")]
    """Study time (HH:MM).

    Maps to database scan_time and dictation report_header.scan_time.
    """

    weight: Weight
    """
    Patient's weight with unit (e.g., {value: 150, unit: 'lbs'} or {value: 68, unit:
    'kg'})
    """
