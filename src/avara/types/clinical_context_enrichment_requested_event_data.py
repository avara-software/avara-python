# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ClinicalContextEnrichmentRequestedEventData"]


class ClinicalContextEnrichmentRequestedEventData(BaseModel):
    """
    Event payload for soft clinical context enrichment when AutoScribe needs EHR context for a study
    """

    clinic_id: str = FieldInfo(alias="clinicId")
    """Clinic UUID"""

    study_id: str = FieldInfo(alias="studyId")
    """Raw study UUID v4 (not branded stu\\__…)"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID"""

    external_patient_id: Optional[str] = FieldInfo(alias="externalPatientId", default=None)
    """External patient identifier when available"""

    mrn: Optional[str] = None
    """Medical record number when available"""
