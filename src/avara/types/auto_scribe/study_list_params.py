# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.severity import Severity
from ..study_report_status import StudyReportStatus

__all__ = ["StudyListParams"]


class StudyListParams(TypedDict, total=False):
    assigned_to: Annotated[Optional[str], PropertyInfo(alias="assignedTo")]
    """Filter by assigned user ID (null = explicitly unassigned).

    Format: usr\\__<32-hex-chars>
    """

    cursor: str
    """Base64 encoded cursor from previous response"""

    express_customer_id: Annotated[Optional[str], PropertyInfo(alias="expressCustomerId")]
    """Filter by Express customer ID (null = studies with no customer).

    Format: cus\\__{32-hex-chars}
    """

    is_cancelled: Annotated[Optional[bool], PropertyInfo(alias="isCancelled")]
    """Filter by cancellation status"""

    limit: float
    """Number of results to return (1-100)"""

    severity: Severity
    """Filter by study severity"""

    study_description: Annotated[str, PropertyInfo(alias="studyDescription")]
    """Filter by study description (contains match)"""

    study_report_status: Annotated[List[StudyReportStatus], PropertyInfo(alias="studyReportStatus")]
    """Filter by report status(es)"""
