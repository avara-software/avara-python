# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorStudies, AsyncCursorStudies
from ..._base_client import AsyncPaginator, make_request_options
from ...types.viewer import (
    study_list_params,
    study_cancel_params,
    study_create_params,
    study_update_params,
    study_uncancel_params,
    study_reroute_url_params,
)
from ...types.viewer.study_list_response import StudyListResponse
from ...types.viewer.study_cancel_response import StudyCancelResponse
from ...types.viewer.study_create_response import StudyCreateResponse
from ...types.viewer.study_update_response import StudyUpdateResponse
from ...types.viewer.study_retrieve_response import StudyRetrieveResponse
from ...types.viewer.study_uncancel_response import StudyUncancelResponse
from ...types.viewer.study_reroute_url_response import StudyRerouteURLResponse
from ...types.viewer.study_retrieve_by_uid_response import StudyRetrieveByUidResponse

__all__ = ["StudiesResource", "AsyncStudiesResource"]


class StudiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StudiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return StudiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StudiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return StudiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        severity: Literal["normal", "high", "stat"],
        study_description: str,
        study_instance_uid: str,
        assigned_to: str | Omit = omit,
        express_customer_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyCreateResponse:
        """
        Creates a new study in the Viewer system with the specified DICOM Study Instance
        UID and metadata. The study can be optionally assigned to a user.

        Args:
          severity: Priority level of the study. 'normal' for routine, 'high' for urgent, 'stat' for
              immediate attention

          study_description: Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          assigned_to: User ID to assign the study to. Format: usr\\__{32-hex-chars}

          express_customer_id: Express customer ID for the study. Format: cus\\__{32-hex-chars}

          metadata: Custom key-value metadata for the study. Maximum 50 pairs, keys up to 100 chars,
              values up to 1000 chars

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/viewer/studies",
            body=maybe_transform(
                {
                    "severity": severity,
                    "study_description": study_description,
                    "study_instance_uid": study_instance_uid,
                    "assigned_to": assigned_to,
                    "express_customer_id": express_customer_id,
                    "metadata": metadata,
                },
                study_create_params.StudyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyCreateResponse,
        )

    def retrieve(
        self,
        study_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyRetrieveResponse:
        """Retrieves a single study by its unique study ID.

        Returns the complete study
        object with all metadata and status information.

        Args:
          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not study_id:
            raise ValueError(f"Expected a non-empty value for `study_id` but received {study_id!r}")
        return self._get(
            path_template("/v1/viewer/studies/{study_id}", study_id=study_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyRetrieveResponse,
        )

    def update(
        self,
        study_id: str,
        *,
        assigned_to: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        severity: Literal["normal", "high", "stat"] | Omit = omit,
        study_description: str | Omit = omit,
        study_viewer_status: Literal["incomplete", "complete"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyUpdateResponse:
        """
        Updates a study's properties including description, severity, assignment,
        organization, and metadata. All fields are optional - only provided fields will
        be updated.

        Args:
          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          assigned_to: User ID to assign the study to, or null to unassign. Format: usr\\__{32-hex-chars}

          severity: Priority level of the study. 'normal' for routine, 'high' for urgent, 'stat' for
              immediate attention

          study_description: Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not study_id:
            raise ValueError(f"Expected a non-empty value for `study_id` but received {study_id!r}")
        return self._patch(
            path_template("/v1/viewer/studies/{study_id}", study_id=study_id),
            body=maybe_transform(
                {
                    "assigned_to": assigned_to,
                    "metadata": metadata,
                    "severity": severity,
                    "study_description": study_description,
                    "study_viewer_status": study_viewer_status,
                },
                study_update_params.StudyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyUpdateResponse,
        )

    def list(
        self,
        *,
        assigned_to: Optional[str] | Omit = omit,
        cursor: str | Omit = omit,
        express_customer_id: Optional[str] | Omit = omit,
        is_cancelled: Optional[bool] | Omit = omit,
        limit: float | Omit = omit,
        severity: Literal["normal", "high", "stat"] | Omit = omit,
        study_description: str | Omit = omit,
        study_viewer_status: Literal["incomplete", "complete"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorStudies[StudyListResponse]:
        """
        Retrieves a paginated list of studies with optional filtering by assignment,
        severity, description, cancellation status, and viewer status. Returns up to 100
        studies per request.

        Args:
          assigned_to:
              Filter by assigned user ID (null = explicitly unassigned). Format:
              usr\\__<32-hex-chars>

          cursor: Base64 encoded cursor from previous response

          express_customer_id:
              Filter by Express customer ID (null = studies with no customer). Format:
              cus\\__{32-hex-chars}

          is_cancelled: Filter by cancellation status

          limit: Number of results to return (1-100)

          severity: Filter by study severity

          study_description: Filter by study description (contains match)

          study_viewer_status: Filter by study viewer status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/viewer/studies",
            page=SyncCursorStudies[StudyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assigned_to": assigned_to,
                        "cursor": cursor,
                        "express_customer_id": express_customer_id,
                        "is_cancelled": is_cancelled,
                        "limit": limit,
                        "severity": severity,
                        "study_description": study_description,
                        "study_viewer_status": study_viewer_status,
                    },
                    study_list_params.StudyListParams,
                ),
            ),
            model=StudyListResponse,
        )

    def cancel(
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
    ) -> StudyCancelResponse:
        """Marks a study as cancelled.

        Cancelled studies are preserved but flagged as
        inactive. Can be identified by either study ID or DICOM Study Instance UID.

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
            "/v1/viewer/studies/cancel",
            body=maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                study_cancel_params.StudyCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyCancelResponse,
        )

    def reroute_url(
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
    ) -> StudyRerouteURLResponse:
        """
        Generates a tokenized URL that redirects users directly to the Avara Viewer for
        the specified study. The URL includes authentication and is time-limited for
        security.

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
            "/v1/viewer/studies/reroute-url",
            body=maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                study_reroute_url_params.StudyRerouteURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyRerouteURLResponse,
        )

    def retrieve_by_uid(
        self,
        study_instance_uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyRetrieveByUidResponse:
        """Retrieves a single study by its DICOM Study Instance UID.

        This is useful when
        you have the DICOM UID but not the Avara study ID.

        Args:
          study_instance_uid: DICOM Study Instance UID. Format: numbers and dots (e.g.,
              1.2.840.10008.5.1.4.1.1.2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not study_instance_uid:
            raise ValueError(f"Expected a non-empty value for `study_instance_uid` but received {study_instance_uid!r}")
        return self._get(
            path_template("/v1/viewer/studies/by-uid/{study_instance_uid}", study_instance_uid=study_instance_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyRetrieveByUidResponse,
        )

    def uncancel(
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
    ) -> StudyUncancelResponse:
        """Restores a cancelled study to active status.

        The study must have been previously
        cancelled. Can be identified by either study ID or DICOM Study Instance UID.

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
            "/v1/viewer/studies/uncancel",
            body=maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                study_uncancel_params.StudyUncancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyUncancelResponse,
        )


class AsyncStudiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStudiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStudiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStudiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncStudiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        severity: Literal["normal", "high", "stat"],
        study_description: str,
        study_instance_uid: str,
        assigned_to: str | Omit = omit,
        express_customer_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyCreateResponse:
        """
        Creates a new study in the Viewer system with the specified DICOM Study Instance
        UID and metadata. The study can be optionally assigned to a user.

        Args:
          severity: Priority level of the study. 'normal' for routine, 'high' for urgent, 'stat' for
              immediate attention

          study_description: Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')

          study_instance_uid: DICOM Study Instance UID. Must be a valid DICOM UID format (e.g.,
              '1.2.840.10008.5.1.4.1.1.2')

          assigned_to: User ID to assign the study to. Format: usr\\__{32-hex-chars}

          express_customer_id: Express customer ID for the study. Format: cus\\__{32-hex-chars}

          metadata: Custom key-value metadata for the study. Maximum 50 pairs, keys up to 100 chars,
              values up to 1000 chars

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/viewer/studies",
            body=await async_maybe_transform(
                {
                    "severity": severity,
                    "study_description": study_description,
                    "study_instance_uid": study_instance_uid,
                    "assigned_to": assigned_to,
                    "express_customer_id": express_customer_id,
                    "metadata": metadata,
                },
                study_create_params.StudyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyCreateResponse,
        )

    async def retrieve(
        self,
        study_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyRetrieveResponse:
        """Retrieves a single study by its unique study ID.

        Returns the complete study
        object with all metadata and status information.

        Args:
          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not study_id:
            raise ValueError(f"Expected a non-empty value for `study_id` but received {study_id!r}")
        return await self._get(
            path_template("/v1/viewer/studies/{study_id}", study_id=study_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyRetrieveResponse,
        )

    async def update(
        self,
        study_id: str,
        *,
        assigned_to: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        severity: Literal["normal", "high", "stat"] | Omit = omit,
        study_description: str | Omit = omit,
        study_viewer_status: Literal["incomplete", "complete"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyUpdateResponse:
        """
        Updates a study's properties including description, severity, assignment,
        organization, and metadata. All fields are optional - only provided fields will
        be updated.

        Args:
          study_id: Unique study identifier. Format: stu\\__{32-hex-chars}

          assigned_to: User ID to assign the study to, or null to unassign. Format: usr\\__{32-hex-chars}

          severity: Priority level of the study. 'normal' for routine, 'high' for urgent, 'stat' for
              immediate attention

          study_description: Description of the study/scan (e.g., 'Brain MRI with Contrast', 'Chest CT')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not study_id:
            raise ValueError(f"Expected a non-empty value for `study_id` but received {study_id!r}")
        return await self._patch(
            path_template("/v1/viewer/studies/{study_id}", study_id=study_id),
            body=await async_maybe_transform(
                {
                    "assigned_to": assigned_to,
                    "metadata": metadata,
                    "severity": severity,
                    "study_description": study_description,
                    "study_viewer_status": study_viewer_status,
                },
                study_update_params.StudyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyUpdateResponse,
        )

    def list(
        self,
        *,
        assigned_to: Optional[str] | Omit = omit,
        cursor: str | Omit = omit,
        express_customer_id: Optional[str] | Omit = omit,
        is_cancelled: Optional[bool] | Omit = omit,
        limit: float | Omit = omit,
        severity: Literal["normal", "high", "stat"] | Omit = omit,
        study_description: str | Omit = omit,
        study_viewer_status: Literal["incomplete", "complete"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[StudyListResponse, AsyncCursorStudies[StudyListResponse]]:
        """
        Retrieves a paginated list of studies with optional filtering by assignment,
        severity, description, cancellation status, and viewer status. Returns up to 100
        studies per request.

        Args:
          assigned_to:
              Filter by assigned user ID (null = explicitly unassigned). Format:
              usr\\__<32-hex-chars>

          cursor: Base64 encoded cursor from previous response

          express_customer_id:
              Filter by Express customer ID (null = studies with no customer). Format:
              cus\\__{32-hex-chars}

          is_cancelled: Filter by cancellation status

          limit: Number of results to return (1-100)

          severity: Filter by study severity

          study_description: Filter by study description (contains match)

          study_viewer_status: Filter by study viewer status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/viewer/studies",
            page=AsyncCursorStudies[StudyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assigned_to": assigned_to,
                        "cursor": cursor,
                        "express_customer_id": express_customer_id,
                        "is_cancelled": is_cancelled,
                        "limit": limit,
                        "severity": severity,
                        "study_description": study_description,
                        "study_viewer_status": study_viewer_status,
                    },
                    study_list_params.StudyListParams,
                ),
            ),
            model=StudyListResponse,
        )

    async def cancel(
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
    ) -> StudyCancelResponse:
        """Marks a study as cancelled.

        Cancelled studies are preserved but flagged as
        inactive. Can be identified by either study ID or DICOM Study Instance UID.

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
            "/v1/viewer/studies/cancel",
            body=await async_maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                study_cancel_params.StudyCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyCancelResponse,
        )

    async def reroute_url(
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
    ) -> StudyRerouteURLResponse:
        """
        Generates a tokenized URL that redirects users directly to the Avara Viewer for
        the specified study. The URL includes authentication and is time-limited for
        security.

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
            "/v1/viewer/studies/reroute-url",
            body=await async_maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                study_reroute_url_params.StudyRerouteURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyRerouteURLResponse,
        )

    async def retrieve_by_uid(
        self,
        study_instance_uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StudyRetrieveByUidResponse:
        """Retrieves a single study by its DICOM Study Instance UID.

        This is useful when
        you have the DICOM UID but not the Avara study ID.

        Args:
          study_instance_uid: DICOM Study Instance UID. Format: numbers and dots (e.g.,
              1.2.840.10008.5.1.4.1.1.2).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not study_instance_uid:
            raise ValueError(f"Expected a non-empty value for `study_instance_uid` but received {study_instance_uid!r}")
        return await self._get(
            path_template("/v1/viewer/studies/by-uid/{study_instance_uid}", study_instance_uid=study_instance_uid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyRetrieveByUidResponse,
        )

    async def uncancel(
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
    ) -> StudyUncancelResponse:
        """Restores a cancelled study to active status.

        The study must have been previously
        cancelled. Can be identified by either study ID or DICOM Study Instance UID.

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
            "/v1/viewer/studies/uncancel",
            body=await async_maybe_transform(
                {
                    "study_id": study_id,
                    "study_instance_uid": study_instance_uid,
                },
                study_uncancel_params.StudyUncancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudyUncancelResponse,
        )


class StudiesResourceWithRawResponse:
    def __init__(self, studies: StudiesResource) -> None:
        self._studies = studies

        self.create = to_raw_response_wrapper(
            studies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            studies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            studies.update,
        )
        self.list = to_raw_response_wrapper(
            studies.list,
        )
        self.cancel = to_raw_response_wrapper(
            studies.cancel,
        )
        self.reroute_url = to_raw_response_wrapper(
            studies.reroute_url,
        )
        self.retrieve_by_uid = to_raw_response_wrapper(
            studies.retrieve_by_uid,
        )
        self.uncancel = to_raw_response_wrapper(
            studies.uncancel,
        )


class AsyncStudiesResourceWithRawResponse:
    def __init__(self, studies: AsyncStudiesResource) -> None:
        self._studies = studies

        self.create = async_to_raw_response_wrapper(
            studies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            studies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            studies.update,
        )
        self.list = async_to_raw_response_wrapper(
            studies.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            studies.cancel,
        )
        self.reroute_url = async_to_raw_response_wrapper(
            studies.reroute_url,
        )
        self.retrieve_by_uid = async_to_raw_response_wrapper(
            studies.retrieve_by_uid,
        )
        self.uncancel = async_to_raw_response_wrapper(
            studies.uncancel,
        )


class StudiesResourceWithStreamingResponse:
    def __init__(self, studies: StudiesResource) -> None:
        self._studies = studies

        self.create = to_streamed_response_wrapper(
            studies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            studies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            studies.update,
        )
        self.list = to_streamed_response_wrapper(
            studies.list,
        )
        self.cancel = to_streamed_response_wrapper(
            studies.cancel,
        )
        self.reroute_url = to_streamed_response_wrapper(
            studies.reroute_url,
        )
        self.retrieve_by_uid = to_streamed_response_wrapper(
            studies.retrieve_by_uid,
        )
        self.uncancel = to_streamed_response_wrapper(
            studies.uncancel,
        )


class AsyncStudiesResourceWithStreamingResponse:
    def __init__(self, studies: AsyncStudiesResource) -> None:
        self._studies = studies

        self.create = async_to_streamed_response_wrapper(
            studies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            studies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            studies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            studies.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            studies.cancel,
        )
        self.reroute_url = async_to_streamed_response_wrapper(
            studies.reroute_url,
        )
        self.retrieve_by_uid = async_to_streamed_response_wrapper(
            studies.retrieve_by_uid,
        )
        self.uncancel = async_to_streamed_response_wrapper(
            studies.uncancel,
        )
