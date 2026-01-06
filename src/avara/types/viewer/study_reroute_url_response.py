# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["StudyRerouteURLResponse"]


class StudyRerouteURLResponse(BaseModel):
    """Response containing the generated reroute URL for a study in Viewer"""

    url: str
