# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.types.express import UserAddResponse, UserRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Avara) -> None:
        user = client.express.users.add(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Avara) -> None:
        response = client.express.users.with_raw_response.add(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Avara) -> None:
        with client.express.users.with_streaming_response.add(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserAddResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            client.express.users.with_raw_response.add(
                express_customer_id="",
                user_id="usr_1234567890abcdef1234567890abcdef",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Avara) -> None:
        user = client.express.users.remove(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Avara) -> None:
        response = client.express.users.with_raw_response.remove(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Avara) -> None:
        with client.express.users.with_streaming_response.remove(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRemoveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            client.express.users.with_raw_response.remove(
                express_customer_id="",
                user_id="usr_1234567890abcdef1234567890abcdef",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncAvara) -> None:
        user = await async_client.express.users.add(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.users.with_raw_response.add(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncAvara) -> None:
        async with async_client.express.users.with_streaming_response.add(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserAddResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            await async_client.express.users.with_raw_response.add(
                express_customer_id="",
                user_id="usr_1234567890abcdef1234567890abcdef",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncAvara) -> None:
        user = await async_client.express.users.remove(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.users.with_raw_response.remove(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncAvara) -> None:
        async with async_client.express.users.with_streaming_response.remove(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRemoveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            await async_client.express.users.with_raw_response.remove(
                express_customer_id="",
                user_id="usr_1234567890abcdef1234567890abcdef",
            )
