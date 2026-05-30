# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared.severity import Severity
from .prior_report_param import PriorReportParam
from ..study_report_metadata_param import StudyReportMetadataParam

__all__ = ["StudyCreateParams"]


class StudyCreateParams(TypedDict, total=False):
    report_metadata: Required[Annotated[StudyReportMetadataParam, PropertyInfo(alias="reportMetadata")]]
    """Patient demographics and scan information for report generation"""

    severity: Required[Severity]
    """Priority level of a study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention.
    """

    study_description: Required[Annotated[str, PropertyInfo(alias="studyDescription")]]
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_instance_uid: Required[Annotated[str, PropertyInfo(alias="studyInstanceUid")]]
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]
    """User ID to assign the study to. Format: usr\\__{32-hex-chars}"""

    clinical_history: Annotated[Optional[str], PropertyInfo(alias="clinicalHistory")]
    """Relevant clinical history for the patient/study"""

    clinical_indication: Annotated[Optional[str], PropertyInfo(alias="clinicalIndication")]
    """Clinical indication for the study (reason the study was ordered)"""

    express_customer_id: Annotated[str, PropertyInfo(alias="expressCustomerId")]
    """Express customer ID for the study. Format: cus\\__{32-hex-chars}"""

    external_patient_id: Annotated[Optional[str], PropertyInfo(alias="externalPatientId")]
    """
    Integrator-provided stable patient identifier used to link studies for the same
    patient across the AutoScribe system
    """

    metadata: Dict[str, str]
    """Custom key-value metadata for the study.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """

    modality: Optional[str]
    """Imaging modality for the study (free text, e.g., 'CT', 'MRI', 'X-Ray')"""

    prior_reports: Annotated[Iterable[PriorReportParam], PropertyInfo(alias="priorReports")]
    """
    External prior reports (metadata + full report text) to provide
    longitudinal/comparison context for this study. Maximum 50 items
    """

    technologist_notes: Annotated[SequenceNotStr[str], PropertyInfo(alias="technologistNotes")]
    """Technologist notes for the study. Maximum 50 items, each up to 1000 characters"""

    technologist_technique: Annotated[Optional[str], PropertyInfo(alias="technologistTechnique")]
    """Imaging technique description provided by the technologist"""
