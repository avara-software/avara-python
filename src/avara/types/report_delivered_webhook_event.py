# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReportDeliveredWebhookEvent", "Data"]


class Data(BaseModel):
    presigned_url: str = FieldInfo(alias="presignedUrl")
    """Presigned URL for PDF download"""

    report_id: str = FieldInfo(alias="reportId")
    """Avara report ID (e.g., rep_1234567890abcdef1234567890abcdef)"""

    study_id: str = FieldInfo(alias="studyId")
    """Avara study ID (e.g., stu_1234567890abcdef1234567890abcdef)"""

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)
    """Report plain text content (optional)"""


class ReportDeliveredWebhookEvent(BaseModel):
    id: str
    """Unique webhook event ID (e.g., whe_1234567890abcdef1234567890abcdef)"""

    data: Data

    type: Literal["report.delivered"]
