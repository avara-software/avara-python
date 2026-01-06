# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    can_create_reports: Annotated[Optional[bool], PropertyInfo(alias="canCreateReports")]
    """Filter by canCreateReports permission (AutoScribe-specific)"""

    cursor: str
    """Base64 encoded cursor from previous response"""

    email: str
    """Filter by exact email match"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """Filter by first name (contains match)"""

    invited_source: Annotated[Literal["dashboard", "api"], PropertyInfo(alias="invitedSource")]
    """Filter by invitation source"""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Filter by last name (contains match)"""

    level: Literal["owner", "admin", "member"]
    """Filter by user level"""

    limit: float
    """Number of results to return (1-100)"""
