# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PriorReportParam"]


class PriorReportParam(TypedDict, total=False):
    """External prior report metadata and text stored on a study"""

    report_text: Required[Annotated[str, PropertyInfo(alias="reportText")]]
    """Full prior report text"""

    external_study_id: Annotated[str, PropertyInfo(alias="externalStudyId")]
    """Integrator's external study identifier"""

    modality: str
    """Imaging modality for the prior study"""

    study_date: Annotated[str, PropertyInfo(alias="studyDate")]
    """Prior study date (YYYY-MM-DD)"""

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]
    """Description of the prior study"""
