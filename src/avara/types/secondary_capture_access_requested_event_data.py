# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SecondaryCaptureAccessRequestedEventData"]


class SecondaryCaptureAccessRequestedEventData(BaseModel):
    """
    Event payload containing study + (optional) series/SOP information for a secondary capture upload
    """

    study_id: str = FieldInfo(alias="studyId")
    """Avara study ID. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    series_instance_uid: Optional[str] = FieldInfo(alias="seriesInstanceUid", default=None)
    """
    DICOM Series Instance UID generated for the new secondary capture series (when
    available).
    """

    sop_instance_uid: Optional[str] = FieldInfo(alias="sopInstanceUid", default=None)
    """
    DICOM SOP Instance UID generated for the new secondary capture object (when
    available).
    """
