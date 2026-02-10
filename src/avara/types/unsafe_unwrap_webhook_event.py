# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .report_delivered_event import ReportDeliveredEvent
from .study_access_requested_event import StudyAccessRequestedEvent

__all__ = ["UnsafeUnwrapWebhookEvent"]

UnsafeUnwrapWebhookEvent: TypeAlias = Annotated[
    Union[StudyAccessRequestedEvent, ReportDeliveredEvent], PropertyInfo(discriminator="type")
]
