# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.ephemeral_hanging_protocol import EphemeralHangingProtocol

__all__ = ["EphemeralSessionCreateParams"]


class EphemeralSessionCreateParams(TypedDict, total=False):
    retrieval_id: Required[Annotated[str, PropertyInfo(alias="retrievalId")]]
    """Opaque customer handle for this view session.

    Avara stores and echoes it; it is not an Avara study ID.
    """

    hanging_protocol: Annotated[EphemeralHangingProtocol, PropertyInfo(alias="hangingProtocol")]
    """Optional single-monitor hanging protocol applied when the ephemeral viewer
    loads.

    Omitted = no protocol. Invalid shape is rejected.
    """

    options: Dict[str, object]
    """Optional JSON object echoed verbatim on ephemeral.access_requested.

    Avara does not read or edit it. Hard cap 3072 bytes on JSON.stringify. Examples:
    studyInstanceUids or internal ids for multi-study reads. Not for URLs or
    manifests.
    """
