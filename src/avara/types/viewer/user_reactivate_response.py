# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UserReactivateResponse"]


class UserReactivateResponse(BaseModel):
    """Response for reactivating a user in Viewer"""

    success: bool

    message: Optional[str] = None
