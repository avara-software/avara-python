# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrgUpdateResponse"]


class OrgUpdateResponse(BaseModel):
    """An organization entity that groups users and studies"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_active: bool = FieldInfo(alias="isActive")

    org_id: str = FieldInfo(alias="orgId")

    org_name: str = FieldInfo(alias="orgName")

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_count: int = FieldInfo(alias="userCount")

    created_by_api_key_id: Optional[str] = FieldInfo(alias="createdByApiKeyId", default=None)

    created_by_user_id: Optional[str] = FieldInfo(alias="createdByUserId", default=None)

    metadata: Optional[Dict[str, str]] = None
