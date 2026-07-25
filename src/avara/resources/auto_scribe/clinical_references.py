# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import ClinicalReferenceType
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
from ...pagination import SyncCursorClinicalReferences, AsyncCursorClinicalReferences
from ..._base_client import AsyncPaginator, make_request_options
from ...types.auto_scribe import (
    clinical_reference_list_params,
    clinical_reference_create_params,
    clinical_reference_update_params,
)
from ...types.clinical_reference_type import ClinicalReferenceType
from ...types.auto_scribe.clinical_reference import ClinicalReference

__all__ = ["ClinicalReferencesResource", "AsyncClinicalReferencesResource"]


class ClinicalReferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClinicalReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return ClinicalReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClinicalReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return ClinicalReferencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: ClinicalReferenceType,
        express_customer_id: str | Omit = omit,
        external_reference_id: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Creates a canonical clinical reference value for study workflow pickers and
        normalization.

        Args:
          type: Category of canonical clinical reference value used for study workflow pickers
              and normalization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autoScribe/clinicalReferences",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "express_customer_id": express_customer_id,
                    "external_reference_id": external_reference_id,
                    "metadata": metadata,
                },
                clinical_reference_create_params.ClinicalReferenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    def retrieve(
        self,
        clinical_reference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Retrieves a single clinical reference by its unique identifier.

        Args:
          clinical_reference_id: Unique clinical reference identifier. Format: ref\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clinical_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `clinical_reference_id` but received {clinical_reference_id!r}"
            )
        return self._get(
            path_template(
                "/v1/autoScribe/clinicalReferences/{clinical_reference_id}", clinical_reference_id=clinical_reference_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    def update(
        self,
        clinical_reference_id: str,
        *,
        express_customer_id: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """Updates name, metadata, and Express customer assignment.

        Type is immutable after
        create.

        Args:
          clinical_reference_id: Unique clinical reference identifier. Format: ref\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clinical_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `clinical_reference_id` but received {clinical_reference_id!r}"
            )
        return self._patch(
            path_template(
                "/v1/autoScribe/clinicalReferences/{clinical_reference_id}", clinical_reference_id=clinical_reference_id
            ),
            body=maybe_transform(
                {
                    "express_customer_id": express_customer_id,
                    "metadata": metadata,
                    "name": name,
                },
                clinical_reference_update_params.ClinicalReferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        express_customer_id: str | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        limit: float | Omit = omit,
        type: ClinicalReferenceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorClinicalReferences[ClinicalReference]:
        """
        Lists clinical references with cursor-based pagination and optional filters.

        Args:
          cursor: Base64 encoded cursor from previous response

          express_customer_id: Filter by Express customer ID. Omit for no filter; pass null for clinic-wide
              references

          is_active: Filter by active status. Defaults to true (active references only). Pass false
              to list inactive references.

          limit: Number of results to return (1-100)

          type: Filter by clinical reference type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/autoScribe/clinicalReferences",
            page=SyncCursorClinicalReferences[ClinicalReference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "express_customer_id": express_customer_id,
                        "is_active": is_active,
                        "limit": limit,
                        "type": type,
                    },
                    clinical_reference_list_params.ClinicalReferenceListParams,
                ),
            ),
            model=ClinicalReference,
        )

    def delete(
        self,
        clinical_reference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Soft-deletes a clinical reference by setting isActive to false and suffixing the
        name to free the unique constraint.

        Args:
          clinical_reference_id: Unique clinical reference identifier. Format: ref\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clinical_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `clinical_reference_id` but received {clinical_reference_id!r}"
            )
        return self._post(
            path_template(
                "/v1/autoScribe/clinicalReferences/{clinical_reference_id}/delete",
                clinical_reference_id=clinical_reference_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    def retrieve_by_external_reference_id(
        self,
        external_reference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Retrieves a single clinical reference by its integrator-provided external
        reference identifier.

        Args:
          external_reference_id: Integrator-provided external reference identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `external_reference_id` but received {external_reference_id!r}"
            )
        return self._get(
            path_template(
                "/v1/autoScribe/clinicalReferences/byExternalReferenceId/{external_reference_id}",
                external_reference_id=external_reference_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )


class AsyncClinicalReferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClinicalReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/avara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClinicalReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClinicalReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/avara-python#with_streaming_response
        """
        return AsyncClinicalReferencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: ClinicalReferenceType,
        express_customer_id: str | Omit = omit,
        external_reference_id: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Creates a canonical clinical reference value for study workflow pickers and
        normalization.

        Args:
          type: Category of canonical clinical reference value used for study workflow pickers
              and normalization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autoScribe/clinicalReferences",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "express_customer_id": express_customer_id,
                    "external_reference_id": external_reference_id,
                    "metadata": metadata,
                },
                clinical_reference_create_params.ClinicalReferenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    async def retrieve(
        self,
        clinical_reference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Retrieves a single clinical reference by its unique identifier.

        Args:
          clinical_reference_id: Unique clinical reference identifier. Format: ref\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clinical_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `clinical_reference_id` but received {clinical_reference_id!r}"
            )
        return await self._get(
            path_template(
                "/v1/autoScribe/clinicalReferences/{clinical_reference_id}", clinical_reference_id=clinical_reference_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    async def update(
        self,
        clinical_reference_id: str,
        *,
        express_customer_id: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """Updates name, metadata, and Express customer assignment.

        Type is immutable after
        create.

        Args:
          clinical_reference_id: Unique clinical reference identifier. Format: ref\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clinical_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `clinical_reference_id` but received {clinical_reference_id!r}"
            )
        return await self._patch(
            path_template(
                "/v1/autoScribe/clinicalReferences/{clinical_reference_id}", clinical_reference_id=clinical_reference_id
            ),
            body=await async_maybe_transform(
                {
                    "express_customer_id": express_customer_id,
                    "metadata": metadata,
                    "name": name,
                },
                clinical_reference_update_params.ClinicalReferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        express_customer_id: str | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        limit: float | Omit = omit,
        type: ClinicalReferenceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ClinicalReference, AsyncCursorClinicalReferences[ClinicalReference]]:
        """
        Lists clinical references with cursor-based pagination and optional filters.

        Args:
          cursor: Base64 encoded cursor from previous response

          express_customer_id: Filter by Express customer ID. Omit for no filter; pass null for clinic-wide
              references

          is_active: Filter by active status. Defaults to true (active references only). Pass false
              to list inactive references.

          limit: Number of results to return (1-100)

          type: Filter by clinical reference type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/autoScribe/clinicalReferences",
            page=AsyncCursorClinicalReferences[ClinicalReference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "express_customer_id": express_customer_id,
                        "is_active": is_active,
                        "limit": limit,
                        "type": type,
                    },
                    clinical_reference_list_params.ClinicalReferenceListParams,
                ),
            ),
            model=ClinicalReference,
        )

    async def delete(
        self,
        clinical_reference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Soft-deletes a clinical reference by setting isActive to false and suffixing the
        name to free the unique constraint.

        Args:
          clinical_reference_id: Unique clinical reference identifier. Format: ref\\__{32-hex-chars}

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clinical_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `clinical_reference_id` but received {clinical_reference_id!r}"
            )
        return await self._post(
            path_template(
                "/v1/autoScribe/clinicalReferences/{clinical_reference_id}/delete",
                clinical_reference_id=clinical_reference_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )

    async def retrieve_by_external_reference_id(
        self,
        external_reference_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClinicalReference:
        """
        Retrieves a single clinical reference by its integrator-provided external
        reference identifier.

        Args:
          external_reference_id: Integrator-provided external reference identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_reference_id:
            raise ValueError(
                f"Expected a non-empty value for `external_reference_id` but received {external_reference_id!r}"
            )
        return await self._get(
            path_template(
                "/v1/autoScribe/clinicalReferences/byExternalReferenceId/{external_reference_id}",
                external_reference_id=external_reference_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClinicalReference,
        )


class ClinicalReferencesResourceWithRawResponse:
    def __init__(self, clinical_references: ClinicalReferencesResource) -> None:
        self._clinical_references = clinical_references

        self.create = to_raw_response_wrapper(
            clinical_references.create,
        )
        self.retrieve = to_raw_response_wrapper(
            clinical_references.retrieve,
        )
        self.update = to_raw_response_wrapper(
            clinical_references.update,
        )
        self.list = to_raw_response_wrapper(
            clinical_references.list,
        )
        self.delete = to_raw_response_wrapper(
            clinical_references.delete,
        )
        self.retrieve_by_external_reference_id = to_raw_response_wrapper(
            clinical_references.retrieve_by_external_reference_id,
        )


class AsyncClinicalReferencesResourceWithRawResponse:
    def __init__(self, clinical_references: AsyncClinicalReferencesResource) -> None:
        self._clinical_references = clinical_references

        self.create = async_to_raw_response_wrapper(
            clinical_references.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            clinical_references.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            clinical_references.update,
        )
        self.list = async_to_raw_response_wrapper(
            clinical_references.list,
        )
        self.delete = async_to_raw_response_wrapper(
            clinical_references.delete,
        )
        self.retrieve_by_external_reference_id = async_to_raw_response_wrapper(
            clinical_references.retrieve_by_external_reference_id,
        )


class ClinicalReferencesResourceWithStreamingResponse:
    def __init__(self, clinical_references: ClinicalReferencesResource) -> None:
        self._clinical_references = clinical_references

        self.create = to_streamed_response_wrapper(
            clinical_references.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            clinical_references.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            clinical_references.update,
        )
        self.list = to_streamed_response_wrapper(
            clinical_references.list,
        )
        self.delete = to_streamed_response_wrapper(
            clinical_references.delete,
        )
        self.retrieve_by_external_reference_id = to_streamed_response_wrapper(
            clinical_references.retrieve_by_external_reference_id,
        )


class AsyncClinicalReferencesResourceWithStreamingResponse:
    def __init__(self, clinical_references: AsyncClinicalReferencesResource) -> None:
        self._clinical_references = clinical_references

        self.create = async_to_streamed_response_wrapper(
            clinical_references.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            clinical_references.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            clinical_references.update,
        )
        self.list = async_to_streamed_response_wrapper(
            clinical_references.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            clinical_references.delete,
        )
        self.retrieve_by_external_reference_id = async_to_streamed_response_wrapper(
            clinical_references.retrieve_by_external_reference_id,
        )
