# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .patient_study_enrichment_requested_event_data import PatientStudyEnrichmentRequestedEventData

__all__ = ["PatientStudyEnrichmentRequestedEvent"]


class PatientStudyEnrichmentRequestedEvent(BaseModel):
    """
    Soft synchronous webhook sent after Avara PACS seeds a study so the partner can enrich demographics and report headers. Failures / timeouts / invalid bodies are treated as empty enrichment.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: PatientStudyEnrichmentRequestedEventData
    """Event payload for soft patient/study enrichment after Avara PACS seeds a study"""

    type: Literal["patient_study.enrichment_requested"]
    """Event type identifier"""
