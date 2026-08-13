# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PatientStudyEnrichmentRequestedEventData"]


class PatientStudyEnrichmentRequestedEventData(BaseModel):
    """Event payload for soft patient/study enrichment after Avara PACS seeds a study"""

    clinic_id: str = FieldInfo(alias="clinicId")
    """Clinic UUID"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID"""

    accession_number: Optional[str] = FieldInfo(alias="accessionNumber", default=None)
    """Accession number from DICOM when available"""

    patient_id: Optional[str] = FieldInfo(alias="patientId", default=None)
    """Patient ID from DICOM when available"""
