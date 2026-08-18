# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.express import user_add_params, user_remove_params
from ...types.express.user_add_response import UserAddResponse
from ...types.express.user_remove_response import UserRemoveResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/avara-software/avara-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/avara-software/avara-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def add(
        self,
        express_customer_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAddResponse:
        """
        Associates an existing user with a customer, granting them access to
        customer-specific resources and studies.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          user_id: User ID to add to the Express customer. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return self._post(
            path_template("/v1/express/{express_customer_id}/users", express_customer_id=express_customer_id),
            body=maybe_transform({"user_id": user_id}, user_add_params.UserAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddResponse,
        )

    def remove(
        self,
        express_customer_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRemoveResponse:
        """
        Removes a user's association with a customer, revoking their access to
        customer-specific resources. The user account remains active but is no longer
        linked to this customer.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          user_id: User ID to remove from the Express customer. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return self._delete(
            path_template("/v1/express/{express_customer_id}/users", express_customer_id=express_customer_id),
            body=maybe_transform({"user_id": user_id}, user_remove_params.UserRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/avara-software/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/avara-software/avara-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def add(
        self,
        express_customer_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAddResponse:
        """
        Associates an existing user with a customer, granting them access to
        customer-specific resources and studies.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          user_id: User ID to add to the Express customer. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return await self._post(
            path_template("/v1/express/{express_customer_id}/users", express_customer_id=express_customer_id),
            body=await async_maybe_transform({"user_id": user_id}, user_add_params.UserAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddResponse,
        )

    async def remove(
        self,
        express_customer_id: str,
        *,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRemoveResponse:
        """
        Removes a user's association with a customer, revoking their access to
        customer-specific resources. The user account remains active but is no longer
        linked to this customer.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          user_id: User ID to remove from the Express customer. Format: usr\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return await self._delete(
            path_template("/v1/express/{express_customer_id}/users", express_customer_id=express_customer_id),
            body=await async_maybe_transform({"user_id": user_id}, user_remove_params.UserRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.remove = to_raw_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.remove = async_to_raw_response_wrapper(
            users.remove,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.remove = to_streamed_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            users.remove,
        )
