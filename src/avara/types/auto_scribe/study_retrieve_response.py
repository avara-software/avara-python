# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .report_id_with_status import ReportIDWithStatus
from ..study_report_metadata import StudyReportMetadata

__all__ = ["StudyRetrieveResponse", "AssignedTo", "CreatedByAPIKey", "CreatedByUser", "Org"]


class AssignedTo(BaseModel):
    """Reference to the assigned radiologist, null if unassigned"""

    email: str

    user_id: str = FieldInfo(alias="userId")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)

    suffix1: Optional[str] = None

    suffix2: Optional[str] = None


class CreatedByAPIKey(BaseModel):
    """Reference to the API key used to create this study"""

    api_key_id: str = FieldInfo(alias="apiKeyId")

    description: str

    is_viewer_enabled: Optional[bool] = FieldInfo(alias="isViewerEnabled", default=None)


class CreatedByUser(BaseModel):
    """Reference to the user who created this study via dashboard"""

    email: str

    user_id: str = FieldInfo(alias="userId")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)

    suffix1: Optional[str] = None

    suffix2: Optional[str] = None


class Org(BaseModel):
    """Reference to the organization this study belongs to"""

    org_id: str = FieldInfo(alias="orgId")

    org_name: str = FieldInfo(alias="orgName")


class StudyRetrieveResponse(BaseModel):
    """A study entity in the AutoScribe system with report workflow status"""

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)
    """Timestamp when the study was cancelled, null if not cancelled"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the study was created"""

    is_cancelled: bool = FieldInfo(alias="isCancelled")
    """Whether the study has been cancelled"""

    report_metadata: StudyReportMetadata = FieldInfo(alias="reportMetadata")
    """Patient demographics and scan information for report generation"""

    severity: Literal["normal", "high", "stat"]
    """Priority level of the study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention
    """

    study_description: str = FieldInfo(alias="studyDescription")
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_id: str = FieldInfo(alias="studyId")
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    study_report_status: Literal["unassigned", "assigned", "in_progress", "completed", "addendum_active"] = FieldInfo(
        alias="studyReportStatus"
    )
    """Report workflow status.

    'unassigned' = no radiologist assigned, 'assigned' = assigned but not started,
    'in_progress' = actively being dictated, 'completed' = report signed,
    'addendum_active' = addendum in progress
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the study was last updated"""

    assigned_to: Optional[AssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """Reference to the assigned radiologist, null if unassigned"""

    created_by_api_key: Optional[CreatedByAPIKey] = FieldInfo(alias="createdByApiKey", default=None)
    """Reference to the API key used to create this study"""

    created_by_user: Optional[CreatedByUser] = FieldInfo(alias="createdByUser", default=None)
    """Reference to the user who created this study via dashboard"""

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata for the study.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """

    org: Optional[Org] = None
    """Reference to the organization this study belongs to"""

    prior_report_texts: Optional[List[str]] = FieldInfo(alias="priorReportTexts", default=None)
    """Array of prior report texts to provide clinical context"""

    prior_study_ids: Optional[List[str]] = FieldInfo(alias="priorStudyIds", default=None)
    """Array of prior study IDs for comparison context (format: stu\\__{32-hex-chars})"""

    report_ids: Optional[List[ReportIDWithStatus]] = FieldInfo(alias="reportIds", default=None)
    """Array of report IDs associated with this study, including addendums"""
