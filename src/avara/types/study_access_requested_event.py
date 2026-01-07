# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StudyAccessRequestedEvent", "Data"]


class Data(BaseModel):
    """Event payload containing study information"""

    study_id: str = FieldInfo(alias="studyId")
    """Avara study ID. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """


class StudyAccessRequestedEvent(BaseModel):
    """Webhook event sent when Avara needs presigned URLs for DICOM images.

    This is a synchronous webhook - you must respond with the URLs within the request timeout.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: Data
    """Event payload containing study information"""

    type: Literal["study.access_requested"]
    """Event type identifier"""
