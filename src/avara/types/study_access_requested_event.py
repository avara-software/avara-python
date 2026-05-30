# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .study_access_requested_event_data import StudyAccessRequestedEventData

__all__ = ["StudyAccessRequestedEvent"]


class StudyAccessRequestedEvent(BaseModel):
    """Webhook event sent when Avara needs presigned URLs for DICOM images.

    This is a synchronous webhook - you must respond with the URLs within the request timeout.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: StudyAccessRequestedEventData
    """Event payload containing study information"""

    type: Literal["study.access_requested"]
    """Event type identifier"""
