# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncCursorExternalReports, AsyncCursorExternalReports
from ....._base_client import AsyncPaginator, make_request_options
from .....types.auto_scribe.studies.external import report_list_params, report_create_params
from .....types.auto_scribe.studies.external.report_list_response import ReportListResponse
from .....types.auto_scribe.studies.external.report_create_response import ReportCreateResponse
from .....types.auto_scribe.studies.external.report_retrieve_response import ReportRetrieveResponse

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        reader_name: str | Omit = omit,
        report_file_name: str | Omit = omit,
        report_file_url: str | Omit = omit,
        report_text: str | Omit = omit,
        signed_at: str | Omit = omit,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCreateResponse:
        """Attach or fill missing report fields on an existing external study.

        Text and
        file are write-once. readerName and signedAt overwrite when provided.

        Args:
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

          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoScribe/studies/external/reports",
            body=maybe_transform(
                {
                    "reader_name": reader_name,
                    "report_file_name": report_file_name,
                    "report_file_url": report_file_url,
                    "report_text": report_text,
                    "signed_at": signed_at,
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                report_create_params.ReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCreateResponse,
        )

    def retrieve(
        self,
        external_report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportRetrieveResponse:
        """
        Returns snapshot metadata plus report text and/or a short-lived download URL.
        Text is what AI priors use; the file is reader-only and is not used for AI.

        Args:
          external_report_id: External report identifier. Format: ext\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_report_id:
            raise ValueError(f"Expected a non-empty value for `external_report_id` but received {external_report_id!r}")
        return self._get(
            path_template(
                "/v1/autoScribe/studies/external/reports/{external_report_id}", external_report_id=external_report_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        study_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorExternalReports[ReportListResponse]:
        """Cursor-paginated list of external reports.

        List items omit report text and
        download URLs.

        Args:
          cursor: Base64 encoded cursor from previous response

          limit: Number of results to return (1-100)

          study_id: Filter to one study. Format: stu\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/autoScribe/studies/external/reports",
            page=SyncCursorExternalReports[ReportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "study_id": study_id,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=ReportListResponse,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        reader_name: str | Omit = omit,
        report_file_name: str | Omit = omit,
        report_file_url: str | Omit = omit,
        report_text: str | Omit = omit,
        signed_at: str | Omit = omit,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCreateResponse:
        """Attach or fill missing report fields on an existing external study.

        Text and
        file are write-once. readerName and signedAt overwrite when provided.

        Args:
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

          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoScribe/studies/external/reports",
            body=await async_maybe_transform(
                {
                    "reader_name": reader_name,
                    "report_file_name": report_file_name,
                    "report_file_url": report_file_url,
                    "report_text": report_text,
                    "signed_at": signed_at,
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                report_create_params.ReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCreateResponse,
        )

    async def retrieve(
        self,
        external_report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportRetrieveResponse:
        """
        Returns snapshot metadata plus report text and/or a short-lived download URL.
        Text is what AI priors use; the file is reader-only and is not used for AI.

        Args:
          external_report_id: External report identifier. Format: ext\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_report_id:
            raise ValueError(f"Expected a non-empty value for `external_report_id` but received {external_report_id!r}")
        return await self._get(
            path_template(
                "/v1/autoScribe/studies/external/reports/{external_report_id}", external_report_id=external_report_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        study_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReportListResponse, AsyncCursorExternalReports[ReportListResponse]]:
        """Cursor-paginated list of external reports.

        List items omit report text and
        download URLs.

        Args:
          cursor: Base64 encoded cursor from previous response

          limit: Number of results to return (1-100)

          study_id: Filter to one study. Format: stu\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/autoScribe/studies/external/reports",
            page=AsyncCursorExternalReports[ReportListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "study_id": study_id,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            model=ReportListResponse,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.create = to_raw_response_wrapper(
            reports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            reports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            reports.list,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.create = async_to_raw_response_wrapper(
            reports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            reports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            reports.list,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.create = to_streamed_response_wrapper(
            reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            reports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            reports.list,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.create = async_to_streamed_response_wrapper(
            reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            reports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            reports.list,
        )
