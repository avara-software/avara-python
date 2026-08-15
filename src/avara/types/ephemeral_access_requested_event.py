# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ephemeral_access_requested_event_data import EphemeralAccessRequestedEventData

__all__ = ["EphemeralAccessRequestedEvent"]


class EphemeralAccessRequestedEvent(BaseModel):
    """
    Webhook event sent when Avara needs presigned URLs for an ephemeral viewer session. This is a synchronous webhook — you must respond with the URLs within the request timeout. There is no Avara study; use retrievalId (and optional options) to resolve images.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: EphemeralAccessRequestedEventData
    """Event payload for an ephemeral viewer session.

    retrievalId is the customer handle from mint. options is echoed verbatim when
    present; Avara does not read or edit it.
    """

    type: Literal["ephemeral.access_requested"]
    """Event type identifier"""
