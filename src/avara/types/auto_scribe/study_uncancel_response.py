# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["StudyUncancelResponse"]


class StudyUncancelResponse(BaseModel):
    """Response for uncancelling a study in AutoScribe"""

    success: bool

    message: Optional[str] = None
