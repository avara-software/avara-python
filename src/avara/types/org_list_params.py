# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrgListParams"]


class OrgListParams(TypedDict, total=False):
    cursor: str
    """Base64 encoded cursor from previous response"""

    limit: float
    """Number of results to return (1-100)"""
