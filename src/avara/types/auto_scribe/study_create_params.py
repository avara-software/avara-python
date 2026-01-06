# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..study_report_metadata_param import StudyReportMetadataParam

__all__ = ["StudyCreateParams"]


class StudyCreateParams(TypedDict, total=False):
    report_metadata: Required[Annotated[StudyReportMetadataParam, PropertyInfo(alias="reportMetadata")]]
    """Metadata for a study report including patient demographics and scan information"""

    severity: Required[Literal["normal", "high", "stat"]]

    study_description: Required[Annotated[str, PropertyInfo(alias="studyDescription")]]

    study_instance_uid: Required[Annotated[str, PropertyInfo(alias="studyInstanceUid")]]

    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]

    metadata: Dict[str, str]

    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    prior_report_texts: Annotated[SequenceNotStr[str], PropertyInfo(alias="priorReportTexts")]

    prior_study_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="priorStudyIds")]
