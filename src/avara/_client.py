# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AvaraError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import orgs, viewer, auto_scribe
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.orgs.orgs import OrgsResource, AsyncOrgsResource
    from .resources.viewer.viewer import ViewerResource, AsyncViewerResource
    from .resources.auto_scribe.auto_scribe import AutoScribeResource, AsyncAutoScribeResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Avara", "AsyncAvara", "Client", "AsyncClient"]


class Avara(SyncAPIClient):
    # client options
    api_key: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Avara client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `AVARA_API_KEY`
        - `webhook_key` from `AVARA_WEBHOOK_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("AVARA_API_KEY")
        if api_key is None:
            raise AvaraError(
                "The api_key client option must be set either by passing api_key to the client or by setting the AVARA_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("AVARA_WEBHOOK_KEY")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("AVARA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.avarasoftware.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def auto_scribe(self) -> AutoScribeResource:
        from .resources.auto_scribe import AutoScribeResource

        return AutoScribeResource(self)

    @cached_property
    def viewer(self) -> ViewerResource:
        from .resources.viewer import ViewerResource

        return ViewerResource(self)

    @cached_property
    def orgs(self) -> OrgsResource:
        from .resources.orgs import OrgsResource

        return OrgsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhook event handling utilities for Avara.

        Avara sends webhook events to your configured endpoint with Standard Webhooks headers
        (`webhook-id`, `webhook-timestamp`, `webhook-signature`) for signature verification.

        ## Event Types

        - **`study.access_requested`**: Synchronous - you must return presigned DICOM image URLs within the request timeout
        - **`report.delivered`**: Asynchronous notification when a report is completed

        ## TypeScript

        ```typescript
        import Avara from 'avara';
        import express from 'express';

        const client = new Avara({
          webhookKey: process.env.AVARA_WEBHOOK_KEY, // From your Avara dashboard
        });

        app.post('/webhooks/avara', express.raw({ type: 'application/json' }), (req, res) => {
          try {
            const event = client.webhooks.unwrap(req.body.toString(), req.headers);

            if (event.type === 'report.delivered') {
              console.log('Report ready:', event.data.reportId);
              console.log('PDF URL:', event.data.presignedUrl);
              return res.json({ success: true });
            }

            if (event.type === 'study.access_requested') {
              // Fetch presigned URLs from your PACS/storage
              const urls = await getPresignedUrls(event.data.studyInstanceUid);
              return res.json({ authorized: true, urls });
            }
          } catch (err) {
            console.error('Webhook error:', err);
            return res.status(400).json({ error: 'Invalid webhook' });
          }
        });
        ```

        ## Python

        ```python
        import os
        from flask import Flask, request, jsonify
        from avara import Avara

        app = Flask(__name__)
        client = Avara(webhook_key=os.environ['AVARA_WEBHOOK_KEY'])

        @app.route('/webhooks/avara', methods=['POST'])
        def handle_webhook():
            try:
                event = client.webhooks.unwrap(request.data, dict(request.headers))

                if event.type == 'report.delivered':
                    print(f"Report ready: {event.data.report_id}")
                    print(f"PDF URL: {event.data.presigned_url}")
                    return jsonify({'success': True})

                if event.type == 'study.access_requested':
                    # Fetch presigned URLs from your PACS/storage
                    urls = get_presigned_urls(event.data.study_instance_uid)
                    return jsonify({'authorized': True, 'urls': urls})

            except Exception as e:
                print(f"Webhook error: {e}")
                return jsonify({'error': 'Invalid webhook'}), 400
        ```

        ## Verification

        The `unwrap()` method verifies the webhook signature using your `webhookKey` before parsing.
        This ensures the request came from Avara and wasn't tampered with.
        """
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AvaraWithRawResponse:
        return AvaraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvaraWithStreamedResponse:
        return AvaraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAvara(AsyncAPIClient):
    # client options
    api_key: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAvara client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `AVARA_API_KEY`
        - `webhook_key` from `AVARA_WEBHOOK_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("AVARA_API_KEY")
        if api_key is None:
            raise AvaraError(
                "The api_key client option must be set either by passing api_key to the client or by setting the AVARA_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("AVARA_WEBHOOK_KEY")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("AVARA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.avarasoftware.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def auto_scribe(self) -> AsyncAutoScribeResource:
        from .resources.auto_scribe import AsyncAutoScribeResource

        return AsyncAutoScribeResource(self)

    @cached_property
    def viewer(self) -> AsyncViewerResource:
        from .resources.viewer import AsyncViewerResource

        return AsyncViewerResource(self)

    @cached_property
    def orgs(self) -> AsyncOrgsResource:
        from .resources.orgs import AsyncOrgsResource

        return AsyncOrgsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhook event handling utilities for Avara.

        Avara sends webhook events to your configured endpoint with Standard Webhooks headers
        (`webhook-id`, `webhook-timestamp`, `webhook-signature`) for signature verification.

        ## Event Types

        - **`study.access_requested`**: Synchronous - you must return presigned DICOM image URLs within the request timeout
        - **`report.delivered`**: Asynchronous notification when a report is completed

        ## TypeScript

        ```typescript
        import Avara from 'avara';
        import express from 'express';

        const client = new Avara({
          webhookKey: process.env.AVARA_WEBHOOK_KEY, // From your Avara dashboard
        });

        app.post('/webhooks/avara', express.raw({ type: 'application/json' }), (req, res) => {
          try {
            const event = client.webhooks.unwrap(req.body.toString(), req.headers);

            if (event.type === 'report.delivered') {
              console.log('Report ready:', event.data.reportId);
              console.log('PDF URL:', event.data.presignedUrl);
              return res.json({ success: true });
            }

            if (event.type === 'study.access_requested') {
              // Fetch presigned URLs from your PACS/storage
              const urls = await getPresignedUrls(event.data.studyInstanceUid);
              return res.json({ authorized: true, urls });
            }
          } catch (err) {
            console.error('Webhook error:', err);
            return res.status(400).json({ error: 'Invalid webhook' });
          }
        });
        ```

        ## Python

        ```python
        import os
        from flask import Flask, request, jsonify
        from avara import Avara

        app = Flask(__name__)
        client = Avara(webhook_key=os.environ['AVARA_WEBHOOK_KEY'])

        @app.route('/webhooks/avara', methods=['POST'])
        def handle_webhook():
            try:
                event = client.webhooks.unwrap(request.data, dict(request.headers))

                if event.type == 'report.delivered':
                    print(f"Report ready: {event.data.report_id}")
                    print(f"PDF URL: {event.data.presigned_url}")
                    return jsonify({'success': True})

                if event.type == 'study.access_requested':
                    # Fetch presigned URLs from your PACS/storage
                    urls = get_presigned_urls(event.data.study_instance_uid)
                    return jsonify({'authorized': True, 'urls': urls})

            except Exception as e:
                print(f"Webhook error: {e}")
                return jsonify({'error': 'Invalid webhook'}), 400
        ```

        ## Verification

        The `unwrap()` method verifies the webhook signature using your `webhookKey` before parsing.
        This ensures the request came from Avara and wasn't tampered with.
        """
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAvaraWithRawResponse:
        return AsyncAvaraWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvaraWithStreamedResponse:
        return AsyncAvaraWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AvaraWithRawResponse:
    _client: Avara

    def __init__(self, client: Avara) -> None:
        self._client = client

    @cached_property
    def auto_scribe(self) -> auto_scribe.AutoScribeResourceWithRawResponse:
        from .resources.auto_scribe import AutoScribeResourceWithRawResponse

        return AutoScribeResourceWithRawResponse(self._client.auto_scribe)

    @cached_property
    def viewer(self) -> viewer.ViewerResourceWithRawResponse:
        from .resources.viewer import ViewerResourceWithRawResponse

        return ViewerResourceWithRawResponse(self._client.viewer)

    @cached_property
    def orgs(self) -> orgs.OrgsResourceWithRawResponse:
        from .resources.orgs import OrgsResourceWithRawResponse

        return OrgsResourceWithRawResponse(self._client.orgs)


class AsyncAvaraWithRawResponse:
    _client: AsyncAvara

    def __init__(self, client: AsyncAvara) -> None:
        self._client = client

    @cached_property
    def auto_scribe(self) -> auto_scribe.AsyncAutoScribeResourceWithRawResponse:
        from .resources.auto_scribe import AsyncAutoScribeResourceWithRawResponse

        return AsyncAutoScribeResourceWithRawResponse(self._client.auto_scribe)

    @cached_property
    def viewer(self) -> viewer.AsyncViewerResourceWithRawResponse:
        from .resources.viewer import AsyncViewerResourceWithRawResponse

        return AsyncViewerResourceWithRawResponse(self._client.viewer)

    @cached_property
    def orgs(self) -> orgs.AsyncOrgsResourceWithRawResponse:
        from .resources.orgs import AsyncOrgsResourceWithRawResponse

        return AsyncOrgsResourceWithRawResponse(self._client.orgs)


class AvaraWithStreamedResponse:
    _client: Avara

    def __init__(self, client: Avara) -> None:
        self._client = client

    @cached_property
    def auto_scribe(self) -> auto_scribe.AutoScribeResourceWithStreamingResponse:
        from .resources.auto_scribe import AutoScribeResourceWithStreamingResponse

        return AutoScribeResourceWithStreamingResponse(self._client.auto_scribe)

    @cached_property
    def viewer(self) -> viewer.ViewerResourceWithStreamingResponse:
        from .resources.viewer import ViewerResourceWithStreamingResponse

        return ViewerResourceWithStreamingResponse(self._client.viewer)

    @cached_property
    def orgs(self) -> orgs.OrgsResourceWithStreamingResponse:
        from .resources.orgs import OrgsResourceWithStreamingResponse

        return OrgsResourceWithStreamingResponse(self._client.orgs)


class AsyncAvaraWithStreamedResponse:
    _client: AsyncAvara

    def __init__(self, client: AsyncAvara) -> None:
        self._client = client

    @cached_property
    def auto_scribe(self) -> auto_scribe.AsyncAutoScribeResourceWithStreamingResponse:
        from .resources.auto_scribe import AsyncAutoScribeResourceWithStreamingResponse

        return AsyncAutoScribeResourceWithStreamingResponse(self._client.auto_scribe)

    @cached_property
    def viewer(self) -> viewer.AsyncViewerResourceWithStreamingResponse:
        from .resources.viewer import AsyncViewerResourceWithStreamingResponse

        return AsyncViewerResourceWithStreamingResponse(self._client.viewer)

    @cached_property
    def orgs(self) -> orgs.AsyncOrgsResourceWithStreamingResponse:
        from .resources.orgs import AsyncOrgsResourceWithStreamingResponse

        return AsyncOrgsResourceWithStreamingResponse(self._client.orgs)


Client = Avara

AsyncClient = AsyncAvara
