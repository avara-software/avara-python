# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from avara.types import (
    ExpressListResponse,
    ExpressCreateResponse,
    ExpressUpdateResponse,
    ExpressRetrieveResponse,
    ExpressDeactivateResponse,
    ExpressReactivateResponse,
)
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorExpressCustomers, AsyncCursorExpressCustomers

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpress:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        express = client.express.create(
            express_customer_name="City Medical Center - Radiology Department",
        )
        assert_matches_type(ExpressCreateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        express = client.express.create(
            express_customer_name="City Medical Center - Radiology Department",
            metadata={
                "department": "radiology",
                "region": "northeast",
            },
        )
        assert_matches_type(ExpressCreateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.express.with_raw_response.create(
            express_customer_name="City Medical Center - Radiology Department",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = response.parse()
        assert_matches_type(ExpressCreateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.express.with_streaming_response.create(
            express_customer_name="City Medical Center - Radiology Department",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = response.parse()
            assert_matches_type(ExpressCreateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        express = client.express.retrieve(
            "cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressRetrieveResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.express.with_raw_response.retrieve(
            "cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = response.parse()
        assert_matches_type(ExpressRetrieveResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.express.with_streaming_response.retrieve(
            "cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = response.parse()
            assert_matches_type(ExpressRetrieveResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            client.express.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Avara) -> None:
        express = client.express.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressUpdateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Avara) -> None:
        express = client.express.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            express_customer_name="City Medical Center - Radiology & Imaging",
            metadata={
                "department": "radiology",
                "region": "northeast",
                "wing": "Building A",
            },
        )
        assert_matches_type(ExpressUpdateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Avara) -> None:
        response = client.express.with_raw_response.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = response.parse()
        assert_matches_type(ExpressUpdateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Avara) -> None:
        with client.express.with_streaming_response.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = response.parse()
            assert_matches_type(ExpressUpdateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            client.express.with_raw_response.update(
                express_customer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        express = client.express.list()
        assert_matches_type(SyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        express = client.express.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            limit=20,
        )
        assert_matches_type(SyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.express.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = response.parse()
        assert_matches_type(SyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.express.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = response.parse()
            assert_matches_type(SyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: Avara) -> None:
        express = client.express.deactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressDeactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: Avara) -> None:
        response = client.express.with_raw_response.deactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = response.parse()
        assert_matches_type(ExpressDeactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: Avara) -> None:
        with client.express.with_streaming_response.deactivate(
            "cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = response.parse()
            assert_matches_type(ExpressDeactivateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            client.express.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reactivate(self, client: Avara) -> None:
        express = client.express.reactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressReactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reactivate(self, client: Avara) -> None:
        response = client.express.with_raw_response.reactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = response.parse()
        assert_matches_type(ExpressReactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reactivate(self, client: Avara) -> None:
        with client.express.with_streaming_response.reactivate(
            "cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = response.parse()
            assert_matches_type(ExpressReactivateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reactivate(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            client.express.with_raw_response.reactivate(
                "",
            )


class TestAsyncExpress:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.create(
            express_customer_name="City Medical Center - Radiology Department",
        )
        assert_matches_type(ExpressCreateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.create(
            express_customer_name="City Medical Center - Radiology Department",
            metadata={
                "department": "radiology",
                "region": "northeast",
            },
        )
        assert_matches_type(ExpressCreateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.with_raw_response.create(
            express_customer_name="City Medical Center - Radiology Department",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = await response.parse()
        assert_matches_type(ExpressCreateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.express.with_streaming_response.create(
            express_customer_name="City Medical Center - Radiology Department",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = await response.parse()
            assert_matches_type(ExpressCreateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.retrieve(
            "cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressRetrieveResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.with_raw_response.retrieve(
            "cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = await response.parse()
        assert_matches_type(ExpressRetrieveResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.express.with_streaming_response.retrieve(
            "cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = await response.parse()
            assert_matches_type(ExpressRetrieveResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            await async_client.express.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressUpdateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            express_customer_name="City Medical Center - Radiology & Imaging",
            metadata={
                "department": "radiology",
                "region": "northeast",
                "wing": "Building A",
            },
        )
        assert_matches_type(ExpressUpdateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.with_raw_response.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = await response.parse()
        assert_matches_type(ExpressUpdateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAvara) -> None:
        async with async_client.express.with_streaming_response.update(
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = await response.parse()
            assert_matches_type(ExpressUpdateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            await async_client.express.with_raw_response.update(
                express_customer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.list()
        assert_matches_type(AsyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            limit=20,
        )
        assert_matches_type(AsyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = await response.parse()
        assert_matches_type(AsyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.express.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = await response.parse()
            assert_matches_type(AsyncCursorExpressCustomers[ExpressListResponse], express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.deactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressDeactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.with_raw_response.deactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = await response.parse()
        assert_matches_type(ExpressDeactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncAvara) -> None:
        async with async_client.express.with_streaming_response.deactivate(
            "cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = await response.parse()
            assert_matches_type(ExpressDeactivateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            await async_client.express.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reactivate(self, async_client: AsyncAvara) -> None:
        express = await async_client.express.reactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ExpressReactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reactivate(self, async_client: AsyncAvara) -> None:
        response = await async_client.express.with_raw_response.reactivate(
            "cus_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        express = await response.parse()
        assert_matches_type(ExpressReactivateResponse, express, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reactivate(self, async_client: AsyncAvara) -> None:
        async with async_client.express.with_streaming_response.reactivate(
            "cus_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            express = await response.parse()
            assert_matches_type(ExpressReactivateResponse, express, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reactivate(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `express_customer_id` but received ''"):
            await async_client.express.with_raw_response.reactivate(
                "",
            )
