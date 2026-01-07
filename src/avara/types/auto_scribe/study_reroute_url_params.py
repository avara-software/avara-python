# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StudyRerouteURLParams"]


class StudyRerouteURLParams(TypedDict, total=False):
    assigned_to_user_id: Required[Annotated[str, PropertyInfo(alias="assignedToUserId")]]
    """User ID to assign study to. Format: usr\\__{32-hex-chars}"""

    study_id: Annotated[str, PropertyInfo(alias="studyId")]
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: Annotated[str, PropertyInfo(alias="studyInstanceUid")]
    """DICOM Study Instance UID"""
