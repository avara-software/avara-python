# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ExternalDeleteResponse"]


class ExternalDeleteResponse(BaseModel):
    """Result of deleting an external study"""

    success: bool

    message: Optional[str] = None
