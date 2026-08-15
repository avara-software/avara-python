# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ...types.auto_scribe import ephemeral_session_create_params
from ...types.auto_scribe.ephemeral_session_create_response import EphemeralSessionCreateResponse

__all__ = ["EphemeralSessionsResource", "AsyncEphemeralSessionsResource"]


class EphemeralSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EphemeralSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return EphemeralSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EphemeralSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return EphemeralSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        retrieval_id: str,
        options: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EphemeralSessionCreateResponse:
        """
        Mints a 30-second tokenized landing URL for a userless, studyless AutoScribe
        viewer session. The token names a customer retrievalId (not an Avara study).
        Optional options are echoed verbatim on ephemeral.access_requested (max 3072
        bytes JSON). Requires a customer study webhook on the API key.

        Args:
          retrieval_id: Opaque customer handle for this view session. Avara stores and echoes it; it is
              not an Avara study ID.

          options: Optional JSON object echoed verbatim on ephemeral.access_requested. Avara does
              not read or edit it. Hard cap 3072 bytes on JSON.stringify. Examples:
              studyInstanceUids or internal ids for multi-study reads. Not for URLs or
              manifests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoScribe/ephemeral-sessions",
            body=maybe_transform(
                {
                    "retrieval_id": retrieval_id,
                    "options": options,
                },
                ephemeral_session_create_params.EphemeralSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EphemeralSessionCreateResponse,
        )


class AsyncEphemeralSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEphemeralSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEphemeralSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEphemeralSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncEphemeralSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        retrieval_id: str,
        options: Dict[str, Optional[object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EphemeralSessionCreateResponse:
        """
        Mints a 30-second tokenized landing URL for a userless, studyless AutoScribe
        viewer session. The token names a customer retrievalId (not an Avara study).
        Optional options are echoed verbatim on ephemeral.access_requested (max 3072
        bytes JSON). Requires a customer study webhook on the API key.

        Args:
          retrieval_id: Opaque customer handle for this view session. Avara stores and echoes it; it is
              not an Avara study ID.

          options: Optional JSON object echoed verbatim on ephemeral.access_requested. Avara does
              not read or edit it. Hard cap 3072 bytes on JSON.stringify. Examples:
              studyInstanceUids or internal ids for multi-study reads. Not for URLs or
              manifests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoScribe/ephemeral-sessions",
            body=await async_maybe_transform(
                {
                    "retrieval_id": retrieval_id,
                    "options": options,
                },
                ephemeral_session_create_params.EphemeralSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EphemeralSessionCreateResponse,
        )


class EphemeralSessionsResourceWithRawResponse:
    def __init__(self, ephemeral_sessions: EphemeralSessionsResource) -> None:
        self._ephemeral_sessions = ephemeral_sessions

        self.create = to_raw_response_wrapper(
            ephemeral_sessions.create,
        )


class AsyncEphemeralSessionsResourceWithRawResponse:
    def __init__(self, ephemeral_sessions: AsyncEphemeralSessionsResource) -> None:
        self._ephemeral_sessions = ephemeral_sessions

        self.create = async_to_raw_response_wrapper(
            ephemeral_sessions.create,
        )


class EphemeralSessionsResourceWithStreamingResponse:
    def __init__(self, ephemeral_sessions: EphemeralSessionsResource) -> None:
        self._ephemeral_sessions = ephemeral_sessions

        self.create = to_streamed_response_wrapper(
            ephemeral_sessions.create,
        )


class AsyncEphemeralSessionsResourceWithStreamingResponse:
    def __init__(self, ephemeral_sessions: AsyncEphemeralSessionsResource) -> None:
        self._ephemeral_sessions = ephemeral_sessions

        self.create = async_to_streamed_response_wrapper(
            ephemeral_sessions.create,
        )
