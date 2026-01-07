# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKeyReference"]


class APIKeyReference(BaseModel):
    """A reference to an API key with basic identifying information"""

    api_key_id: str = FieldInfo(alias="apiKeyId")
    """Unique API key identifier (UUIDv4 format)"""

    description: str
    """Human-readable description of the API key"""

    is_viewer_enabled: Optional[bool] = FieldInfo(alias="isViewerEnabled", default=None)
    """Whether this API key has access to the Viewer product"""
