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
    """Unique report identifier. Format: rep\\__{32-hex-chars}"""

    snapshot_metadata: StudyReportMetadata = FieldInfo(alias="snapshotMetadata")
    """Patient demographics and scan information for report generation"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID this report belongs to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)
    """Plain text content of the report"""


class ListReportsTextResponseReport(BaseModel):
    """A report with its plain text content"""

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

    plain_text: Optional[str] = FieldInfo(alias="plainText", default=None)
    """Plain text content of the report"""


class ListReportsTextResponse(BaseModel):
    """Response containing a list of reports with their plain text"""

    reports: List[ListReportsTextResponseReport]
    """Array of report text items"""

    study_id: str = FieldInfo(alias="studyId")
    """Study ID the reports belong to. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: str = FieldInfo(alias="studyInstanceUid")
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """


ReportTextResponse: TypeAlias = Union[SingleReportTextResponse, ListReportsTextResponse]
