# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.severity import Severity
from ..study_viewer_status import StudyViewerStatus

__all__ = ["StudyUpdateParams"]


class StudyUpdateParams(TypedDict, total=False):
    assigned_to: Annotated[str, PropertyInfo(alias="assignedTo")]
    """User ID to assign the study to, or null to unassign.

    Format: usr\\__{32-hex-chars}
    """

    metadata: Optional[Dict[str, str]]

    severity: Severity
    """Priority level of a study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention.
    """

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_viewer_status: Annotated[StudyViewerStatus, PropertyInfo(alias="studyViewerStatus")]
    """Viewer completion status for a study.

    'incomplete' = not yet finished in the viewer, 'complete' = finished.
    """
