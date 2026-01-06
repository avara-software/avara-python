# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..study_report_metadata import StudyReportMetadata

__all__ = ["ReportPdfResponse", "SingleReportPdfResponse", "ListReportsPdfResponse", "ListReportsPdfResponseReport"]


class SingleReportPdfResponse(BaseModel):
    """Response containing a single report with its PDF download URL"""

    presigned_url: str = FieldInfo(alias="presignedUrl")

    report_id: str = FieldInfo(alias="reportId")

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Metadata for a study report including patient demographics and scan information"""

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")


class ListReportsPdfResponseReport(BaseModel):
    """A report with its PDF download URL"""

    presigned_url: str = FieldInfo(alias="presignedUrl")

    report_id: str = FieldInfo(alias="reportId")

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Metadata for a study report including patient demographics and scan information"""

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")


class ListReportsPdfResponse(BaseModel):
    """Response containing a list of reports with their PDF download URLs"""

    reports: List[ListReportsPdfResponseReport]

    study_id: str = FieldInfo(alias="studyId")

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")


ReportPdfResponse: TypeAlias = Union[SingleReportPdfResponse, ListReportsPdfResponse]
