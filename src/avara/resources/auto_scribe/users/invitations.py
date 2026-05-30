# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.auto_scribe.users import invitation_list_params, invitation_revoke_params, invitation_update_params
from ....types.shared.clinic_role import ClinicRole
from ....types.shared.invitation_status import InvitationStatus
from ....types.shared.assignable_user_level import AssignableUserLevel
from ....types.shared.invitation_expired_filter import InvitationExpiredFilter
from ....types.auto_scribe.users.invitation_list_response import InvitationListResponse
from ....types.auto_scribe.users.invitation_revoke_response import InvitationRevokeResponse
from ....types.auto_scribe.users.invitation_update_response import InvitationUpdateResponse
from ....types.auto_scribe.users.invitation_retrieve_response import InvitationRetrieveResponse

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
        invitation details including status, expiration, associated user information,
        and AutoScribe-specific permissions.

        Args:
          invitation_id: Unique invitation identifier. Format: inv\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._get(
            path_template("/v1/autoScribe/users/invitations/{invitation_id}", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    def update(
        self,
        invitation_id: str,
        *,
        can_create_reports: bool | Omit = omit,
        can_manage_studies: bool | Omit = omit,
        clinic_role: Optional[ClinicRole] | Omit = omit,
        first_name: str | Omit = omit,
        has_dashboard_access: bool | Omit = omit,
        last_name: str | Omit = omit,
        level: AssignableUserLevel | Omit = omit,
        middle_name: Optional[str] | Omit = omit,
        npi_number: Optional[str] | Omit = omit,
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
        Updates a pending invitation's user details, permissions, and
        AutoScribe-specific settings before it is accepted. Only valid for invitations
        that have not expired or been processed. NPI number is required if enabling
        report creation.

        Args:
          invitation_id: Unique invitation identifier. Format: inv\\__{32-hex-chars}

          can_create_reports: Whether the invited user can generate and sign radiology reports. Requires NPI
              number

          can_manage_studies: Whether the invited user will have permission to create, update, and manage
              studies

          clinic_role: A user's clinical or organizational role within the clinic.

          first_name: Invited user's first name

          has_dashboard_access: Whether the invited user will have dashboard access

          last_name: Invited user's last name

          level: User access level assignable via the API. 'admin' can manage users/settings,
              'member' has standard access. 'owner' is dashboard-only and cannot be assigned
              via the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._patch(
            path_template("/v1/autoScribe/users/invitations/{invitation_id}", invitation_id=invitation_id),
            body=maybe_transform(
                {
                    "can_create_reports": can_create_reports,
                    "can_manage_studies": can_manage_studies,
                    "clinic_role": clinic_role,
                    "first_name": first_name,
                    "has_dashboard_access": has_dashboard_access,
                    "last_name": last_name,
                    "level": level,
                    "middle_name": middle_name,
                    "npi_number": npi_number,
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
        expired: InvitationExpiredFilter | Omit = omit,
        limit: float | Omit = omit,
        start_date: str | Omit = omit,
        status: List[InvitationStatus] | Omit = omit,
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

          user_id: Filter by user ID. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/autoScribe/users/invitations",
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
          invitation_id: Invitation ID to revoke. Format: inv\\__{32-hex-chars}

          user_id: User ID whose pending invitation to revoke. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoScribe/users/invitations/revoke",
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
        invitation details including status, expiration, associated user information,
        and AutoScribe-specific permissions.

        Args:
          invitation_id: Unique invitation identifier. Format: inv\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._get(
            path_template("/v1/autoScribe/users/invitations/{invitation_id}", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationRetrieveResponse,
        )

    async def update(
        self,
        invitation_id: str,
        *,
        can_create_reports: bool | Omit = omit,
        can_manage_studies: bool | Omit = omit,
        clinic_role: Optional[ClinicRole] | Omit = omit,
        first_name: str | Omit = omit,
        has_dashboard_access: bool | Omit = omit,
        last_name: str | Omit = omit,
        level: AssignableUserLevel | Omit = omit,
        middle_name: Optional[str] | Omit = omit,
        npi_number: Optional[str] | Omit = omit,
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
        Updates a pending invitation's user details, permissions, and
        AutoScribe-specific settings before it is accepted. Only valid for invitations
        that have not expired or been processed. NPI number is required if enabling
        report creation.

        Args:
          invitation_id: Unique invitation identifier. Format: inv\\__{32-hex-chars}

          can_create_reports: Whether the invited user can generate and sign radiology reports. Requires NPI
              number

          can_manage_studies: Whether the invited user will have permission to create, update, and manage
              studies

          clinic_role: A user's clinical or organizational role within the clinic.

          first_name: Invited user's first name

          has_dashboard_access: Whether the invited user will have dashboard access

          last_name: Invited user's last name

          level: User access level assignable via the API. 'admin' can manage users/settings,
              'member' has standard access. 'owner' is dashboard-only and cannot be assigned
              via the API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._patch(
            path_template("/v1/autoScribe/users/invitations/{invitation_id}", invitation_id=invitation_id),
            body=await async_maybe_transform(
                {
                    "can_create_reports": can_create_reports,
                    "can_manage_studies": can_manage_studies,
                    "clinic_role": clinic_role,
                    "first_name": first_name,
                    "has_dashboard_access": has_dashboard_access,
                    "last_name": last_name,
                    "level": level,
                    "middle_name": middle_name,
                    "npi_number": npi_number,
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
        expired: InvitationExpiredFilter | Omit = omit,
        limit: float | Omit = omit,
        start_date: str | Omit = omit,
        status: List[InvitationStatus] | Omit = omit,
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

          user_id: Filter by user ID. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/autoScribe/users/invitations",
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
          invitation_id: Invitation ID to revoke. Format: inv\\__{32-hex-chars}

          user_id: User ID whose pending invitation to revoke. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoScribe/users/invitations/revoke",
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
