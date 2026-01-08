# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["StudyUpdateParams", "ReportMetadata", "ReportMetadataHeight", "ReportMetadataWeight"]


class StudyUpdateParams(TypedDict, total=False):
    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]
    """User ID to assign the study to, or null to unassign.

    Format: usr\\__{32-hex-chars}
    """

    metadata: Optional[Dict[str, str]]

    org_id: Annotated[str, PropertyInfo(alias="orgId")]
    """Organization ID for the study, or null to remove. Format: org\\__{32-hex-chars}"""

    prior_report_texts: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="priorReportTexts")]

    prior_study_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="priorStudyIds")]

    report_metadata: Annotated[ReportMetadata, PropertyInfo(alias="reportMetadata")]

    severity: Literal["normal", "high", "stat"]
    """Priority level of the study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention
    """

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""


class ReportMetadataHeight(TypedDict, total=False):
    unit: Required[Literal["in", "cm"]]

    value: Required[float]


class ReportMetadataWeight(TypedDict, total=False):
    unit: Required[Literal["lbs", "kg"]]

    value: Required[float]


class ReportMetadata(TypedDict, total=False):
    age: Optional[str]

    date_of_birth: Annotated[Optional[str], PropertyInfo(alias="dateOfBirth")]

    facility_name: Annotated[Optional[str], PropertyInfo(alias="facilityName")]

    height: Optional[ReportMetadataHeight]

    mrn: Optional[str]

    patient_name: Annotated[Optional[str], PropertyInfo(alias="patientName")]

    referring_physician_name: Annotated[Optional[str], PropertyInfo(alias="referringPhysicianName")]

    scan_date: Annotated[Optional[str], PropertyInfo(alias="scanDate")]

    scan_time: Annotated[Optional[str], PropertyInfo(alias="scanTime")]

    scan_type: Annotated[Optional[str], PropertyInfo(alias="scanType")]

    sex: Optional[Literal["male", "female", "other"]]

    weight: Optional[ReportMetadataWeight]
