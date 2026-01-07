# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..study_report_metadata import StudyReportMetadata

__all__ = ["ReportListResponse", "Report"]


class Report(BaseModel):
    """A radiology report in the AutoScribe system"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_addendum: bool = FieldInfo(alias="isAddendum")

    report_id: str = FieldInfo(alias="reportId")

    signed_at: Optional[datetime] = FieldInfo(alias="signedAt", default=None)

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Patient demographics and scan information for report generation"""

    status: Literal["in_progress", "completed"]

    study_id: str = FieldInfo(alias="studyId")

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")

    report_plain_text: Optional[str] = FieldInfo(alias="reportPlainText", default=None)


class ReportListResponse(BaseModel):
    """Response containing a list of reports for a study"""

    reports: List[Report]

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
