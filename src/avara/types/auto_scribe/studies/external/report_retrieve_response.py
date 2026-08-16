# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....study_report_metadata import StudyReportMetadata

__all__ = ["ReportRetrieveResponse"]


class ReportRetrieveResponse(BaseModel):
    """External report snapshot including text and/or a presigned file URL"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_report_id: str = FieldInfo(alias="externalReportId")

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")

    presigned_url: Optional[str] = FieldInfo(alias="presignedUrl", default=None)
    """Short-lived download URL for the attached PDF or image.

    Not used for AI tooling; the reader can still access it.
    """

    reader_name: Optional[str] = FieldInfo(alias="readerName", default=None)

    report_text: Optional[str] = FieldInfo(alias="reportText", default=None)
    """
    When this study is used as a prior, report AI tools leverage this text directly.
    """

    signed_at: Optional[str] = FieldInfo(alias="signedAt", default=None)

    snapshot_metadata: Optional[StudyReportMetadata] = FieldInfo(alias="snapshotMetadata", default=None)
    """Patient demographics and scan information for report generation"""
