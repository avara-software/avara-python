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
    """Time-limited presigned URL to download the PDF (expires after 1 hour)"""

    report_id: str = FieldInfo(alias="reportId")
    """Unique report identifier. Format: rep\\__{32-hex-chars}"""

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Patient demographics and scan information for report generation"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID this report belongs to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """


class ListReportsPdfResponseReport(BaseModel):
    """A report with its PDF download URL"""

    presigned_url: str = FieldInfo(alias="presignedUrl")
    """Time-limited presigned URL to download the PDF (expires after 1 hour)"""

    report_id: str = FieldInfo(alias="reportId")
    """Unique report identifier. Format: rep\\__{32-hex-chars}"""

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Patient demographics and scan information for report generation"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID this report belongs to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """


class ListReportsPdfResponse(BaseModel):
    """Response containing a list of reports with their PDF download URLs"""

    reports: List[ListReportsPdfResponseReport]
    """Array of report PDF items with download URLs"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID the reports belong to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """


ReportPdfResponse: TypeAlias = Union[SingleReportPdfResponse, ListReportsPdfResponse]
