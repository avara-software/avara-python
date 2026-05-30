# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .report_delivered_event_data import ReportDeliveredEventData

__all__ = ["ReportDeliveredEvent"]


class ReportDeliveredEvent(BaseModel):
    """Webhook event sent when a report is completed.

    This is an asynchronous notification - respond with a simple acknowledgment.
    """

    id: str
    """Unique webhook event ID. Format: whe\\__{32-hex-chars}"""

    data: ReportDeliveredEventData
    """Event payload containing report and study information"""

    type: Literal["report.delivered"]
    """Event type identifier"""
