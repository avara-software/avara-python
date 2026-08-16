# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.shared.severity import Severity
from .....types.auto_scribe.studies import external_create_params, external_delete_params
from .....types.study_report_metadata_param import StudyReportMetadataParam
from .....types.auto_scribe.studies.external_create_response import ExternalCreateResponse
from .....types.auto_scribe.studies.external_delete_response import ExternalDeleteResponse

__all__ = ["ExternalResource", "AsyncExternalResource"]


class ExternalResource(SyncAPIResource):
    @cached_property
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return ExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return ExternalResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        report_metadata: StudyReportMetadataParam,
        severity: Severity,
        study_description: str,
        study_instance_uid: str,
        express_customer_id: str | Omit = omit,
        external_patient_id: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        modality: Optional[str] | Omit = omit,
        reader_name: str | Omit = omit,
        report_file_name: str | Omit = omit,
        report_file_url: str | Omit = omit,
        report_text: str | Omit = omit,
        signed_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalCreateResponse:
        """Creates an archive (external) AutoScribe study.

        Clinical context fields are not
        accepted. If no report fields are sent, no report row is created. Study create
        is all-or-nothing, including file ingest.

        Args:
          report_metadata: Patient demographics and scan information for report generation

          severity: Priority level of a study. 'normal' for routine, 'high' for urgent, 'stat' for
              immediate attention.

          study_description: Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          external_patient_id: Strongly recommended if you want to leverage priors functionality for future
              reads for this patient.

          metadata: Custom key-value metadata for the study. Maximum 50 pairs, keys up to 100 chars,
              values up to 1000 chars

          reader_name: Optional original reader / author name. Shown as-is. May be set on study create
              or a later report create; a later create overwrites it when provided.

          report_file_name: File name including extension. Required when reportFileUrl is provided.
              Supported types: PDF, PNG, JPG, GIF, WEBP.

          report_file_url: HTTPS download URL for a PDF or image (PNG, JPG, GIF, WEBP). Not used for AI
              tooling; the reader can still access it. Avara fetches this URL server-side. If
              omitted, you can add it later. Once set, it cannot be edited; delete the study
              to remake it. Whitelist https://api.avarasoftware.com on the file host if the
              fetch is origin-restricted.

          report_text: When this study is used as a prior, report AI tools leverage this text directly.
              If omitted, you can add it later via POST /studies/external/reports. Once set,
              it cannot be edited; delete the study to remake it.

          signed_at: Optional original sign-off timestamp or label. Shown as-is with no format
              validation. May be set on study create or a later report create; a later create
              overwrites it when provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoScribe/studies/external",
            body=maybe_transform(
                {
                    "report_metadata": report_metadata,
                    "severity": severity,
                    "study_description": study_description,
                    "study_instance_uid": study_instance_uid,
                    "express_customer_id": express_customer_id,
                    "external_patient_id": external_patient_id,
                    "metadata": metadata,
                    "modality": modality,
                    "reader_name": reader_name,
                    "report_file_name": report_file_name,
                    "report_file_url": report_file_url,
                    "report_text": report_text,
                    "signed_at": signed_at,
                },
                external_create_params.ExternalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalCreateResponse,
        )

    def delete(
        self,
        *,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalDeleteResponse:
        """Soft-deletes an external study.

        This is one-way; POST /studies/uncancel cannot
        reverse it.

        Args:
          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoScribe/studies/external/delete",
            body=maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                external_delete_params.ExternalDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalDeleteResponse,
        )


class AsyncExternalResource(AsyncAPIResource):
    @cached_property
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncExternalResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        report_metadata: StudyReportMetadataParam,
        severity: Severity,
        study_description: str,
        study_instance_uid: str,
        express_customer_id: str | Omit = omit,
        external_patient_id: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        modality: Optional[str] | Omit = omit,
        reader_name: str | Omit = omit,
        report_file_name: str | Omit = omit,
        report_file_url: str | Omit = omit,
        report_text: str | Omit = omit,
        signed_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalCreateResponse:
        """Creates an archive (external) AutoScribe study.

        Clinical context fields are not
        accepted. If no report fields are sent, no report row is created. Study create
        is all-or-nothing, including file ingest.

        Args:
          report_metadata: Patient demographics and scan information for report generation

          severity: Priority level of a study. 'normal' for routine, 'high' for urgent, 'stat' for
              immediate attention.

          study_description: Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          external_patient_id: Strongly recommended if you want to leverage priors functionality for future
              reads for this patient.

          metadata: Custom key-value metadata for the study. Maximum 50 pairs, keys up to 100 chars,
              values up to 1000 chars

          reader_name: Optional original reader / author name. Shown as-is. May be set on study create
              or a later report create; a later create overwrites it when provided.

          report_file_name: File name including extension. Required when reportFileUrl is provided.
              Supported types: PDF, PNG, JPG, GIF, WEBP.

          report_file_url: HTTPS download URL for a PDF or image (PNG, JPG, GIF, WEBP). Not used for AI
              tooling; the reader can still access it. Avara fetches this URL server-side. If
              omitted, you can add it later. Once set, it cannot be edited; delete the study
              to remake it. Whitelist https://api.avarasoftware.com on the file host if the
              fetch is origin-restricted.

          report_text: When this study is used as a prior, report AI tools leverage this text directly.
              If omitted, you can add it later via POST /studies/external/reports. Once set,
              it cannot be edited; delete the study to remake it.

          signed_at: Optional original sign-off timestamp or label. Shown as-is with no format
              validation. May be set on study create or a later report create; a later create
              overwrites it when provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoScribe/studies/external",
            body=await async_maybe_transform(
                {
                    "report_metadata": report_metadata,
                    "severity": severity,
                    "study_description": study_description,
                    "study_instance_uid": study_instance_uid,
                    "express_customer_id": express_customer_id,
                    "external_patient_id": external_patient_id,
                    "metadata": metadata,
                    "modality": modality,
                    "reader_name": reader_name,
                    "report_file_name": report_file_name,
                    "report_file_url": report_file_url,
                    "report_text": report_text,
                    "signed_at": signed_at,
                },
                external_create_params.ExternalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalCreateResponse,
        )

    async def delete(
        self,
        *,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalDeleteResponse:
        """Soft-deletes an external study.

        This is one-way; POST /studies/uncancel cannot
        reverse it.

        Args:
          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoScribe/studies/external/delete",
            body=await async_maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                external_delete_params.ExternalDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalDeleteResponse,
        )


class ExternalResourceWithRawResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.create = to_raw_response_wrapper(
            external.create,
        )
        self.delete = to_raw_response_wrapper(
            external.delete,
        )

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._external.reports)


class AsyncExternalResourceWithRawResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.create = async_to_raw_response_wrapper(
            external.create,
        )
        self.delete = async_to_raw_response_wrapper(
            external.delete,
        )

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._external.reports)


class ExternalResourceWithStreamingResponse:
    def __init__(self, external: ExternalResource) -> None:
        self._external = external

        self.create = to_streamed_response_wrapper(
            external.create,
        )
        self.delete = to_streamed_response_wrapper(
            external.delete,
        )

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._external.reports)


class AsyncExternalResourceWithStreamingResponse:
    def __init__(self, external: AsyncExternalResource) -> None:
        self._external = external

        self.create = async_to_streamed_response_wrapper(
            external.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            external.delete,
        )

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._external.reports)
