# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .report import Report
from ..._models import BaseModel

__all__ = ["ReportListResponse"]


class ReportListResponse(BaseModel):
    """Response containing a list of reports for a study"""

    reports: List[Report]
    """Array of report objects with full details"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID the reports belong to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """
