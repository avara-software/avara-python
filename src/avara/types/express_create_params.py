# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExpressCreateParams"]


class ExpressCreateParams(TypedDict, total=False):
    express_customer_name: Required[Annotated[str, PropertyInfo(alias="expressCustomerName")]]
    """Name of the Express customer to create"""

    metadata: Dict[str, str]
    """Custom key-value metadata for the Express customer. Maximum 50 pairs"""
