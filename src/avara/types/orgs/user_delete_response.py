# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UserDeleteResponse"]


class UserDeleteResponse(BaseModel):
    """Standard success response with optional message"""

    success: bool

    message: Optional[str] = None
