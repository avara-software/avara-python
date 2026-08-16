# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.types.auto_scribe.studies import (
    ExternalCreateResponse,
    ExternalDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        external = client.auto_scribe.studies.external.create(
            report_metadata={},
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(ExternalCreateResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        external = client.auto_scribe.studies.external.create(
            report_metadata={
                "age": "38 years",
                "date_of_birth": "1985-07-20",
                "facility_name": "City Medical Center",
                "height": {
                    "unit": "cm",
                    "value": 165,
                },
                "mrn": "MRN-2024-001234",
                "patient_name": "Jane Doe",
                "procedure": "CT Chest",
                "referring_physician_name": "Dr. Michael Chen",
                "sex": "female",
                "study_date": "2024-01-15",
                "study_time": "14:30",
                "weight": {
                    "unit": "kg",
                    "value": 62,
                },
            },
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            external_patient_id="PAT-2024-7731",
            metadata={
                "department": "radiology",
                "priority": "routine",
            },
            modality="modality",
            reader_name="x",
            report_file_name="x",
            report_file_url="https://example.com",
            report_text="IMPRESSION: No acute cardiopulmonary process.",
            signed_at="x",
        )
        assert_matches_type(ExternalCreateResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.auto_scribe.studies.external.with_raw_response.create(
            report_metadata={},
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = response.parse()
        assert_matches_type(ExternalCreateResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.auto_scribe.studies.external.with_streaming_response.create(
            report_metadata={},
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = response.parse()
            assert_matches_type(ExternalCreateResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Avara) -> None:
        external = client.auto_scribe.studies.external.delete()
        assert_matches_type(ExternalDeleteResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Avara) -> None:
        external = client.auto_scribe.studies.external.delete(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(ExternalDeleteResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Avara) -> None:
        response = client.auto_scribe.studies.external.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = response.parse()
        assert_matches_type(ExternalDeleteResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Avara) -> None:
        with client.auto_scribe.studies.external.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = response.parse()
            assert_matches_type(ExternalDeleteResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExternal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        external = await async_client.auto_scribe.studies.external.create(
            report_metadata={},
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(ExternalCreateResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        external = await async_client.auto_scribe.studies.external.create(
            report_metadata={
                "age": "38 years",
                "date_of_birth": "1985-07-20",
                "facility_name": "City Medical Center",
                "height": {
                    "unit": "cm",
                    "value": 165,
                },
                "mrn": "MRN-2024-001234",
                "patient_name": "Jane Doe",
                "procedure": "CT Chest",
                "referring_physician_name": "Dr. Michael Chen",
                "sex": "female",
                "study_date": "2024-01-15",
                "study_time": "14:30",
                "weight": {
                    "unit": "kg",
                    "value": 62,
                },
            },
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
            express_customer_id="cus_1234567890abcdef1234567890abcdef",
            external_patient_id="PAT-2024-7731",
            metadata={
                "department": "radiology",
                "priority": "routine",
            },
            modality="modality",
            reader_name="x",
            report_file_name="x",
            report_file_url="https://example.com",
            report_text="IMPRESSION: No acute cardiopulmonary process.",
            signed_at="x",
        )
        assert_matches_type(ExternalCreateResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.external.with_raw_response.create(
            report_metadata={},
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = await response.parse()
        assert_matches_type(ExternalCreateResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.external.with_streaming_response.create(
            report_metadata={},
            severity="normal",
            study_description="CT Chest without contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = await response.parse()
            assert_matches_type(ExternalCreateResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAvara) -> None:
        external = await async_client.auto_scribe.studies.external.delete()
        assert_matches_type(ExternalDeleteResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAvara) -> None:
        external = await async_client.auto_scribe.studies.external.delete(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(ExternalDeleteResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.external.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external = await response.parse()
        assert_matches_type(ExternalDeleteResponse, external, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.external.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external = await response.parse()
            assert_matches_type(ExternalDeleteResponse, external, path=["response"])

        assert cast(Any, response.is_closed) is True
