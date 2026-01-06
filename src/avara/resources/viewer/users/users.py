# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .invitations import (
    InvitationsResource,
    AsyncInvitationsResource,
    InvitationsResourceWithRawResponse,
    AsyncInvitationsResourceWithRawResponse,
    InvitationsResourceWithStreamingResponse,
    AsyncInvitationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorUsers, AsyncCursorUsers
from ...._base_client import AsyncPaginator, make_request_options
from ....types.viewer import (
    user_list_params,
    user_create_params,
    user_update_params,
    user_reactivate_params,
    user_revoke_access_params,
)
from ....types.viewer.user_list_response import UserListResponse
from ....types.viewer.user_create_response import UserCreateResponse
from ....types.viewer.user_update_response import UserUpdateResponse
from ....types.viewer.user_retrieve_response import UserRetrieveResponse
from ....types.viewer.user_reactivate_response import UserReactivateResponse
from ....types.viewer.user_revoke_access_response import UserRevokeAccessResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def invitations(self) -> InvitationsResource:
        return InvitationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        can_manage_studies: bool,
        clinic_role: Literal[
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
        ],
        email: str,
        first_name: str,
        has_dashboard_access: bool,
        last_name: str,
        level: Literal["admin", "member"],
        middle_name: str | Omit = omit,
        phone_number: str | Omit = omit,
        suffix1: str | Omit = omit,
        suffix2: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/viewer/users",
            body=maybe_transform(
                {
                    "can_manage_studies": can_manage_studies,
                    "clinic_role": clinic_role,
                    "email": email,
                    "first_name": first_name,
                    "has_dashboard_access": has_dashboard_access,
                    "last_name": last_name,
                    "level": level,
                    "middle_name": middle_name,
                    "phone_number": phone_number,
                    "suffix1": suffix1,
                    "suffix2": suffix2,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

    def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v1/viewer/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    def update(
        self,
        user_id: str,
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
    ) -> UserUpdateResponse:
        """Args:
          user_id: User ID.

        Format: usr\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/v1/viewer/users/{user_id}",
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
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        invited_source: Literal["dashboard", "api"] | Omit = omit,
        last_name: str | Omit = omit,
        level: Literal["owner", "admin", "member"] | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorUsers[UserListResponse]:
        """
        Args:
          cursor: Base64 encoded cursor from previous response

          email: Filter by exact email match

          first_name: Filter by first name (contains match)

          invited_source: Filter by invitation source

          last_name: Filter by last name (contains match)

          level: Filter by user level

          limit: Number of results to return (1-100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/viewer/users",
            page=SyncCursorUsers[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "email": email,
                        "first_name": first_name,
                        "invited_source": invited_source,
                        "last_name": last_name,
                        "level": level,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )

    def reactivate(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserReactivateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/viewer/users/reactivate",
            body=maybe_transform({"user_id": user_id}, user_reactivate_params.UserReactivateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserReactivateResponse,
        )

    def revoke_access(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRevokeAccessResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/viewer/users/revoke-access",
            body=maybe_transform({"user_id": user_id}, user_revoke_access_params.UserRevokeAccessParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRevokeAccessResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def invitations(self) -> AsyncInvitationsResource:
        return AsyncInvitationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        can_manage_studies: bool,
        clinic_role: Literal[
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
        ],
        email: str,
        first_name: str,
        has_dashboard_access: bool,
        last_name: str,
        level: Literal["admin", "member"],
        middle_name: str | Omit = omit,
        phone_number: str | Omit = omit,
        suffix1: str | Omit = omit,
        suffix2: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/viewer/users",
            body=await async_maybe_transform(
                {
                    "can_manage_studies": can_manage_studies,
                    "clinic_role": clinic_role,
                    "email": email,
                    "first_name": first_name,
                    "has_dashboard_access": has_dashboard_access,
                    "last_name": last_name,
                    "level": level,
                    "middle_name": middle_name,
                    "phone_number": phone_number,
                    "suffix1": suffix1,
                    "suffix2": suffix2,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserCreateResponse,
        )

    async def retrieve(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v1/viewer/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    async def update(
        self,
        user_id: str,
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
    ) -> UserUpdateResponse:
        """Args:
          user_id: User ID.

        Format: usr\\__<32-hex-chars>

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/v1/viewer/users/{user_id}",
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
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        invited_source: Literal["dashboard", "api"] | Omit = omit,
        last_name: str | Omit = omit,
        level: Literal["owner", "admin", "member"] | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserListResponse, AsyncCursorUsers[UserListResponse]]:
        """
        Args:
          cursor: Base64 encoded cursor from previous response

          email: Filter by exact email match

          first_name: Filter by first name (contains match)

          invited_source: Filter by invitation source

          last_name: Filter by last name (contains match)

          level: Filter by user level

          limit: Number of results to return (1-100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/viewer/users",
            page=AsyncCursorUsers[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "email": email,
                        "first_name": first_name,
                        "invited_source": invited_source,
                        "last_name": last_name,
                        "level": level,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )

    async def reactivate(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserReactivateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/viewer/users/reactivate",
            body=await async_maybe_transform({"user_id": user_id}, user_reactivate_params.UserReactivateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserReactivateResponse,
        )

    async def revoke_access(
        self,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRevokeAccessResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/viewer/users/revoke-access",
            body=await async_maybe_transform({"user_id": user_id}, user_revoke_access_params.UserRevokeAccessParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRevokeAccessResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.reactivate = to_raw_response_wrapper(
            users.reactivate,
        )
        self.revoke_access = to_raw_response_wrapper(
            users.revoke_access,
        )

    @cached_property
    def invitations(self) -> InvitationsResourceWithRawResponse:
        return InvitationsResourceWithRawResponse(self._users.invitations)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.reactivate = async_to_raw_response_wrapper(
            users.reactivate,
        )
        self.revoke_access = async_to_raw_response_wrapper(
            users.revoke_access,
        )

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithRawResponse:
        return AsyncInvitationsResourceWithRawResponse(self._users.invitations)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.reactivate = to_streamed_response_wrapper(
            users.reactivate,
        )
        self.revoke_access = to_streamed_response_wrapper(
            users.revoke_access,
        )

    @cached_property
    def invitations(self) -> InvitationsResourceWithStreamingResponse:
        return InvitationsResourceWithStreamingResponse(self._users.invitations)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.reactivate = async_to_streamed_response_wrapper(
            users.reactivate,
        )
        self.revoke_access = async_to_streamed_response_wrapper(
            users.revoke_access,
        )

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithStreamingResponse:
        return AsyncInvitationsResourceWithStreamingResponse(self._users.invitations)
