# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.types.auto_scribe import EphemeralSessionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEphemeralSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        ephemeral_session = client.auto_scribe.ephemeral_sessions.create(
            retrieval_id="order-12345",
        )
        assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        ephemeral_session = client.auto_scribe.ephemeral_sessions.create(
            retrieval_id="order-12345",
            hanging_protocol={
                "layout": "2x2",
                "viewport_assignments": ["Axial T1", "Axial T2", None, "Sagittal T2"],
            },
            options={"studyInstanceUids": "bar"},
        )
        assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.auto_scribe.ephemeral_sessions.with_raw_response.create(
            retrieval_id="order-12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeral_session = response.parse()
        assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.auto_scribe.ephemeral_sessions.with_streaming_response.create(
            retrieval_id="order-12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeral_session = response.parse()
            assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEphemeralSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        ephemeral_session = await async_client.auto_scribe.ephemeral_sessions.create(
            retrieval_id="order-12345",
        )
        assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        ephemeral_session = await async_client.auto_scribe.ephemeral_sessions.create(
            retrieval_id="order-12345",
            hanging_protocol={
                "layout": "2x2",
                "viewport_assignments": ["Axial T1", "Axial T2", None, "Sagittal T2"],
            },
            options={"studyInstanceUids": "bar"},
        )
        assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.ephemeral_sessions.with_raw_response.create(
            retrieval_id="order-12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ephemeral_session = await response.parse()
        assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.ephemeral_sessions.with_streaming_response.create(
            retrieval_id="order-12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ephemeral_session = await response.parse()
            assert_matches_type(EphemeralSessionCreateResponse, ephemeral_session, path=["response"])

        assert cast(Any, response.is_closed) is True
