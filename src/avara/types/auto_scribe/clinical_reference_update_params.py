# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ClinicalReferenceUpdateParams"]


class ClinicalReferenceUpdateParams(TypedDict, total=False):
    express_customer_id: Annotated[str, PropertyInfo(alias="expressCustomerId")]

    metadata: Optional[Dict[str, str]]

    name: str
