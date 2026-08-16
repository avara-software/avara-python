# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ReportCreateResponse"]


class ReportCreateResponse(BaseModel):
    """Created or updated external report identifiers"""

    external_report_id: str = FieldInfo(alias="externalReportId")

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
