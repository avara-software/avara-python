# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..sex import Sex
from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..height_unit import HeightUnit
from ..weight_unit import WeightUnit
from ..shared.severity import Severity
from .prior_report_param import PriorReportParam

__all__ = ["StudyUpdateParams", "ReportMetadata", "ReportMetadataHeight", "ReportMetadataWeight"]


class StudyUpdateParams(TypedDict, total=False):
    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]
    """User ID to assign the study to, or null to unassign.

    Format: usr\\__{32-hex-chars}
    """

    clinical_history: Annotated[Optional[str], PropertyInfo(alias="clinicalHistory")]
    """Relevant clinical history for the patient/study. Null clears."""

    clinical_indication: Annotated[Optional[str], PropertyInfo(alias="clinicalIndication")]
    """Clinical indication for the study. Null clears."""

    express_customer_id: Annotated[str, PropertyInfo(alias="expressCustomerId")]
    """Express Customer ID for the study, or null to remove.

    Format: cus\\__{32-hex-chars}
    """

    external_patient_id: Annotated[Optional[str], PropertyInfo(alias="externalPatientId")]
    """
    Integrator-provided stable patient identifier used to link studies for the same
    patient. Null clears.
    """

    metadata: Optional[Dict[str, str]]

    modality: Optional[str]
    """Imaging modality for the study (free text). Null clears."""

    prior_reports: Annotated[Optional[Iterable[PriorReportParam]], PropertyInfo(alias="priorReports")]
    """External prior reports (metadata + full report text) for comparison context.

    Null clears; an array replaces the existing set. Maximum 50 items
    """

    report_metadata: Annotated[ReportMetadata, PropertyInfo(alias="reportMetadata")]

    severity: Severity
    """Priority level of a study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention.
    """

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    technologist_notes: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="technologistNotes")]
    """Technologist notes for the study.

    Null clears; an array replaces the existing set. Maximum 50 items, each up to
    1000 characters
    """

    technologist_technique: Annotated[Optional[str], PropertyInfo(alias="technologistTechnique")]
    """Imaging technique description provided by the technologist. Null clears."""


class ReportMetadataHeight(TypedDict, total=False):
    unit: Required[HeightUnit]
    """Unit of measure for a height value. 'in' = inches, 'cm' = centimeters."""

    value: Required[float]


class ReportMetadataWeight(TypedDict, total=False):
    unit: Required[WeightUnit]
    """Unit of measure for a weight value. 'lbs' = pounds, 'kg' = kilograms."""

    value: Required[float]


class ReportMetadata(TypedDict, total=False):
    age: Optional[str]

    date_of_birth: Annotated[Optional[str], PropertyInfo(alias="dateOfBirth")]

    facility_name: Annotated[Optional[str], PropertyInfo(alias="facilityName")]

    height: Optional[ReportMetadataHeight]

    mrn: Optional[str]

    patient_name: Annotated[Optional[str], PropertyInfo(alias="patientName")]

    procedure: Optional[str]
    """Procedure or study type.

    Nullable on PATCH. Maps to DB scan_type and report_header.scan_type.
    """

    referring_physician_name: Annotated[Optional[str], PropertyInfo(alias="referringPhysicianName")]

    sex: Optional[Sex]
    """Patient's biological sex. Options: 'male', 'female', 'other'"""

    study_date: Annotated[Optional[str], PropertyInfo(alias="studyDate")]
    """Study date (YYYY-MM-DD).

    Nullable on PATCH. Maps to DB scan_date and report_header.scan_date.
    """

    study_time: Annotated[Optional[str], PropertyInfo(alias="studyTime")]
    """Study time (HH:MM).

    Nullable on PATCH. Maps to DB scan_time and report_header.scan_time.
    """

    weight: Optional[ReportMetadataWeight]
