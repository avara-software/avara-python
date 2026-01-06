# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..study_report_metadata import StudyReportMetadata

__all__ = ["ReportTextResponse", "SingleReportTextResponse", "ListReportsTextResponse", "ListReportsTextResponseReport"]


class SingleReportTextResponse(BaseModel):
    """Response containing a single report with its plain text"""

    report_id: str = FieldInfo(alias="reportId")

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Metadata for a study report including patient demographics and scan information"""

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)


class ListReportsTextResponseReport(BaseModel):
    """A report with its plain text content"""

    report_id: str = FieldInfo(alias="reportId")

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Metadata for a study report including patient demographics and scan information"""

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)


class ListReportsTextResponse(BaseModel):
    """Response containing a list of reports with their plain text"""

    reports: List[ListReportsTextResponseReport]

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")


ReportTextResponse: TypeAlias = Union[SingleReportTextResponse, ListReportsTextResponse]
