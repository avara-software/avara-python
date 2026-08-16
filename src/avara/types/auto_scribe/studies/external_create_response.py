# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...study_type import StudyType
from ..prior_report import PriorReport
from ...shared.severity import Severity
from ...study_report_status import StudyReportStatus
from ..report_id_with_status import ReportIDWithStatus
from ...shared.user_reference import UserReference
from ...study_report_metadata import StudyReportMetadata
from ...shared.api_key_reference import APIKeyReference
from ...shared.express_customer_reference import ExpressCustomerReference

__all__ = ["ExternalCreateResponse"]


class ExternalCreateResponse(BaseModel):
    """A study entity in the AutoScribe system with report workflow status"""

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)
    """Timestamp when the study was cancelled, null if not cancelled"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the study was created"""

    is_cancelled: bool = FieldInfo(alias="isCancelled")
    """Whether the study has been cancelled"""

    report_metadata: StudyReportMetadata = FieldInfo(alias="reportMetadata")
    """Patient demographics and scan information for report generation"""

    severity: Severity
    """Priority level of a study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention.
    """

    study_description: str = FieldInfo(alias="studyDescription")
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_id: str = FieldInfo(alias="studyId")
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    study_report_status: StudyReportStatus = FieldInfo(alias="studyReportStatus")
    """AutoScribe report workflow status for a study.

    'unassigned' = no radiologist assigned, 'assigned' = assigned but not started,
    'in_progress' = actively being dictated, 'completed' = report signed,
    'addendum_active' = addendum in progress.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the study was last updated"""

    assigned_to: Optional[UserReference] = FieldInfo(alias="assignedTo", default=None)
    """A reference to a user with basic identifying information"""

    clinical_history: Optional[str] = FieldInfo(alias="clinicalHistory", default=None)
    """Relevant clinical history for the study"""

    clinical_indication: Optional[str] = FieldInfo(alias="clinicalIndication", default=None)
    """Clinical indication for the study"""

    created_by_api_key: Optional[APIKeyReference] = FieldInfo(alias="createdByApiKey", default=None)
    """A reference to an API key with basic identifying information"""

    created_by_user: Optional[UserReference] = FieldInfo(alias="createdByUser", default=None)
    """A reference to a user with basic identifying information"""

    express_customer: Optional[ExpressCustomerReference] = FieldInfo(alias="expressCustomer", default=None)
    """A reference to an Express customer with basic identifying information"""

    external_patient_id: Optional[str] = FieldInfo(alias="externalPatientId", default=None)
    """Integrator-provided stable patient identifier for linking studies"""

    external_report_id: Optional[str] = FieldInfo(alias="externalReportId", default=None)
    """External report identifier when this study has an attached archive report.

    Format: ext\\__{32-hex-chars}
    """

    is_critical: Optional[bool] = FieldInfo(alias="isCritical", default=None)
    """Whether the primary report was marked as critical at sign-off"""

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata for the study.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """

    modality: Optional[str] = None
    """Imaging modality for the study (free text)"""

    prior_reports: Optional[List[PriorReport]] = FieldInfo(alias="priorReports", default=None)
    """External prior reports with metadata and text"""

    report_ids: Optional[List[ReportIDWithStatus]] = FieldInfo(alias="reportIds", default=None)
    """Array of report IDs associated with this study, including addendums"""

    study_type: Optional[StudyType] = FieldInfo(alias="studyType", default=None)
    """Kind of study.

    'standard' is a live AutoScribe reading-workflow study. 'external' is an
    imported archive study.
    """

    technologist_notes: Optional[List[str]] = FieldInfo(alias="technologistNotes", default=None)
    """Technologist notes for the study"""

    technologist_technique: Optional[str] = FieldInfo(alias="technologistTechnique", default=None)
    """Imaging technique description"""
