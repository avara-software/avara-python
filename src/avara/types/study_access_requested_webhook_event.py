# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StudyAccessRequestedWebhookEvent", "Data"]


class Data(BaseModel):
    study_id: str = FieldInfo(alias="studyId")
    """Avara study ID (e.g., stu_1234567890abcdef1234567890abcdef)"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID"""


class StudyAccessRequestedWebhookEvent(BaseModel):
    id: str
    """Unique webhook event ID (e.g., whe_1234567890abcdef1234567890abcdef)"""

    data: Data

    type: Literal["study.access_requested"]
