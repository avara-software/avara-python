# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ReportListResponse"]


class ReportListResponse(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_report_id: str = FieldInfo(alias="externalReportId")

    has_report_text: bool = FieldInfo(alias="hasReportText")

    report_pdf_present: bool = FieldInfo(alias="reportPdfPresent")

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")

    reader_name: Optional[str] = FieldInfo(alias="readerName", default=None)

    signed_at: Optional[str] = FieldInfo(alias="signedAt", default=None)
