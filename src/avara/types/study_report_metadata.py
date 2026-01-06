# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StudyReportMetadata", "Height", "Weight"]


class Height(BaseModel):
    unit: Literal["in", "cm"]

    value: float


class Weight(BaseModel):
    unit: Literal["lbs", "kg"]

    value: float


class StudyReportMetadata(BaseModel):
    """Metadata for a study report including patient demographics and scan information"""

    age: Optional[str] = None

    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)

    facility_name: Optional[str] = FieldInfo(alias="facilityName", default=None)

    height: Optional[Height] = None

    mrn: Optional[str] = None

    patient_name: Optional[str] = FieldInfo(alias="patientName", default=None)

    referring_physician_name: Optional[str] = FieldInfo(alias="referringPhysicianName", default=None)

    scan_date: Optional[str] = FieldInfo(alias="scanDate", default=None)

    scan_time: Optional[str] = FieldInfo(alias="scanTime", default=None)

    scan_type: Optional[str] = FieldInfo(alias="scanType", default=None)

    sex: Optional[Literal["male", "female", "other"]] = None

    weight: Optional[Weight] = None
