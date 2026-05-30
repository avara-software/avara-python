# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StudyReportMetadata", "Height", "Weight"]


class Height(BaseModel):
    """
    Patient's height with unit (e.g., {value: 70, unit: 'inches'} or {value: 178, unit: 'cm'})
    """

    unit: Literal["in", "cm"]

    value: float


class Weight(BaseModel):
    """
    Patient's weight with unit (e.g., {value: 150, unit: 'lbs'} or {value: 68, unit: 'kg'})
    """

    unit: Literal["lbs", "kg"]

    value: float


class StudyReportMetadata(BaseModel):
    """Patient demographics and scan information for report generation"""

    age: Optional[str] = None
    """Patient's age at study date (e.g., '34.5 years', '2 months')"""

    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)
    """Patient's date of birth. Format: YYYY-MM-DD (e.g., '1990-05-20')"""

    facility_name: Optional[str] = FieldInfo(alias="facilityName", default=None)
    """Name of the medical facility where the scan was performed"""

    height: Optional[Height] = None
    """
    Patient's height with unit (e.g., {value: 70, unit: 'inches'} or {value: 178,
    unit: 'cm'})
    """

    mrn: Optional[str] = None
    """Medical Record Number - unique patient identifier"""

    patient_name: Optional[str] = FieldInfo(alias="patientName", default=None)
    """Full name of the patient"""

    procedure: Optional[str] = None
    """Procedure or study type (e.g., 'MRI Brain with Contrast').

    Maps to database scan_type and dictation report_header.scan_type.
    """

    referring_physician_name: Optional[str] = FieldInfo(alias="referringPhysicianName", default=None)
    """Name of the physician who referred the patient for this scan"""

    sex: Optional[Literal["male", "female", "other"]] = None
    """Patient's biological sex. Options: 'male', 'female', 'other'"""

    study_date: Optional[str] = FieldInfo(alias="studyDate", default=None)
    """Study date (YYYY-MM-DD).

    Maps to database scan_date and dictation report_header.scan_date.
    """

    study_time: Optional[str] = FieldInfo(alias="studyTime", default=None)
    """Study time (HH:MM).

    Maps to database scan_time and dictation report_header.scan_time.
    """

    weight: Optional[Weight] = None
    """
    Patient's weight with unit (e.g., {value: 150, unit: 'lbs'} or {value: 68, unit:
    'kg'})
    """
