# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .report_delivered_event import ReportDeliveredEvent
from .study_access_requested_event import StudyAccessRequestedEvent
from .modality_worklist_requested_event import ModalityWorklistRequestedEvent
from .patient_study_enrichment_requested_event import PatientStudyEnrichmentRequestedEvent
from .secondary_capture_access_requested_event import SecondaryCaptureAccessRequestedEvent
from .clinical_context_enrichment_requested_event import ClinicalContextEnrichmentRequestedEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        StudyAccessRequestedEvent,
        ReportDeliveredEvent,
        SecondaryCaptureAccessRequestedEvent,
        ModalityWorklistRequestedEvent,
        PatientStudyEnrichmentRequestedEvent,
        ClinicalContextEnrichmentRequestedEvent,
    ],
    PropertyInfo(discriminator="type"),
]
