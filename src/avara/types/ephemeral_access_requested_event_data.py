# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EphemeralAccessRequestedEventData"]


class EphemeralAccessRequestedEventData(BaseModel):
    """Event payload for an ephemeral viewer session.

    retrievalId is the customer handle from mint. options is echoed verbatim when present; Avara does not read or edit it.
    """

    retrieval_id: str = FieldInfo(alias="retrievalId")
    """Opaque customer handle for this view session. Not an Avara study ID."""

    options: Optional[Dict[str, object]] = None
    """Optional JSON object echoed verbatim from mint.

    Avara does not read or edit it. Examples: studyInstanceUids or internal ids for
    multi-study reads. Not for URLs or manifests.
    """
