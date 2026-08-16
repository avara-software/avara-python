# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared.viewer_layout import ViewerLayout

__all__ = ["EphemeralHangingProtocol"]


class EphemeralHangingProtocol(TypedDict, total=False):
    """Optional single-monitor hanging protocol applied when the ephemeral viewer loads.

    Omitted = no protocol. Invalid shape is rejected.
    """

    layout: Required[ViewerLayout]
    """Viewport grid layout for an ephemeral hanging protocol.

    Wire values match first-party viewer layouts ('1x1' through '4x4').
    """

    viewport_assignments: Required[Annotated[SequenceNotStr[Optional[str]], PropertyInfo(alias="viewportAssignments")]]
