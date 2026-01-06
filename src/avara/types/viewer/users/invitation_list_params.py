# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InvitationListParams"]


class InvitationListParams(TypedDict, total=False):
    cursor: str
    """Base64 encoded cursor from previous response"""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Filter invitations created on or before this date (YYYY-MM-DD)"""

    expired: Literal["all", "expired", "not-expired"]
    """Filter by expiration status"""

    limit: float
    """Number of results to return (1-100)"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Filter invitations created on or after this date (YYYY-MM-DD)"""

    status: List[Literal["sent", "accepted", "rejected", "revoked"]]
    """Filter by invitation status(es)"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Filter by user ID. Format: usr\\__<32-hex-chars>"""
