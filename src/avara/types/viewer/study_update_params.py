# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StudyUpdateParams"]


class StudyUpdateParams(TypedDict, total=False):
    assigned_to: Annotated[Optional[str], PropertyInfo(alias="assignedTo")]

    metadata: Optional[Dict[str, str]]

    severity: Literal["normal", "high", "stat"]

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]

    study_viewer_status: Annotated[Literal["incomplete", "complete"], PropertyInfo(alias="studyViewerStatus")]
