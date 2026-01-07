# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorInvitations, AsyncCursorInvitations
from ...._base_client import AsyncPaginator, make_request_options
from ....types.viewer.users import invitation_list_params, invitation_revoke_params, invitation_update_params
from ....types.viewer.users.invitation_list_response import InvitationListResponse
from ....types.viewer.users.invitation_revoke_response import InvitationRevokeResponse
from ....types.viewer.users.invitation_update_response import InvitationUpdateResponse
from ....types.viewer.users.invitation_retrieve_response import InvitationRetrieveResponse

__all__ = ["InvitationsResource", "AsyncInvitationsResource"]


class InvitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return InvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return InvitationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRetrieveResponse:
        """Retrieves a single invitation by its unique invitation ID.

        Returns the complete
        invitation details including status, expiration, and associated user
        information.

        Args:
          invitation_id: Invitation ID. Format: inv\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._get(
            f"/v1/viewer/users/invitations/{invitation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    def update(
        self,
        invitation_id: str,
        *,
        can_manage_studies: bool | Omit = omit,
        clinic_role: Optional[
            Literal[
                "Radiologist",
                "Cardiologist",
                "Neurologist",
                "Urologist",
                "Gynecologist",
                "Endocrinologist",
                "Doctor",
                "Surgeon",
                "Physician",
                "Physician Assistant",
                "Nurse Practitioner",
                "Registered Nurse",
                "Patient Care Coordinator",
                "Front Desk Operator",
                "Imaging Technologist",
                "PACS Administrator",
                "Software Engineer",
                "Revenue Cycle Manager",
                "Administrative Director",
                "Administrative Assistant",
                "Other",
            ]
        ]
        | Omit = omit,
        first_name: str | Omit = omit,
        has_dashboard_access: bool | Omit = omit,
        last_name: str | Omit = omit,
        level: Literal["admin", "member"] | Omit = omit,
        middle_name: Optional[str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        suffix1: Optional[str] | Omit = omit,
        suffix2: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationUpdateResponse:
        """
        Updates a pending invitation's user details and permissions before it is
        accepted. Only valid for invitations that have not expired or been processed.

        Args:
          invitation_id: Invitation ID. Format: inv\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._patch(
            f"/v1/viewer/users/invitations/{invitation_id}",
            body=maybe_transform(
                {
                    "can_manage_studies": can_manage_studies,
                    "clinic_role": clinic_role,
                    "first_name": first_name,
                    "has_dashboard_access": has_dashboard_access,
                    "last_name": last_name,
                    "level": level,
                    "middle_name": middle_name,
                    "phone_number": phone_number,
                    "suffix1": suffix1,
                    "suffix2": suffix2,
                },
                invitation_update_params.InvitationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        end_date: str | Omit = omit,
        expired: Literal["all", "expired", "not-expired"] | Omit = omit,
        limit: float | Omit = omit,
        start_date: str | Omit = omit,
        status: List[Literal["sent", "accepted", "rejected", "revoked"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorInvitations[InvitationListResponse]:
        """
        Retrieves a paginated list of user invitations with optional filtering by
        status, expiration, date range, and user ID. Returns up to 100 invitations per
        request.

        Args:
          cursor: Base64 encoded cursor from previous response

          end_date: Filter invitations created on or before this date (YYYY-MM-DD)

          expired: Filter by expiration status

          limit: Number of results to return (1-100)

          start_date: Filter invitations created on or after this date (YYYY-MM-DD)

          status: Filter by invitation status(es)

          user_id: Filter by user ID. Format: usr\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/viewer/users/invitations",
            page=SyncCursorInvitations[InvitationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "end_date": end_date,
                        "expired": expired,
                        "limit": limit,
                        "start_date": start_date,
                        "status": status,
                        "user_id": user_id,
                    },
                    invitation_list_params.InvitationListParams,
                ),
            ),
            model=InvitationListResponse,
        )

    def revoke(
        self,
        *,
        invitation_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRevokeResponse:
        """Revokes a pending invitation, preventing it from being accepted.

        Can revoke by
        invitation ID, user ID, or both. Useful for cancelling invitations sent in
        error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/viewer/users/invitations/revoke",
            body=maybe_transform(
                {
                    "invitation_id": invitation_id,
                    "user_id": user_id,
                },
                invitation_revoke_params.InvitationRevokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRevokeResponse,
        )


class AsyncInvitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncInvitationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRetrieveResponse:
        """Retrieves a single invitation by its unique invitation ID.

        Returns the complete
        invitation details including status, expiration, and associated user
        information.

        Args:
          invitation_id: Invitation ID. Format: inv\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._get(
            f"/v1/viewer/users/invitations/{invitation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    async def update(
        self,
        invitation_id: str,
        *,
        can_manage_studies: bool | Omit = omit,
        clinic_role: Optional[
            Literal[
                "Radiologist",
                "Cardiologist",
                "Neurologist",
                "Urologist",
                "Gynecologist",
                "Endocrinologist",
                "Doctor",
                "Surgeon",
                "Physician",
                "Physician Assistant",
                "Nurse Practitioner",
                "Registered Nurse",
                "Patient Care Coordinator",
                "Front Desk Operator",
                "Imaging Technologist",
                "PACS Administrator",
                "Software Engineer",
                "Revenue Cycle Manager",
                "Administrative Director",
                "Administrative Assistant",
                "Other",
            ]
        ]
        | Omit = omit,
        first_name: str | Omit = omit,
        has_dashboard_access: bool | Omit = omit,
        last_name: str | Omit = omit,
        level: Literal["admin", "member"] | Omit = omit,
        middle_name: Optional[str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        suffix1: Optional[str] | Omit = omit,
        suffix2: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationUpdateResponse:
        """
        Updates a pending invitation's user details and permissions before it is
        accepted. Only valid for invitations that have not expired or been processed.

        Args:
          invitation_id: Invitation ID. Format: inv\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._patch(
            f"/v1/viewer/users/invitations/{invitation_id}",
            body=await async_maybe_transform(
                {
                    "can_manage_studies": can_manage_studies,
                    "clinic_role": clinic_role,
                    "first_name": first_name,
                    "has_dashboard_access": has_dashboard_access,
                    "last_name": last_name,
                    "level": level,
                    "middle_name": middle_name,
                    "phone_number": phone_number,
                    "suffix1": suffix1,
                    "suffix2": suffix2,
                },
                invitation_update_params.InvitationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        end_date: str | Omit = omit,
        expired: Literal["all", "expired", "not-expired"] | Omit = omit,
        limit: float | Omit = omit,
        start_date: str | Omit = omit,
        status: List[Literal["sent", "accepted", "rejected", "revoked"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InvitationListResponse, AsyncCursorInvitations[InvitationListResponse]]:
        """
        Retrieves a paginated list of user invitations with optional filtering by
        status, expiration, date range, and user ID. Returns up to 100 invitations per
        request.

        Args:
          cursor: Base64 encoded cursor from previous response

          end_date: Filter invitations created on or before this date (YYYY-MM-DD)

          expired: Filter by expiration status

          limit: Number of results to return (1-100)

          start_date: Filter invitations created on or after this date (YYYY-MM-DD)

          status: Filter by invitation status(es)

          user_id: Filter by user ID. Format: usr\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/viewer/users/invitations",
            page=AsyncCursorInvitations[InvitationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "end_date": end_date,
                        "expired": expired,
                        "limit": limit,
                        "start_date": start_date,
                        "status": status,
                        "user_id": user_id,
                    },
                    invitation_list_params.InvitationListParams,
                ),
            ),
            model=InvitationListResponse,
        )

    async def revoke(
        self,
        *,
        invitation_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationRevokeResponse:
        """Revokes a pending invitation, preventing it from being accepted.

        Can revoke by
        invitation ID, user ID, or both. Useful for cancelling invitations sent in
        error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/viewer/users/invitations/revoke",
            body=await async_maybe_transform(
                {
                    "invitation_id": invitation_id,
                    "user_id": user_id,
                },
                invitation_revoke_params.InvitationRevokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRevokeResponse,
        )


class InvitationsResourceWithRawResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = to_raw_response_wrapper(
            invitations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            invitations.update,
        )
        self.list = to_raw_response_wrapper(
            invitations.list,
        )
        self.revoke = to_raw_response_wrapper(
            invitations.revoke,
        )


class AsyncInvitationsResourceWithRawResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = async_to_raw_response_wrapper(
            invitations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            invitations.update,
        )
        self.list = async_to_raw_response_wrapper(
            invitations.list,
        )
        self.revoke = async_to_raw_response_wrapper(
            invitations.revoke,
        )


class InvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = to_streamed_response_wrapper(
            invitations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invitations.update,
        )
        self.list = to_streamed_response_wrapper(
            invitations.list,
        )
        self.revoke = to_streamed_response_wrapper(
            invitations.revoke,
        )


class AsyncInvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.retrieve = async_to_streamed_response_wrapper(
            invitations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invitations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invitations.list,
        )
        self.revoke = async_to_streamed_response_wrapper(
            invitations.revoke,
        )
