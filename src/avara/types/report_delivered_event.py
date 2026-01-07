# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReportDeliveredEvent", "Data"]


class Data(BaseModel):
    """Event payload containing report and study information"""

    presigned_url: str = FieldInfo(alias="presignedUrl")
    """Presigned URL for PDF download. Time-limited, typically valid for 1 hour."""

    report_id: str = FieldInfo(alias="reportId")
    """Avara report ID. Format: rep\\__{32-hex-chars}"""

    study_id: str = FieldInfo(alias="studyId")
    """Avara study ID. Format: stu\\__{32-hex-chars}"""

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)
    """Report plain text content (optional). Contains the full report text."""


class ReportDeliveredEvent(BaseModel):
    """Webhook event sent when a report is completed.

    This is an asynchronous notification - respond with a simple acknowledgment.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: Data
    """Event payload containing report and study information"""

    type: Literal["report.delivered"]
    """Event type identifier"""
