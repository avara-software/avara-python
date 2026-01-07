# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from avara.types import (
    OrgListResponse,
    OrgCreateResponse,
    OrgUpdateResponse,
    OrgRetrieveResponse,
    OrgDeactivateResponse,
    OrgReactivateResponse,
)
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorOrganizations, AsyncCursorOrganizations

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrgs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        org = client.orgs.create(
            org_name="City Medical Center - Radiology Department",
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        org = client.orgs.create(
            org_name="City Medical Center - Radiology Department",
            metadata={
                "department": "radiology",
                "region": "northeast",
            },
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.orgs.with_raw_response.create(
            org_name="City Medical Center - Radiology Department",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.orgs.with_streaming_response.create(
            org_name="City Medical Center - Radiology Department",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgCreateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        org = client.orgs.retrieve(
            "org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgRetrieveResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.orgs.with_raw_response.retrieve(
            "org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgRetrieveResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.orgs.with_streaming_response.retrieve(
            "org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgRetrieveResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Avara) -> None:
        org = client.orgs.update(
            org_id="org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Avara) -> None:
        org = client.orgs.update(
            org_id="org_1234567890abcdef1234567890abcdef",
            metadata={
                "department": "radiology",
                "region": "northeast",
                "wing": "Building A",
            },
            org_name="City Medical Center - Radiology & Imaging",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Avara) -> None:
        response = client.orgs.with_raw_response.update(
            org_id="org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Avara) -> None:
        with client.orgs.with_streaming_response.update(
            org_id="org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgUpdateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.with_raw_response.update(
                org_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        org = client.orgs.list()
        assert_matches_type(SyncCursorOrganizations[OrgListResponse], org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        org = client.orgs.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            limit=20,
        )
        assert_matches_type(SyncCursorOrganizations[OrgListResponse], org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.orgs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(SyncCursorOrganizations[OrgListResponse], org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.orgs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(SyncCursorOrganizations[OrgListResponse], org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: Avara) -> None:
        org = client.orgs.deactivate(
            "org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgDeactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: Avara) -> None:
        response = client.orgs.with_raw_response.deactivate(
            "org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgDeactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: Avara) -> None:
        with client.orgs.with_streaming_response.deactivate(
            "org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgDeactivateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reactivate(self, client: Avara) -> None:
        org = client.orgs.reactivate(
            "org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgReactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reactivate(self, client: Avara) -> None:
        response = client.orgs.with_raw_response.reactivate(
            "org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgReactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reactivate(self, client: Avara) -> None:
        with client.orgs.with_streaming_response.reactivate(
            "org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgReactivateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reactivate(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.with_raw_response.reactivate(
                "",
            )


class TestAsyncOrgs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.create(
            org_name="City Medical Center - Radiology Department",
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.create(
            org_name="City Medical Center - Radiology Department",
            metadata={
                "department": "radiology",
                "region": "northeast",
            },
        )
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.orgs.with_raw_response.create(
            org_name="City Medical Center - Radiology Department",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgCreateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.orgs.with_streaming_response.create(
            org_name="City Medical Center - Radiology Department",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgCreateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.retrieve(
            "org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgRetrieveResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.orgs.with_raw_response.retrieve(
            "org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgRetrieveResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.orgs.with_streaming_response.retrieve(
            "org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgRetrieveResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.update(
            org_id="org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.update(
            org_id="org_1234567890abcdef1234567890abcdef",
            metadata={
                "department": "radiology",
                "region": "northeast",
                "wing": "Building A",
            },
            org_name="City Medical Center - Radiology & Imaging",
        )
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAvara) -> None:
        response = await async_client.orgs.with_raw_response.update(
            org_id="org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgUpdateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAvara) -> None:
        async with async_client.orgs.with_streaming_response.update(
            org_id="org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgUpdateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.with_raw_response.update(
                org_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.list()
        assert_matches_type(AsyncCursorOrganizations[OrgListResponse], org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            limit=20,
        )
        assert_matches_type(AsyncCursorOrganizations[OrgListResponse], org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.orgs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(AsyncCursorOrganizations[OrgListResponse], org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.orgs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(AsyncCursorOrganizations[OrgListResponse], org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.deactivate(
            "org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgDeactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncAvara) -> None:
        response = await async_client.orgs.with_raw_response.deactivate(
            "org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgDeactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncAvara) -> None:
        async with async_client.orgs.with_streaming_response.deactivate(
            "org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgDeactivateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reactivate(self, async_client: AsyncAvara) -> None:
        org = await async_client.orgs.reactivate(
            "org_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(OrgReactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reactivate(self, async_client: AsyncAvara) -> None:
        response = await async_client.orgs.with_raw_response.reactivate(
            "org_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgReactivateResponse, org, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reactivate(self, async_client: AsyncAvara) -> None:
        async with async_client.orgs.with_streaming_response.reactivate(
            "org_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgReactivateResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reactivate(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.with_raw_response.reactivate(
                "",
            )
