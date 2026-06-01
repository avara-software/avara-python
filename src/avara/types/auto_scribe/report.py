# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..report_status import ReportStatus
from ..study_report_metadata import StudyReportMetadata

__all__ = ["Report"]


class Report(BaseModel):
    """A radiology report in the AutoScribe system"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the report was created"""

    is_addendum: bool = FieldInfo(alias="isAddendum")
    """Whether this report is an addendum to a previous report"""

    is_critical: Optional[bool] = FieldInfo(alias="isCritical", default=None)
    """Whether the report was marked critical at sign-off.

    null when the report is not yet completed; true/false once completed.
    """

    report_id: str = FieldInfo(alias="reportId")
    """Unique report identifier. Format: rep\\__{32-hex-chars}"""

    signed_at: Optional[datetime] = FieldInfo(alias="signedAt", default=None)
    """Timestamp when the report was signed, null if not yet signed"""

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Patient demographics and scan information for report generation"""

    status: ReportStatus
    """Status of an individual report.

    'in_progress' = actively being dictated, 'completed' = signed.
    """

    study_id: str = FieldInfo(alias="studyId")
    """Study ID this report belongs to. Format: stu\\__{32-hex-chars}"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the report was last updated"""

    user_id: str = FieldInfo(alias="userId")
    """User ID of the radiologist who created/signed this report.

    Format: usr\\__{32-hex-chars}
    """

    report_plain_text: Optional[str] = FieldInfo(alias="reportPlainText", default=None)
    """Plain text content of the report"""
