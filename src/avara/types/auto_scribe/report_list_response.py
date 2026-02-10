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
    """Timestamp when the report was created"""

    is_addendum: bool = FieldInfo(alias="isAddendum")
    """Whether this report is an addendum to a previous report"""

    report_id: str = FieldInfo(alias="reportId")
    """Unique report identifier. Format: rep\\__{32-hex-chars}"""

    signed_at: Optional[datetime] = FieldInfo(alias="signedAt", default=None)
    """Timestamp when the report was signed, null if not yet signed"""

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Patient demographics and scan information for report generation"""

    status: Literal["in_progress", "completed"]
    """Report status"""

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


class ReportListResponse(BaseModel):
    """Response containing a list of reports for a study"""

    reports: List[Report]
    """Array of report objects with full details"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID the reports belong to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """
