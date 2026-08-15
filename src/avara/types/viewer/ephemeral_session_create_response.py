# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EphemeralSessionCreateResponse"]


class EphemeralSessionCreateResponse(BaseModel):
    """Tokenized landing URL for an ephemeral Viewer session (30-second token)."""

    url: str
