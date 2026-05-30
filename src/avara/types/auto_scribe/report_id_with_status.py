# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..report_status import ReportStatus

__all__ = ["ReportIDWithStatus"]


class ReportIDWithStatus(BaseModel):
    """A report ID paired with its current status"""

    report_id: str = FieldInfo(alias="reportId")
    """Unique report identifier. Format: rep\\__{32-hex-chars}"""

    status: ReportStatus
    """Status of an individual report.

    'in_progress' = actively being dictated, 'completed' = signed.
    """
