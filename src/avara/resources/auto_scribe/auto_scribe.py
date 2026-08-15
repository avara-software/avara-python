# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
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
from .clinical_references import (
    ClinicalReferencesResource,
    AsyncClinicalReferencesResource,
    ClinicalReferencesResourceWithRawResponse,
    AsyncClinicalReferencesResourceWithRawResponse,
    ClinicalReferencesResourceWithStreamingResponse,
    AsyncClinicalReferencesResourceWithStreamingResponse,
)

__all__ = ["AutoScribeResource", "AsyncAutoScribeResource"]


class AutoScribeResource(SyncAPIResource):
    @cached_property
    def clinical_references(self) -> ClinicalReferencesResource:
        return ClinicalReferencesResource(self._client)

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
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AutoScribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AutoScribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoScribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AutoScribeResourceWithStreamingResponse(self)


class AsyncAutoScribeResource(AsyncAPIResource):
    @cached_property
    def clinical_references(self) -> AsyncClinicalReferencesResource:
        return AsyncClinicalReferencesResource(self._client)

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
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAutoScribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoScribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoScribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncAutoScribeResourceWithStreamingResponse(self)


class AutoScribeResourceWithRawResponse:
    def __init__(self, auto_scribe: AutoScribeResource) -> None:
        self._auto_scribe = auto_scribe

    @cached_property
    def clinical_references(self) -> ClinicalReferencesResourceWithRawResponse:
        return ClinicalReferencesResourceWithRawResponse(self._auto_scribe.clinical_references)

    @cached_property
    def ephemeral_sessions(self) -> EphemeralSessionsResourceWithRawResponse:
        return EphemeralSessionsResourceWithRawResponse(self._auto_scribe.ephemeral_sessions)

    @cached_property
    def studies(self) -> StudiesResourceWithRawResponse:
        return StudiesResourceWithRawResponse(self._auto_scribe.studies)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._auto_scribe.users)

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._auto_scribe.reports)


class AsyncAutoScribeResourceWithRawResponse:
    def __init__(self, auto_scribe: AsyncAutoScribeResource) -> None:
        self._auto_scribe = auto_scribe

    @cached_property
    def clinical_references(self) -> AsyncClinicalReferencesResourceWithRawResponse:
        return AsyncClinicalReferencesResourceWithRawResponse(self._auto_scribe.clinical_references)

    @cached_property
    def ephemeral_sessions(self) -> AsyncEphemeralSessionsResourceWithRawResponse:
        return AsyncEphemeralSessionsResourceWithRawResponse(self._auto_scribe.ephemeral_sessions)

    @cached_property
    def studies(self) -> AsyncStudiesResourceWithRawResponse:
        return AsyncStudiesResourceWithRawResponse(self._auto_scribe.studies)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._auto_scribe.users)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._auto_scribe.reports)


class AutoScribeResourceWithStreamingResponse:
    def __init__(self, auto_scribe: AutoScribeResource) -> None:
        self._auto_scribe = auto_scribe

    @cached_property
    def clinical_references(self) -> ClinicalReferencesResourceWithStreamingResponse:
        return ClinicalReferencesResourceWithStreamingResponse(self._auto_scribe.clinical_references)

    @cached_property
    def ephemeral_sessions(self) -> EphemeralSessionsResourceWithStreamingResponse:
        return EphemeralSessionsResourceWithStreamingResponse(self._auto_scribe.ephemeral_sessions)

    @cached_property
    def studies(self) -> StudiesResourceWithStreamingResponse:
        return StudiesResourceWithStreamingResponse(self._auto_scribe.studies)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._auto_scribe.users)

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._auto_scribe.reports)


class AsyncAutoScribeResourceWithStreamingResponse:
    def __init__(self, auto_scribe: AsyncAutoScribeResource) -> None:
        self._auto_scribe = auto_scribe

    @cached_property
    def clinical_references(self) -> AsyncClinicalReferencesResourceWithStreamingResponse:
        return AsyncClinicalReferencesResourceWithStreamingResponse(self._auto_scribe.clinical_references)

    @cached_property
    def ephemeral_sessions(self) -> AsyncEphemeralSessionsResourceWithStreamingResponse:
        return AsyncEphemeralSessionsResourceWithStreamingResponse(self._auto_scribe.ephemeral_sessions)

    @cached_property
    def studies(self) -> AsyncStudiesResourceWithStreamingResponse:
        return AsyncStudiesResourceWithStreamingResponse(self._auto_scribe.studies)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._auto_scribe.users)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._auto_scribe.reports)
