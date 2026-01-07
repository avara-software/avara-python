# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrgCreateResponse"]


class OrgCreateResponse(BaseModel):
    """An organization entity that groups users and studies"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the organization was created"""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether the organization is currently active"""

    org_id: str = FieldInfo(alias="orgId")
    """Unique organization identifier. Format: org\\__{32-hex-chars}"""

    org_name: str = FieldInfo(alias="orgName")
    """Name of the organization"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the organization was last updated"""

    user_count: int = FieldInfo(alias="userCount")
    """Number of users currently in this organization"""

    created_by_api_key_id: Optional[str] = FieldInfo(alias="createdByApiKeyId", default=None)
    """UUID of the API key used to create this organization, for audit tracking"""

    created_by_user_id: Optional[str] = FieldInfo(alias="createdByUserId", default=None)
    """
    User ID who created this organization via dashboard, null if created via API key
    """

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata for the organization.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """
