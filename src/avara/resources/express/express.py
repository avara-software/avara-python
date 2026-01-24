# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import express_list_params, express_create_params, express_update_params
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
from ...pagination import SyncCursorExpressCustomers, AsyncCursorExpressCustomers
from ..._base_client import AsyncPaginator, make_request_options
from ...types.express_list_response import ExpressListResponse
from ...types.express_create_response import ExpressCreateResponse
from ...types.express_update_response import ExpressUpdateResponse
from ...types.express_retrieve_response import ExpressRetrieveResponse
from ...types.express_deactivate_response import ExpressDeactivateResponse
from ...types.express_reactivate_response import ExpressReactivateResponse

__all__ = ["ExpressResource", "AsyncExpressResource"]


class ExpressResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExpressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return ExpressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return ExpressResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        express_customer_name: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressCreateResponse:
        """Creates a new customer with a unique identifier and name.

        Customers can be used
        to group and manage users, studies, and access permissions across the Avara
        platform.

        Args:
          express_customer_name: Name of the Express customer to create

          metadata: Custom key-value metadata for the Express customer. Maximum 50 pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/express",
            body=maybe_transform(
                {
                    "express_customer_name": express_customer_name,
                    "metadata": metadata,
                },
                express_create_params.ExpressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressCreateResponse,
        )

    def retrieve(
        self,
        express_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressRetrieveResponse:
        """Retrieves a single customer by its unique customer ID.

        Returns the complete
        customer object with name, status, and timestamps.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return self._get(
            f"/v1/express/{express_customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressRetrieveResponse,
        )

    def update(
        self,
        express_customer_id: str,
        *,
        express_customer_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressUpdateResponse:
        """Updates a customer's properties such as name or other metadata.

        All fields are
        optional - only provided fields will be updated.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          express_customer_name: Updated name for the Express customer

          metadata: Updated metadata. Pass null to clear all metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return self._patch(
            f"/v1/express/{express_customer_id}",
            body=maybe_transform(
                {
                    "express_customer_name": express_customer_name,
                    "metadata": metadata,
                },
                express_update_params.ExpressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorExpressCustomers[ExpressListResponse]:
        """Retrieves a paginated list of customers with optional filtering by name.

        Returns
        up to 100 customers per request.

        Args:
          cursor: Base64 encoded cursor from previous response

          limit: Number of results to return (1-100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/express",
            page=SyncCursorExpressCustomers[ExpressListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    express_list_params.ExpressListParams,
                ),
            ),
            model=ExpressListResponse,
        )

    def deactivate(
        self,
        express_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressDeactivateResponse:
        """
        Deactivates a customer, preventing it from being used for new studies or user
        assignments. Existing data is preserved and the customer can be reactivated
        later.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

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
            f"/v1/express/{express_customer_id}/deactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressDeactivateResponse,
        )

    def reactivate(
        self,
        express_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressReactivateResponse:
        """
        Restores a deactivated customer to active status, allowing it to be used for new
        studies and user assignments again.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

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
            f"/v1/express/{express_customer_id}/reactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressReactivateResponse,
        )


class AsyncExpressResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExpressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncExpressResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        express_customer_name: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressCreateResponse:
        """Creates a new customer with a unique identifier and name.

        Customers can be used
        to group and manage users, studies, and access permissions across the Avara
        platform.

        Args:
          express_customer_name: Name of the Express customer to create

          metadata: Custom key-value metadata for the Express customer. Maximum 50 pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/express",
            body=await async_maybe_transform(
                {
                    "express_customer_name": express_customer_name,
                    "metadata": metadata,
                },
                express_create_params.ExpressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressCreateResponse,
        )

    async def retrieve(
        self,
        express_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressRetrieveResponse:
        """Retrieves a single customer by its unique customer ID.

        Returns the complete
        customer object with name, status, and timestamps.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return await self._get(
            f"/v1/express/{express_customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressRetrieveResponse,
        )

    async def update(
        self,
        express_customer_id: str,
        *,
        express_customer_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressUpdateResponse:
        """Updates a customer's properties such as name or other metadata.

        All fields are
        optional - only provided fields will be updated.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

          express_customer_name: Updated name for the Express customer

          metadata: Updated metadata. Pass null to clear all metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not express_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `express_customer_id` but received {express_customer_id!r}"
            )
        return await self._patch(
            f"/v1/express/{express_customer_id}",
            body=await async_maybe_transform(
                {
                    "express_customer_name": express_customer_name,
                    "metadata": metadata,
                },
                express_update_params.ExpressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExpressListResponse, AsyncCursorExpressCustomers[ExpressListResponse]]:
        """Retrieves a paginated list of customers with optional filtering by name.

        Returns
        up to 100 customers per request.

        Args:
          cursor: Base64 encoded cursor from previous response

          limit: Number of results to return (1-100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/express",
            page=AsyncCursorExpressCustomers[ExpressListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    express_list_params.ExpressListParams,
                ),
            ),
            model=ExpressListResponse,
        )

    async def deactivate(
        self,
        express_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressDeactivateResponse:
        """
        Deactivates a customer, preventing it from being used for new studies or user
        assignments. Existing data is preserved and the customer can be reactivated
        later.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

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
            f"/v1/express/{express_customer_id}/deactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressDeactivateResponse,
        )

    async def reactivate(
        self,
        express_customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExpressReactivateResponse:
        """
        Restores a deactivated customer to active status, allowing it to be used for new
        studies and user assignments again.

        Args:
          express_customer_id: Unique Express customer identifier. Format: cus\\__{32-hex-chars}

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
            f"/v1/express/{express_customer_id}/reactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpressReactivateResponse,
        )


class ExpressResourceWithRawResponse:
    def __init__(self, express: ExpressResource) -> None:
        self._express = express

        self.create = to_raw_response_wrapper(
            express.create,
        )
        self.retrieve = to_raw_response_wrapper(
            express.retrieve,
        )
        self.update = to_raw_response_wrapper(
            express.update,
        )
        self.list = to_raw_response_wrapper(
            express.list,
        )
        self.deactivate = to_raw_response_wrapper(
            express.deactivate,
        )
        self.reactivate = to_raw_response_wrapper(
            express.reactivate,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._express.users)


class AsyncExpressResourceWithRawResponse:
    def __init__(self, express: AsyncExpressResource) -> None:
        self._express = express

        self.create = async_to_raw_response_wrapper(
            express.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            express.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            express.update,
        )
        self.list = async_to_raw_response_wrapper(
            express.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            express.deactivate,
        )
        self.reactivate = async_to_raw_response_wrapper(
            express.reactivate,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._express.users)


class ExpressResourceWithStreamingResponse:
    def __init__(self, express: ExpressResource) -> None:
        self._express = express

        self.create = to_streamed_response_wrapper(
            express.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            express.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            express.update,
        )
        self.list = to_streamed_response_wrapper(
            express.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            express.deactivate,
        )
        self.reactivate = to_streamed_response_wrapper(
            express.reactivate,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._express.users)


class AsyncExpressResourceWithStreamingResponse:
    def __init__(self, express: AsyncExpressResource) -> None:
        self._express = express

        self.create = async_to_streamed_response_wrapper(
            express.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            express.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            express.update,
        )
        self.list = async_to_streamed_response_wrapper(
            express.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            express.deactivate,
        )
        self.reactivate = async_to_streamed_response_wrapper(
            express.reactivate,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._express.users)
