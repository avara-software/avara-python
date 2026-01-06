# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.types.auto_scribe import (
    ReportPdfResponse,
    ReportListResponse,
    ReportTextResponse,
    ReportAddendumResponse,
    ReportCancelAddendumResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        report = client.auto_scribe.reports.list()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        report = client.auto_scribe.reports.list(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.auto_scribe.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.auto_scribe.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportListResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_addendum(self, client: Avara) -> None:
        report = client.auto_scribe.reports.addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ReportAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_addendum(self, client: Avara) -> None:
        response = client.auto_scribe.reports.with_raw_response.addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_addendum(self, client: Avara) -> None:
        with client.auto_scribe.reports.with_streaming_response.addendum(
            "rep_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportAddendumResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_addendum(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.auto_scribe.reports.with_raw_response.addendum(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_addendum(self, client: Avara) -> None:
        report = client.auto_scribe.reports.cancel_addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ReportCancelAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel_addendum(self, client: Avara) -> None:
        response = client.auto_scribe.reports.with_raw_response.cancel_addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportCancelAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel_addendum(self, client: Avara) -> None:
        with client.auto_scribe.reports.with_streaming_response.cancel_addendum(
            "rep_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportCancelAddendumResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel_addendum(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.auto_scribe.reports.with_raw_response.cancel_addendum(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pdf(self, client: Avara) -> None:
        report = client.auto_scribe.reports.pdf()
        assert_matches_type(ReportPdfResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pdf_with_all_params(self, client: Avara) -> None:
        report = client.auto_scribe.reports.pdf(
            report_id="rep_1234567890abcdef1234567890abcdef",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(ReportPdfResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_pdf(self, client: Avara) -> None:
        response = client.auto_scribe.reports.with_raw_response.pdf()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportPdfResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_pdf(self, client: Avara) -> None:
        with client.auto_scribe.reports.with_streaming_response.pdf() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportPdfResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_text(self, client: Avara) -> None:
        report = client.auto_scribe.reports.text()
        assert_matches_type(ReportTextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_text_with_all_params(self, client: Avara) -> None:
        report = client.auto_scribe.reports.text(
            report_id="rep_1234567890abcdef1234567890abcdef",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(ReportTextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_text(self, client: Avara) -> None:
        response = client.auto_scribe.reports.with_raw_response.text()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportTextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_text(self, client: Avara) -> None:
        with client.auto_scribe.reports.with_streaming_response.text() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportTextResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.list()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.list(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportListResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_addendum(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ReportAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_addendum(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.reports.with_raw_response.addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_addendum(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.reports.with_streaming_response.addendum(
            "rep_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportAddendumResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_addendum(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.auto_scribe.reports.with_raw_response.addendum(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_addendum(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.cancel_addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(ReportCancelAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel_addendum(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.reports.with_raw_response.cancel_addendum(
            "rep_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportCancelAddendumResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_addendum(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.reports.with_streaming_response.cancel_addendum(
            "rep_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportCancelAddendumResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel_addendum(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.auto_scribe.reports.with_raw_response.cancel_addendum(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pdf(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.pdf()
        assert_matches_type(ReportPdfResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pdf_with_all_params(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.pdf(
            report_id="rep_1234567890abcdef1234567890abcdef",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(ReportPdfResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_pdf(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.reports.with_raw_response.pdf()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportPdfResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_pdf(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.reports.with_streaming_response.pdf() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportPdfResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_text(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.text()
        assert_matches_type(ReportTextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncAvara) -> None:
        report = await async_client.auto_scribe.reports.text(
            report_id="rep_1234567890abcdef1234567890abcdef",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(ReportTextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_text(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.reports.with_raw_response.text()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportTextResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.reports.with_streaming_response.text() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportTextResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
