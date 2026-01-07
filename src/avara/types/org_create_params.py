# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrgCreateParams"]


class OrgCreateParams(TypedDict, total=False):
    org_name: Required[Annotated[str, PropertyInfo(alias="orgName")]]
    """Name of the organization to create"""

    metadata: Dict[str, str]
    """Custom key-value metadata for the organization. Maximum 50 pairs"""
