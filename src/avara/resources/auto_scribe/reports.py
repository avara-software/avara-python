# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.auto_scribe import report_pdf_params, report_list_params, report_text_params
from ...types.auto_scribe.report_pdf_response import ReportPdfResponse
from ...types.auto_scribe.report_list_response import ReportListResponse
from ...types.auto_scribe.report_text_response import ReportTextResponse
from ...types.auto_scribe.report_addendum_response import ReportAddendumResponse
from ...types.auto_scribe.report_cancel_addendum_response import ReportCancelAddendumResponse

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

    def list(
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
    ) -> ReportListResponse:
        """
        Retrieves all reports (including versions and addendums) for a specific study.
        Must provide either study ID or DICOM Study Instance UID. Returns report
        metadata including status, version, and timestamps.

        Args:
          study_instance_uid: DICOM Study Instance UID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/autoScribe/reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "study_id": study_id,
                        "study_instance_uid": study_instance_uid,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            cast_to=ReportListResponse,
        )

    def addendum(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportAddendumResponse:
        """Initiates the creation of an addendum to an existing completed report.

        The study
        status will change to 'addendum_active' allowing the radiologist to dictate
        additional findings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._post(
            f"/v1/autoScribe/reports/{report_id}/addendum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportAddendumResponse,
        )

    def cancel_addendum(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCancelAddendumResponse:
        """Cancels an in-progress addendum and reverts the study status to 'completed'.

        The
        original report remains unchanged. Only valid for active addendums.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._post(
            f"/v1/autoScribe/reports/{report_id}/cancel-addendum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCancelAddendumResponse,
        )

    def pdf(
        self,
        *,
        report_id: str | Omit = omit,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportPdfResponse:
        """Retrieves presigned URLs for accessing report PDFs.

        Can fetch a single report by
        report ID, or all reports for a study by study ID/DICOM UID. URLs are
        time-limited for security.

        Args:
          study_instance_uid: DICOM Study Instance UID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ReportPdfResponse,
            self._get(
                "/v1/autoScribe/reports/pdf",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "report_id": report_id,
                            "study_id": study_id,
                            "study_instance_uid": study_instance_uid,
                        },
                        report_pdf_params.ReportPdfParams,
                    ),
                ),
                cast_to=cast(Any, ReportPdfResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def text(
        self,
        *,
        report_id: str | Omit = omit,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportTextResponse:
        """Retrieves the text content of a report.

        Can fetch a single report by report ID,
        or all reports for a study by study ID/DICOM UID. Returns plain text report
        content.

        Args:
          study_instance_uid: DICOM Study Instance UID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ReportTextResponse,
            self._get(
                "/v1/autoScribe/reports/text",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "report_id": report_id,
                            "study_id": study_id,
                            "study_instance_uid": study_instance_uid,
                        },
                        report_text_params.ReportTextParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReportTextResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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

    async def list(
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
    ) -> ReportListResponse:
        """
        Retrieves all reports (including versions and addendums) for a specific study.
        Must provide either study ID or DICOM Study Instance UID. Returns report
        metadata including status, version, and timestamps.

        Args:
          study_instance_uid: DICOM Study Instance UID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/autoScribe/reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "study_id": study_id,
                        "study_instance_uid": study_instance_uid,
                    },
                    report_list_params.ReportListParams,
                ),
            ),
            cast_to=ReportListResponse,
        )

    async def addendum(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportAddendumResponse:
        """Initiates the creation of an addendum to an existing completed report.

        The study
        status will change to 'addendum_active' allowing the radiologist to dictate
        additional findings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._post(
            f"/v1/autoScribe/reports/{report_id}/addendum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportAddendumResponse,
        )

    async def cancel_addendum(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportCancelAddendumResponse:
        """Cancels an in-progress addendum and reverts the study status to 'completed'.

        The
        original report remains unchanged. Only valid for active addendums.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._post(
            f"/v1/autoScribe/reports/{report_id}/cancel-addendum",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportCancelAddendumResponse,
        )

    async def pdf(
        self,
        *,
        report_id: str | Omit = omit,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportPdfResponse:
        """Retrieves presigned URLs for accessing report PDFs.

        Can fetch a single report by
        report ID, or all reports for a study by study ID/DICOM UID. URLs are
        time-limited for security.

        Args:
          study_instance_uid: DICOM Study Instance UID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ReportPdfResponse,
            await self._get(
                "/v1/autoScribe/reports/pdf",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "report_id": report_id,
                            "study_id": study_id,
                            "study_instance_uid": study_instance_uid,
                        },
                        report_pdf_params.ReportPdfParams,
                    ),
                ),
                cast_to=cast(Any, ReportPdfResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def text(
        self,
        *,
        report_id: str | Omit = omit,
        study_id: str | Omit = omit,
        study_instance_uid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportTextResponse:
        """Retrieves the text content of a report.

        Can fetch a single report by report ID,
        or all reports for a study by study ID/DICOM UID. Returns plain text report
        content.

        Args:
          study_instance_uid: DICOM Study Instance UID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ReportTextResponse,
            await self._get(
                "/v1/autoScribe/reports/text",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "report_id": report_id,
                            "study_id": study_id,
                            "study_instance_uid": study_instance_uid,
                        },
                        report_text_params.ReportTextParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReportTextResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.list = to_raw_response_wrapper(
            reports.list,
        )
        self.addendum = to_raw_response_wrapper(
            reports.addendum,
        )
        self.cancel_addendum = to_raw_response_wrapper(
            reports.cancel_addendum,
        )
        self.pdf = to_raw_response_wrapper(
            reports.pdf,
        )
        self.text = to_raw_response_wrapper(
            reports.text,
        )


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.list = async_to_raw_response_wrapper(
            reports.list,
        )
        self.addendum = async_to_raw_response_wrapper(
            reports.addendum,
        )
        self.cancel_addendum = async_to_raw_response_wrapper(
            reports.cancel_addendum,
        )
        self.pdf = async_to_raw_response_wrapper(
            reports.pdf,
        )
        self.text = async_to_raw_response_wrapper(
            reports.text,
        )


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.list = to_streamed_response_wrapper(
            reports.list,
        )
        self.addendum = to_streamed_response_wrapper(
            reports.addendum,
        )
        self.cancel_addendum = to_streamed_response_wrapper(
            reports.cancel_addendum,
        )
        self.pdf = to_streamed_response_wrapper(
            reports.pdf,
        )
        self.text = to_streamed_response_wrapper(
            reports.text,
        )


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.list = async_to_streamed_response_wrapper(
            reports.list,
        )
        self.addendum = async_to_streamed_response_wrapper(
            reports.addendum,
        )
        self.cancel_addendum = async_to_streamed_response_wrapper(
            reports.cancel_addendum,
        )
        self.pdf = async_to_streamed_response_wrapper(
            reports.pdf,
        )
        self.text = async_to_streamed_response_wrapper(
            reports.text,
        )
