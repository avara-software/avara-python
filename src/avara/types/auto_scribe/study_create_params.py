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
    """Patient demographics and scan information for report generation"""

    severity: Required[Literal["normal", "high", "stat"]]
    """Priority level of the study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention
    """

    study_description: Required[Annotated[str, PropertyInfo(alias="studyDescription")]]
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_instance_uid: Required[Annotated[str, PropertyInfo(alias="studyInstanceUid")]]
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]
    """User ID to assign the study to. Format: usr\\__{32-hex-chars}"""

    metadata: Dict[str, str]
    """Custom key-value metadata for the study.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """

    org_id: Annotated[str, PropertyInfo(alias="orgId")]
    """Organization ID for the study. Format: org\\__{32-hex-chars}"""

    prior_report_texts: Annotated[SequenceNotStr[str], PropertyInfo(alias="priorReportTexts")]

    prior_study_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="priorStudyIds")]
