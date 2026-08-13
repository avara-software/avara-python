# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .clinical_context_enrichment_requested_event_data import ClinicalContextEnrichmentRequestedEventData

__all__ = ["ClinicalContextEnrichmentRequestedEvent"]


class ClinicalContextEnrichmentRequestedEvent(BaseModel):
    """
    Soft synchronous webhook sent when AutoScribe needs clinical context from the partner EHR. Failures / timeouts / invalid bodies are treated as empty enrichment.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: ClinicalContextEnrichmentRequestedEventData
    """
    Event payload for soft clinical context enrichment when AutoScribe needs EHR
    context for a study
    """

    type: Literal["clinical_context.enrichment_requested"]
    """Event type identifier"""
