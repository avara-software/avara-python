# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModalityWorklistRequestedEventData"]


class ModalityWorklistRequestedEventData(BaseModel):
    """Event payload for a modality worklist (C-FIND MWL) request"""

    calling_ae: str = FieldInfo(alias="callingAe")
    """Calling AE title from the modality"""

    clinic_id: str = FieldInfo(alias="clinicId")
    """Clinic UUID that owns the modality / worklist query"""

    date_end: str = FieldInfo(alias="dateEnd")
    """Inclusive worklist window end date (YYYY-MM-DD)"""

    date_start: str = FieldInfo(alias="dateStart")
    """Inclusive worklist window start date (YYYY-MM-DD)"""

    source_ip: str = FieldInfo(alias="sourceIp")
    """Source IP observed by Avara for the modality request"""

    modality: Optional[str] = None
    """Present when the modality C-FIND included a modality filter"""
