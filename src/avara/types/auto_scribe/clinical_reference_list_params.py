# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..clinical_reference_type import ClinicalReferenceType

__all__ = ["ClinicalReferenceListParams"]


class ClinicalReferenceListParams(TypedDict, total=False):
    cursor: str
    """Base64 encoded cursor from previous response"""

    express_customer_id: Annotated[str, PropertyInfo(alias="expressCustomerId")]
    """Filter by Express customer ID.

    Omit for no filter; pass null for clinic-wide references
    """

    is_active: Annotated[Optional[bool], PropertyInfo(alias="isActive")]
    """Filter by active status.

    Defaults to true (active references only). Pass false to list inactive
    references.
    """

    limit: float
    """Number of results to return (1-100)"""

    type: ClinicalReferenceType
    """Filter by clinical reference type"""
