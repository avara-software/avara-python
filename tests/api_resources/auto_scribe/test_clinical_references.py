# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorClinicalReferences, AsyncCursorClinicalReferences
from avara.types.auto_scribe import (
    ClinicalReference,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClinicalReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.create(
            name="City Medical Center",
            type="facility",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.create(
            name="City Medical Center",
            type="facility",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            external_reference_id="FAC-001",
            metadata={"region": "northeast"},
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.auto_scribe.clinical_references.with_raw_response.create(
            name="City Medical Center",
            type="facility",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.auto_scribe.clinical_references.with_streaming_response.create(
            name="City Medical Center",
            type="facility",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.retrieve(
            "ref_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.auto_scribe.clinical_references.with_raw_response.retrieve(
            "ref_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.auto_scribe.clinical_references.with_streaming_response.retrieve(
            "ref_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clinical_reference_id` but received ''"):
            client.auto_scribe.clinical_references.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            metadata={
                "region": "northeast",
                "wing": "Building A",
            },
            name="City Medical Center - Main Campus",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Avara) -> None:
        response = client.auto_scribe.clinical_references.with_raw_response.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Avara) -> None:
        with client.auto_scribe.clinical_references.with_streaming_response.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clinical_reference_id` but received ''"):
            client.auto_scribe.clinical_references.with_raw_response.update(
                clinical_reference_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.list()
        assert_matches_type(SyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.list(
            cursor="eyJjcmVhdGVkQXQiOiIyMDI0LTAxLTE1VDA5OjAwOjAwWiJ9",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            is_active=True,
            limit=20,
            type="facility",
        )
        assert_matches_type(SyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.auto_scribe.clinical_references.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = response.parse()
        assert_matches_type(SyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.auto_scribe.clinical_references.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = response.parse()
            assert_matches_type(SyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.delete(
            "ref_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Avara) -> None:
        response = client.auto_scribe.clinical_references.with_raw_response.delete(
            "ref_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Avara) -> None:
        with client.auto_scribe.clinical_references.with_streaming_response.delete(
            "ref_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clinical_reference_id` but received ''"):
            client.auto_scribe.clinical_references.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_external_reference_id(self, client: Avara) -> None:
        clinical_reference = client.auto_scribe.clinical_references.retrieve_by_external_reference_id(
            "FAC-001",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_external_reference_id(self, client: Avara) -> None:
        response = client.auto_scribe.clinical_references.with_raw_response.retrieve_by_external_reference_id(
            "FAC-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_external_reference_id(self, client: Avara) -> None:
        with client.auto_scribe.clinical_references.with_streaming_response.retrieve_by_external_reference_id(
            "FAC-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_external_reference_id(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_reference_id` but received ''"):
            client.auto_scribe.clinical_references.with_raw_response.retrieve_by_external_reference_id(
                "",
            )


class TestAsyncClinicalReferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.create(
            name="City Medical Center",
            type="facility",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.create(
            name="City Medical Center",
            type="facility",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            external_reference_id="FAC-001",
            metadata={"region": "northeast"},
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.clinical_references.with_raw_response.create(
            name="City Medical Center",
            type="facility",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = await response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.clinical_references.with_streaming_response.create(
            name="City Medical Center",
            type="facility",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = await response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.retrieve(
            "ref_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.clinical_references.with_raw_response.retrieve(
            "ref_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = await response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.clinical_references.with_streaming_response.retrieve(
            "ref_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = await response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clinical_reference_id` but received ''"):
            await async_client.auto_scribe.clinical_references.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            metadata={
                "region": "northeast",
                "wing": "Building A",
            },
            name="City Medical Center - Main Campus",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.clinical_references.with_raw_response.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = await response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.clinical_references.with_streaming_response.update(
            clinical_reference_id="ref_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = await response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clinical_reference_id` but received ''"):
            await async_client.auto_scribe.clinical_references.with_raw_response.update(
                clinical_reference_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.list()
        assert_matches_type(AsyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.list(
            cursor="eyJjcmVhdGVkQXQiOiIyMDI0LTAxLTE1VDA5OjAwOjAwWiJ9",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            is_active=True,
            limit=20,
            type="facility",
        )
        assert_matches_type(AsyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.clinical_references.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = await response.parse()
        assert_matches_type(AsyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.clinical_references.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = await response.parse()
            assert_matches_type(AsyncCursorClinicalReferences[ClinicalReference], clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.delete(
            "ref_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.clinical_references.with_raw_response.delete(
            "ref_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = await response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.clinical_references.with_streaming_response.delete(
            "ref_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = await response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clinical_reference_id` but received ''"):
            await async_client.auto_scribe.clinical_references.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_external_reference_id(self, async_client: AsyncAvara) -> None:
        clinical_reference = await async_client.auto_scribe.clinical_references.retrieve_by_external_reference_id(
            "FAC-001",
        )
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_external_reference_id(self, async_client: AsyncAvara) -> None:
        response = (
            await async_client.auto_scribe.clinical_references.with_raw_response.retrieve_by_external_reference_id(
                "FAC-001",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clinical_reference = await response.parse()
        assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_external_reference_id(self, async_client: AsyncAvara) -> None:
        async with (
            async_client.auto_scribe.clinical_references.with_streaming_response.retrieve_by_external_reference_id(
                "FAC-001",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clinical_reference = await response.parse()
            assert_matches_type(ClinicalReference, clinical_reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_external_reference_id(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_reference_id` but received ''"):
            await async_client.auto_scribe.clinical_references.with_raw_response.retrieve_by_external_reference_id(
                "",
            )
