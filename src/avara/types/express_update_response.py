# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExpressUpdateResponse"]


class ExpressUpdateResponse(BaseModel):
    """An Express customer entity that groups users and studies"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the Express customer was created"""

    express_customer_id: str = FieldInfo(alias="expressCustomerId")
    """Unique Express customer identifier. Format: cus\\__{32-hex-chars}"""

    express_customer_name: str = FieldInfo(alias="expressCustomerName")
    """Name of the Express customer"""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether the Express customer is currently active"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the Express customer was last updated"""

    user_count: int = FieldInfo(alias="userCount")
    """Number of users currently in this Express customer"""

    created_by_api_key_id: Optional[str] = FieldInfo(alias="createdByApiKeyId", default=None)
    """UUID of the API key used to create this Express customer, for audit tracking"""

    created_by_user_id: Optional[str] = FieldInfo(alias="createdByUserId", default=None)
    """
    User ID who created this Express customer via dashboard, null if created via API
    key
    """

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata for the Express customer.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """
