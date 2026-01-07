# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReportListParams"]


class ReportListParams(TypedDict, total=False):
    study_id: Annotated[str, PropertyInfo(alias="studyId")]
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: Annotated[str, PropertyInfo(alias="studyInstanceUid")]
    """DICOM Study Instance UID"""
