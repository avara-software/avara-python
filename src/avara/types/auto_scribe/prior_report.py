# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PriorReport"]


class PriorReport(BaseModel):
    """External prior report metadata and text stored on a study"""

    report_text: str = FieldInfo(alias="reportText")
    """Full prior report text"""

    external_study_id: Optional[str] = FieldInfo(alias="externalStudyId", default=None)
    """Integrator's external study identifier"""

    modality: Optional[str] = None
    """Imaging modality for the prior study"""

    study_date: Optional[str] = FieldInfo(alias="studyDate", default=None)
    """Prior study date (YYYY-MM-DD)"""

    study_description: Optional[str] = FieldInfo(alias="studyDescription", default=None)
    """Description of the prior study"""
