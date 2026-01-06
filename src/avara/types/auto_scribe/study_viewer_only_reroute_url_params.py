# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StudyViewerOnlyRerouteURLParams"]


class StudyViewerOnlyRerouteURLParams(TypedDict, total=False):
    study_id: Annotated[str, PropertyInfo(alias="studyId")]

    study_instance_uid: Annotated[str, PropertyInfo(alias="studyInstanceUid")]

    user_id: Annotated[str, PropertyInfo(alias="userId")]
