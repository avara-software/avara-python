# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ReportIDWithStatus"]


class ReportIDWithStatus(BaseModel):
    """A report ID paired with its current status"""

    report_id: str = FieldInfo(alias="reportId")

    status: Literal["in_progress", "completed"]
