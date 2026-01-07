# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.org_reference import OrgReference
from ..shared.user_reference import UserReference
from ..shared.api_key_reference import APIKeyReference

__all__ = ["StudyCreateResponse"]


class StudyCreateResponse(BaseModel):
    """A study entity in the Viewer system with viewing status"""

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)
    """Timestamp when the study was cancelled, null if not cancelled"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the study was created"""

    is_cancelled: bool = FieldInfo(alias="isCancelled")
    """Whether the study has been cancelled"""

    severity: Literal["normal", "high", "stat"]
    """Priority level of the study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention
    """

    study_description: str = FieldInfo(alias="studyDescription")
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_id: str = FieldInfo(alias="studyId")
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    study_viewer_status: Literal["incomplete", "complete"] = FieldInfo(alias="studyViewerStatus")

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp when the study was last updated"""

    assigned_to: Optional[UserReference] = FieldInfo(alias="assignedTo", default=None)
    """A reference to a user with basic identifying information"""

    created_by_api_key: Optional[APIKeyReference] = FieldInfo(alias="createdByApiKey", default=None)
    """A reference to an API key with basic identifying information"""

    created_by_user: Optional[UserReference] = FieldInfo(alias="createdByUser", default=None)
    """A reference to a user with basic identifying information"""

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata for the study.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """

    org: Optional[OrgReference] = None
    """A reference to an organization with basic identifying information"""
