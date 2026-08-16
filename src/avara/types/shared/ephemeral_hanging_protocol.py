# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .viewer_layout import ViewerLayout

__all__ = ["EphemeralHangingProtocol"]


class EphemeralHangingProtocol(BaseModel):
    """Optional single-monitor hanging protocol applied when the ephemeral viewer loads.

    Omitted = no protocol. Invalid shape is rejected.
    """

    layout: ViewerLayout
    """Viewport grid layout for an ephemeral hanging protocol.

    Wire values match first-party viewer layouts ('1x1' through '4x4').
    """

    viewport_assignments: List[Optional[str]] = FieldInfo(alias="viewportAssignments")
