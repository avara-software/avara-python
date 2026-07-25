# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..clinical_reference_type import ClinicalReferenceType

__all__ = ["ClinicalReferenceCreateParams"]


class ClinicalReferenceCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[ClinicalReferenceType]
    """
    Category of canonical clinical reference value used for study workflow pickers
    and normalization.
    """

    express_customer_id: Annotated[str, PropertyInfo(alias="expressCustomerId")]

    external_reference_id: Annotated[Optional[str], PropertyInfo(alias="externalReferenceId")]

    metadata: Dict[str, str]
