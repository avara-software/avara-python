# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReportTextParams"]


class ReportTextParams(TypedDict, total=False):
    report_id: Annotated[str, PropertyInfo(alias="reportId")]
    """Report ID. Format: rep\\__<32-hex-chars>"""

    study_id: Annotated[str, PropertyInfo(alias="studyId")]
    """Study ID. Format: stu\\__<32-hex-chars>"""

    study_instance_uid: Annotated[str, PropertyInfo(alias="studyInstanceUid")]
    """DICOM Study Instance UID"""
