# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    reader_name: Annotated[str, PropertyInfo(alias="readerName")]
    """Optional original reader / author name.

    Shown as-is. May be set on study create or a later report create; a later create
    overwrites it when provided.
    """

    report_file_name: Annotated[str, PropertyInfo(alias="reportFileName")]
    """File name including extension.

    Required when reportFileUrl is provided. Supported types: PDF, PNG, JPG, GIF,
    WEBP.
    """

    report_file_url: Annotated[str, PropertyInfo(alias="reportFileUrl")]
    """HTTPS download URL for a PDF or image (PNG, JPG, GIF, WEBP).

    Not used for AI tooling; the reader can still access it. Avara fetches this URL
    server-side. If omitted, you can add it later. Once set, it cannot be edited;
    delete the study to remake it. Whitelist https://api.avarasoftware.com on the
    file host if the fetch is origin-restricted.
    """

    report_text: Annotated[str, PropertyInfo(alias="reportText")]
    """When this study is used as a prior, report AI tools leverage this text directly.

    If omitted, you can add it later via POST /studies/external/reports. Once set,
    it cannot be edited; delete the study to remake it.
    """

    signed_at: Annotated[str, PropertyInfo(alias="signedAt")]
    """Optional original sign-off timestamp or label.

    Shown as-is with no format validation. May be set on study create or a later
    report create; a later create overwrites it when provided.
    """

    study_id: Annotated[str, PropertyInfo(alias="studyId")]
    """Unique study identifier. Format: stu\\__{32-hex-chars}"""

    study_instance_uid: Annotated[str, PropertyInfo(alias="studyInstanceUid")]
    """DICOM Study Instance UID.

    Must be a valid DICOM UID format (e.g., '1.2.840.10008.5.1.4.1.1.2')
    """
