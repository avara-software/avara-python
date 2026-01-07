# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import Mapping, cast

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import AvaraError
from ..types.unwrap_webhook_event import UnwrapWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
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

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> UnwrapWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise AvaraError("You need to install `avara[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
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

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> UnwrapWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise AvaraError("You need to install `avara[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )
