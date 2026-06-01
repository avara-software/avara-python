# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReportDeliveredEventData"]


class ReportDeliveredEventData(BaseModel):
    """Event payload containing report and study information"""

    is_critical: bool = FieldInfo(alias="isCritical")
    """Whether the report was marked critical at sign-out."""

    presigned_url: str = FieldInfo(alias="presignedUrl")
    """Presigned URL for PDF download. Time-limited, typically valid for 1 hour."""

    report_id: str = FieldInfo(alias="reportId")
    """Avara report ID. Format: rep\\__{32-hex-chars}"""

    study_id: str = FieldInfo(alias="studyId")
    """Avara study ID. Format: stu\\__{32-hex-chars}"""

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)
    """Report plain text content (optional). Contains the full report text."""
