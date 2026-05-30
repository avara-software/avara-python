# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .prior_report import PriorReport
from ..shared.severity import Severity
from ..study_report_status import StudyReportStatus
from .report_id_with_status import ReportIDWithStatus
from ..study_report_metadata import StudyReportMetadata

__all__ = ["StudyListResponse", "AssignedTo", "CreatedByAPIKey", "CreatedByUser", "ExpressCustomer"]


class AssignedTo(BaseModel):
    """Reference to the assigned radiologist, null if unassigned"""

    email: str
    """User's email address"""

    user_id: str = FieldInfo(alias="userId")
    """Unique user identifier. Format: usr\\__{32-hex-chars}"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """User's first name"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """User's last name"""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """User's middle name"""

    suffix1: Optional[str] = None
    """Name suffix (e.g., 'MD', 'Jr.')"""

    suffix2: Optional[str] = None
    """Additional name suffix"""


class CreatedByAPIKey(BaseModel):
    """Reference to the API key used to create this study"""

    api_key_id: str = FieldInfo(alias="apiKeyId")
    """Unique API key identifier (UUIDv4 format)"""

    description: str
    """Human-readable description of the API key"""

    is_viewer_enabled: Optional[bool] = FieldInfo(alias="isViewerEnabled", default=None)
    """Whether this API key has access to the Viewer product"""


class CreatedByUser(BaseModel):
    """Reference to the user who created this study via dashboard"""

    email: str
    """User's email address"""

    user_id: str = FieldInfo(alias="userId")
    """Unique user identifier. Format: usr\\__{32-hex-chars}"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """User's first name"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """User's last name"""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """User's middle name"""

    suffix1: Optional[str] = None
    """Name suffix (e.g., 'MD', 'Jr.')"""

    suffix2: Optional[str] = None
    """Additional name suffix"""


class ExpressCustomer(BaseModel):
    """Reference to the Express customer this study belongs to"""

    express_customer_id: str = FieldInfo(alias="expressCustomerId")
    """Unique Express customer identifier. Format: cus\\__{32-hex-chars}"""

    express_customer_name: str = FieldInfo(alias="expressCustomerName")
    """Name of the Express customer"""


class StudyListResponse(BaseModel):
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

    assigned_to: Optional[AssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """Reference to the assigned radiologist, null if unassigned"""

    clinical_history: Optional[str] = FieldInfo(alias="clinicalHistory", default=None)
    """Relevant clinical history for the study"""

    clinical_indication: Optional[str] = FieldInfo(alias="clinicalIndication", default=None)
    """Clinical indication for the study"""

    created_by_api_key: Optional[CreatedByAPIKey] = FieldInfo(alias="createdByApiKey", default=None)
    """Reference to the API key used to create this study"""

    created_by_user: Optional[CreatedByUser] = FieldInfo(alias="createdByUser", default=None)
    """Reference to the user who created this study via dashboard"""

    express_customer: Optional[ExpressCustomer] = FieldInfo(alias="expressCustomer", default=None)
    """Reference to the Express customer this study belongs to"""

    external_patient_id: Optional[str] = FieldInfo(alias="externalPatientId", default=None)
    """Integrator-provided stable patient identifier for linking studies"""

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

    technologist_notes: Optional[List[str]] = FieldInfo(alias="technologistNotes", default=None)
    """Technologist notes for the study"""

    technologist_technique: Optional[str] = FieldInfo(alias="technologistTechnique", default=None)
    """Imaging technique description"""
