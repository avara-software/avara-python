# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .modality_worklist_requested_event_data import ModalityWorklistRequestedEventData

__all__ = ["ModalityWorklistRequestedEvent"]


class ModalityWorklistRequestedEvent(BaseModel):
    """Webhook event sent when an on-prem modality issues a C-FIND MWL.

    This is a synchronous webhook - you must respond with authorized + items within the request timeout.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: ModalityWorklistRequestedEventData
    """Event payload for a modality worklist (C-FIND MWL) request"""

    type: Literal["modality_worklist.requested"]
    """Event type identifier"""
