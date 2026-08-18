# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .studies import (
    StudiesResource,
    AsyncStudiesResource,
    StudiesResourceWithRawResponse,
    AsyncStudiesResourceWithRawResponse,
    StudiesResourceWithStreamingResponse,
    AsyncStudiesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .ephemeral_sessions import (
    EphemeralSessionsResource,
    AsyncEphemeralSessionsResource,
    EphemeralSessionsResourceWithRawResponse,
    AsyncEphemeralSessionsResourceWithRawResponse,
    EphemeralSessionsResourceWithStreamingResponse,
    AsyncEphemeralSessionsResourceWithStreamingResponse,
)

__all__ = ["ViewerResource", "AsyncViewerResource"]


class ViewerResource(SyncAPIResource):
    @cached_property
    def ephemeral_sessions(self) -> EphemeralSessionsResource:
        return EphemeralSessionsResource(self._client)

    @cached_property
    def studies(self) -> StudiesResource:
        return StudiesResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ViewerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/avara-software/avara-python#accessing-raw-response-data-eg-headers
        """
        return ViewerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/avara-software/avara-python#with_streaming_response
        """
        return ViewerResourceWithStreamingResponse(self)


class AsyncViewerResource(AsyncAPIResource):
    @cached_property
    def ephemeral_sessions(self) -> AsyncEphemeralSessionsResource:
        return AsyncEphemeralSessionsResource(self._client)

    @cached_property
    def studies(self) -> AsyncStudiesResource:
        return AsyncStudiesResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncViewerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/avara-software/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViewerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/avara-software/avara-python#with_streaming_response
        """
        return AsyncViewerResourceWithStreamingResponse(self)


class ViewerResourceWithRawResponse:
    def __init__(self, viewer: ViewerResource) -> None:
        self._viewer = viewer

    @cached_property
    def ephemeral_sessions(self) -> EphemeralSessionsResourceWithRawResponse:
        return EphemeralSessionsResourceWithRawResponse(self._viewer.ephemeral_sessions)

    @cached_property
    def studies(self) -> StudiesResourceWithRawResponse:
        return StudiesResourceWithRawResponse(self._viewer.studies)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._viewer.users)


class AsyncViewerResourceWithRawResponse:
    def __init__(self, viewer: AsyncViewerResource) -> None:
        self._viewer = viewer

    @cached_property
    def ephemeral_sessions(self) -> AsyncEphemeralSessionsResourceWithRawResponse:
        return AsyncEphemeralSessionsResourceWithRawResponse(self._viewer.ephemeral_sessions)

    @cached_property
    def studies(self) -> AsyncStudiesResourceWithRawResponse:
        return AsyncStudiesResourceWithRawResponse(self._viewer.studies)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._viewer.users)


class ViewerResourceWithStreamingResponse:
    def __init__(self, viewer: ViewerResource) -> None:
        self._viewer = viewer

    @cached_property
    def ephemeral_sessions(self) -> EphemeralSessionsResourceWithStreamingResponse:
        return EphemeralSessionsResourceWithStreamingResponse(self._viewer.ephemeral_sessions)

    @cached_property
    def studies(self) -> StudiesResourceWithStreamingResponse:
        return StudiesResourceWithStreamingResponse(self._viewer.studies)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._viewer.users)


class AsyncViewerResourceWithStreamingResponse:
    def __init__(self, viewer: AsyncViewerResource) -> None:
        self._viewer = viewer

    @cached_property
    def ephemeral_sessions(self) -> AsyncEphemeralSessionsResourceWithStreamingResponse:
        return AsyncEphemeralSessionsResourceWithStreamingResponse(self._viewer.ephemeral_sessions)

    @cached_property
    def studies(self) -> AsyncStudiesResourceWithStreamingResponse:
        return AsyncStudiesResourceWithStreamingResponse(self._viewer.studies)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._viewer.users)
