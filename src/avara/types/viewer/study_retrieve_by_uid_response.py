# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.severity import Severity
from ..study_viewer_status import StudyViewerStatus
from ..shared.user_reference import UserReference
from ..shared.api_key_reference import APIKeyReference
from ..shared.express_customer_reference import ExpressCustomerReference

__all__ = ["StudyRetrieveByUidResponse"]


class StudyRetrieveByUidResponse(BaseModel):
    """A study entity in the Viewer system with viewing status"""

    cancelled_at: Optional[datetime] = FieldInfo(alias="cancelledAt", default=None)
    """Timestamp when the study was cancelled, null if not cancelled"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the study was created"""

    is_cancelled: bool = FieldInfo(alias="isCancelled")
    """Whether the study has been cancelled"""

    severity: Severity
    """Priority level of a study.

    'normal' for routine, 'high' for urgent, 'stat' for immediate attention.
    """

    study_description: str = FieldInfo(alias="studyDescription")
    """Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')"""

    study_id: str = FieldInfo(alias="studyId")
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    study_viewer_status: StudyViewerStatus = FieldInfo(alias="studyViewerStatus")
    """Viewer completion status for a study.

    'incomplete' = not yet finished in the viewer, 'complete' = finished.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the study was last updated"""

    assigned_to: Optional[UserReference] = FieldInfo(alias="assignedTo", default=None)
    """A reference to a user with basic identifying information"""

    created_by_api_key: Optional[APIKeyReference] = FieldInfo(alias="createdByApiKey", default=None)
    """A reference to an API key with basic identifying information"""

    created_by_user: Optional[UserReference] = FieldInfo(alias="createdByUser", default=None)
    """A reference to a user with basic identifying information"""

    express_customer: Optional[ExpressCustomerReference] = FieldInfo(alias="expressCustomer", default=None)
    """A reference to an Express customer with basic identifying information"""

    metadata: Optional[Dict[str, str]] = None
    """Custom key-value metadata for the study.

    Maximum 50 pairs, keys up to 100 chars, values up to 1000 chars
    """
