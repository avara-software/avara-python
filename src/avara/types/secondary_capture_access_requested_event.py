# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .secondary_capture_access_requested_event_data import SecondaryCaptureAccessRequestedEventData

__all__ = ["SecondaryCaptureAccessRequestedEvent"]


class SecondaryCaptureAccessRequestedEvent(BaseModel):
    """
    Webhook event sent when Avara needs presigned UPLOAD URLs for a secondary capture DICOM. This is a synchronous webhook - you must respond with the upload URLs within the request timeout.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: SecondaryCaptureAccessRequestedEventData
    """
    Event payload containing study + (optional) series/SOP information for a
    secondary capture upload
    """

    type: Literal["secondary_capture.access_requested"]
    """Event type identifier"""
