# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StudyListParams"]


class StudyListParams(TypedDict, total=False):
    assigned_to: Annotated[Optional[str], PropertyInfo(alias="assignedTo")]
    """Filter by assigned user ID (null = explicitly unassigned).

    Format: usr\\__<32-hex-chars>
    """

    cursor: str
    """Base64 encoded cursor from previous response"""

    is_cancelled: Annotated[Optional[bool], PropertyInfo(alias="isCancelled")]
    """Filter by cancellation status"""

    limit: float
    """Number of results to return (1-100)"""

    severity: Literal["normal", "high", "stat"]
    """Filter by study severity"""

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]
    """Filter by study description (contains match)"""

    study_viewer_status: Annotated[Literal["incomplete", "complete"], PropertyInfo(alias="studyViewerStatus")]
    """Filter by study viewer status"""
