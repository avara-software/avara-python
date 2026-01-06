# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.org_reference import OrgReference
from ..shared.user_reference import UserReference
from ..shared.api_key_reference import APIKeyReference

__all__ = ["StudyListResponse"]


class StudyListResponse(BaseModel):
    """A study entity in the Viewer system with viewing status"""

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    is_cancelled: bool = FieldInfo(alias="isCancelled")

    severity: Literal["normal", "high", "stat"]

    study_description: str = FieldInfo(alias="studyDescription")

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")

    study_viewer_status: Literal["incomplete", "complete"] = FieldInfo(alias="studyViewerStatus")

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    assigned_to: Optional[UserReference] = FieldInfo(alias="assignedTo", default=None)
    """A reference to a user with basic identifying information"""

    created_by_api_key: Optional[APIKeyReference] = FieldInfo(alias="createdByApiKey", default=None)
    """A reference to an API key with basic identifying information"""

    created_by_user: Optional[UserReference] = FieldInfo(alias="createdByUser", default=None)
    """A reference to a user with basic identifying information"""

    metadata: Optional[Dict[str, str]] = None

    org: Optional[OrgReference] = None
    """A reference to an organization with basic identifying information"""
