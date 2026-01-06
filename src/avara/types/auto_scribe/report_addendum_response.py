# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ReportAddendumResponse"]


class ReportAddendumResponse(BaseModel):
    """Response for creating a report addendum"""

    success: bool

    message: Optional[str] = None
