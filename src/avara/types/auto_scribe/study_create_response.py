# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.org_reference import OrgReference
from .report_id_with_status import ReportIDWithStatus
from ..shared.user_reference import UserReference
from ..study_report_metadata import StudyReportMetadata
from ..shared.api_key_reference import APIKeyReference

__all__ = ["StudyCreateResponse"]


class StudyCreateResponse(BaseModel):
    """A study entity in the AutoScribe system with report workflow status"""

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    report_metadata: StudyReportMetadata = FieldInfo(alias="reportMetadata")
    """Metadata for a study report including patient demographics and scan information"""

    severity: Literal["normal", "high", "stat"]

    study_description: str = FieldInfo(alias="studyDescription")

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")

    study_report_status: Literal["unassigned", "assigned", "in_progress", "completed", "addendum_active"] = FieldInfo(
        alias="studyReportStatus"
    )

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    assigned_to: Optional[UserReference] = FieldInfo(alias="assignedTo", default=None)
    """A reference to a user with basic identifying information"""

    created_by_api_key: Optional[APIKeyReference] = FieldInfo(alias="createdByApiKey", default=None)
    """A reference to an API key with basic identifying information"""

    created_by_user: Optional[UserReference] = FieldInfo(alias="createdByUser", default=None)
    """A reference to a user with basic identifying information"""

    metadata: Optional[Dict[str, str]] = None

    org: Optional[OrgReference] = None
    """A reference to an organization with basic identifying information"""

    prior_report_texts: Optional[List[str]] = FieldInfo(alias="priorReportTexts", default=None)

    prior_study_ids: Optional[List[str]] = FieldInfo(alias="priorStudyIds", default=None)

    report_ids: Optional[List[ReportIDWithStatus]] = FieldInfo(alias="reportIds", default=None)
