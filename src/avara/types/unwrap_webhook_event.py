# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .report_delivered_webhook_event import ReportDeliveredWebhookEvent
from .study_access_requested_webhook_event import StudyAccessRequestedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[StudyAccessRequestedWebhookEvent, ReportDeliveredWebhookEvent], PropertyInfo(discriminator="type")
]
