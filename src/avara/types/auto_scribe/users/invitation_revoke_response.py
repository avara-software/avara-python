# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["InvitationRevokeResponse"]


class InvitationRevokeResponse(BaseModel):
    """Response for revoking an invitation in AutoScribe"""

    success: bool

    message: Optional[str] = None
