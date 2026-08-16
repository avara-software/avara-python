# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorExternalReports, AsyncCursorExternalReports
from avara.types.auto_scribe.studies.external import (
    ReportListResponse,
    ReportCreateResponse,
    ReportRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        report = client.auto_scribe.studies.external.reports.create()
        assert_matches_type(ReportCreateResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        report = client.auto_scribe.studies.external.reports.create(
            reader_name="x",
            report_file_name="x",
            report_file_url="https://example.com",
            report_text="x",
            signed_at="x",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(ReportCreateResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.auto_scribe.studies.external.reports.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCreateResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.auto_scribe.studies.external.reports.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCreateResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        report = client.auto_scribe.studies.external.reports.retrieve(
            "ext_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.auto_scribe.studies.external.reports.with_raw_response.retrieve(
            "ext_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.auto_scribe.studies.external.reports.with_streaming_response.retrieve(
            "ext_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrieveResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_report_id` but received ''"):
            client.auto_scribe.studies.external.reports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        report = client.auto_scribe.studies.external.reports.list()
        assert_matches_type(SyncCursorExternalReports[ReportListResponse], report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        report = client.auto_scribe.studies.external.reports.list(
            cursor="cursor",
            limit=20,
            study_id="stu_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(SyncCursorExternalReports[ReportListResponse], report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.auto_scribe.studies.external.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(SyncCursorExternalReports[ReportListResponse], report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.auto_scribe.studies.external.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(SyncCursorExternalReports[ReportListResponse], report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.studies.external.reports.create()
        assert_matches_type(ReportCreateResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.studies.external.reports.create(
            reader_name="x",
            report_file_name="x",
            report_file_url="https://example.com",
            report_text="x",
            signed_at="x",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(ReportCreateResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.external.reports.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCreateResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.external.reports.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCreateResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.studies.external.reports.retrieve(
            "ext_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.external.reports.with_raw_response.retrieve(
            "ext_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.external.reports.with_streaming_response.retrieve(
            "ext_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrieveResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_report_id` but received ''"):
            await async_client.auto_scribe.studies.external.reports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.studies.external.reports.list()
        assert_matches_type(AsyncCursorExternalReports[ReportListResponse], report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.studies.external.reports.list(
            cursor="cursor",
            limit=20,
            study_id="stu_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(AsyncCursorExternalReports[ReportListResponse], report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.external.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(AsyncCursorExternalReports[ReportListResponse], report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.external.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(AsyncCursorExternalReports[ReportListResponse], report, path=["response"])

        assert cast(Any, response.is_closed) is True
