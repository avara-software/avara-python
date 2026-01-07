# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgUpdateParams"]


class OrgUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, str]]
    """Updated metadata. Pass null to clear all metadata"""

    org_name: Annotated[str, PropertyInfo(alias="orgName")]
    """Updated name for the organization"""
