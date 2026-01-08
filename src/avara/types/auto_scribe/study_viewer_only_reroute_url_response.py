# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["StudyViewerOnlyRerouteURLResponse"]


class StudyViewerOnlyRerouteURLResponse(BaseModel):
    """Response containing the generated viewer-only reroute URL.

    Requires viewer to be configured.
    """

    url: str
