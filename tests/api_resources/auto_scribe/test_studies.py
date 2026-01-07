# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorStudies, AsyncCursorStudies
from avara.types.auto_scribe import (
    StudyListResponse,
    StudyCancelResponse,
    StudyCreateResponse,
    StudyUpdateResponse,
    StudyRetrieveResponse,
    StudyUncancelResponse,
    StudyRerouteURLResponse,
    StudyRetrieveByUidResponse,
    StudyViewerOnlyRerouteURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStudies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        study = client.auto_scribe.studies.create(
            report_metadata={},
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyCreateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.create(
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
                "referring_physician_name": "Dr. Michael Chen",
                "scan_date": "2024-03-15",
                "scan_time": "14:30",
                "scan_type": "MRI Brain with Contrast",
                "sex": "female",
                "weight": {
                    "unit": "kg",
                    "value": 62,
                },
            },
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
            assigned_to="usr_1234567890abcdef1234567890abcdef",
            metadata={
                "department": "radiology",
                "priority": "routine",
            },
            org_id="org_1234567890abcdef1234567890abcdef",
            prior_report_texts=["x"],
            prior_study_ids=["string"],
        )
        assert_matches_type(StudyCreateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.create(
            report_metadata={},
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyCreateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.create(
            report_metadata={},
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyCreateResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        study = client.auto_scribe.studies.retrieve(
            "stu_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyRetrieveResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.retrieve(
            "stu_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyRetrieveResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.retrieve(
            "stu_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyRetrieveResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `study_id` but received ''"):
            client.auto_scribe.studies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Avara) -> None:
        study = client.auto_scribe.studies.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyUpdateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
            assigned_to="usr_1234567890abcdef1234567890abcdef",
            metadata={"foo": "string"},
            org_id="org_1234567890abcdef1234567890abcdef",
            prior_report_texts=["x"],
            prior_study_ids=["string"],
            report_metadata={
                "age": "age",
                "date_of_birth": "7321-69-10",
                "facility_name": "facilityName",
                "height": {
                    "unit": "cm",
                    "value": 170,
                },
                "mrn": "mrn",
                "patient_name": "Jane M. Doe",
                "referring_physician_name": "referringPhysicianName",
                "scan_date": "7321-69-10",
                "scan_time": "scanTime",
                "scan_type": "scanType",
                "sex": "female",
                "weight": {
                    "unit": "kg",
                    "value": 68,
                },
            },
            severity="high",
            study_description="Brain MRI with and without Contrast",
        )
        assert_matches_type(StudyUpdateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyUpdateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyUpdateResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `study_id` but received ''"):
            client.auto_scribe.studies.with_raw_response.update(
                study_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        study = client.auto_scribe.studies.list()
        assert_matches_type(SyncCursorStudies[StudyListResponse], study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.list(
            assigned_to="usr_1234567890abcdef1234567890abcdef",
            cursor="eyJvZmZzZXQiOjIwfQ==",
            is_cancelled=False,
            limit=20,
            severity="normal",
            study_description="CT Head",
            study_report_status=["completed"],
        )
        assert_matches_type(SyncCursorStudies[StudyListResponse], study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(SyncCursorStudies[StudyListResponse], study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(SyncCursorStudies[StudyListResponse], study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Avara) -> None:
        study = client.auto_scribe.studies.cancel()
        assert_matches_type(StudyCancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.cancel(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyCancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.cancel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyCancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.cancel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyCancelResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reroute_url(self, client: Avara) -> None:
        study = client.auto_scribe.studies.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reroute_url_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reroute_url(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reroute_url(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_by_uid(self, client: Avara) -> None:
        study = client.auto_scribe.studies.retrieve_by_uid(
            "1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(StudyRetrieveByUidResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_uid(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.retrieve_by_uid(
            "1.2.840.10008.5.1.4.1.1.2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyRetrieveByUidResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_uid(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.retrieve_by_uid(
            "1.2.840.10008.5.1.4.1.1.2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyRetrieveByUidResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_uid(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `study_instance_uid` but received ''"):
            client.auto_scribe.studies.with_raw_response.retrieve_by_uid(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_uncancel(self, client: Avara) -> None:
        study = client.auto_scribe.studies.uncancel()
        assert_matches_type(StudyUncancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_uncancel_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.uncancel(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyUncancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_uncancel(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.uncancel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyUncancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_uncancel(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.uncancel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyUncancelResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_viewer_only_reroute_url(self, client: Avara) -> None:
        study = client.auto_scribe.studies.viewer_only_reroute_url()
        assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_viewer_only_reroute_url_with_all_params(self, client: Avara) -> None:
        study = client.auto_scribe.studies.viewer_only_reroute_url(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_viewer_only_reroute_url(self, client: Avara) -> None:
        response = client.auto_scribe.studies.with_raw_response.viewer_only_reroute_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = response.parse()
        assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_viewer_only_reroute_url(self, client: Avara) -> None:
        with client.auto_scribe.studies.with_streaming_response.viewer_only_reroute_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = response.parse()
            assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStudies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.create(
            report_metadata={},
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyCreateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.create(
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
                "referring_physician_name": "Dr. Michael Chen",
                "scan_date": "2024-03-15",
                "scan_time": "14:30",
                "scan_type": "MRI Brain with Contrast",
                "sex": "female",
                "weight": {
                    "unit": "kg",
                    "value": 62,
                },
            },
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
            assigned_to="usr_1234567890abcdef1234567890abcdef",
            metadata={
                "department": "radiology",
                "priority": "routine",
            },
            org_id="org_1234567890abcdef1234567890abcdef",
            prior_report_texts=["x"],
            prior_study_ids=["string"],
        )
        assert_matches_type(StudyCreateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.create(
            report_metadata={},
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyCreateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.create(
            report_metadata={},
            severity="normal",
            study_description="Brain MRI with Contrast",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyCreateResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.retrieve(
            "stu_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyRetrieveResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.retrieve(
            "stu_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyRetrieveResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.retrieve(
            "stu_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyRetrieveResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `study_id` but received ''"):
            await async_client.auto_scribe.studies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyUpdateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
            assigned_to="usr_1234567890abcdef1234567890abcdef",
            metadata={"foo": "string"},
            org_id="org_1234567890abcdef1234567890abcdef",
            prior_report_texts=["x"],
            prior_study_ids=["string"],
            report_metadata={
                "age": "age",
                "date_of_birth": "7321-69-10",
                "facility_name": "facilityName",
                "height": {
                    "unit": "cm",
                    "value": 170,
                },
                "mrn": "mrn",
                "patient_name": "Jane M. Doe",
                "referring_physician_name": "referringPhysicianName",
                "scan_date": "7321-69-10",
                "scan_time": "scanTime",
                "scan_type": "scanType",
                "sex": "female",
                "weight": {
                    "unit": "kg",
                    "value": 68,
                },
            },
            severity="high",
            study_description="Brain MRI with and without Contrast",
        )
        assert_matches_type(StudyUpdateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyUpdateResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.update(
            study_id="stu_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyUpdateResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `study_id` but received ''"):
            await async_client.auto_scribe.studies.with_raw_response.update(
                study_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.list()
        assert_matches_type(AsyncCursorStudies[StudyListResponse], study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.list(
            assigned_to="usr_1234567890abcdef1234567890abcdef",
            cursor="eyJvZmZzZXQiOjIwfQ==",
            is_cancelled=False,
            limit=20,
            severity="normal",
            study_description="CT Head",
            study_report_status=["completed"],
        )
        assert_matches_type(AsyncCursorStudies[StudyListResponse], study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(AsyncCursorStudies[StudyListResponse], study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(AsyncCursorStudies[StudyListResponse], study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.cancel()
        assert_matches_type(StudyCancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.cancel(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyCancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.cancel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyCancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.cancel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyCancelResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reroute_url(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reroute_url_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reroute_url(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reroute_url(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.reroute_url(
            assigned_to_user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyRerouteURLResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_by_uid(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.retrieve_by_uid(
            "1.2.840.10008.5.1.4.1.1.2",
        )
        assert_matches_type(StudyRetrieveByUidResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_uid(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.retrieve_by_uid(
            "1.2.840.10008.5.1.4.1.1.2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyRetrieveByUidResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_uid(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.retrieve_by_uid(
            "1.2.840.10008.5.1.4.1.1.2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyRetrieveByUidResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_uid(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `study_instance_uid` but received ''"):
            await async_client.auto_scribe.studies.with_raw_response.retrieve_by_uid(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_uncancel(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.uncancel()
        assert_matches_type(StudyUncancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_uncancel_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.uncancel(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
        )
        assert_matches_type(StudyUncancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_uncancel(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.uncancel()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyUncancelResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_uncancel(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.uncancel() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyUncancelResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_viewer_only_reroute_url(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.viewer_only_reroute_url()
        assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_viewer_only_reroute_url_with_all_params(self, async_client: AsyncAvara) -> None:
        study = await async_client.auto_scribe.studies.viewer_only_reroute_url(
            study_id="stu_1234567890abcdef1234567890abcdef",
            study_instance_uid="1.2.840.113619.2.55.3.604688119.868.1234567890.123",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_viewer_only_reroute_url(self, async_client: AsyncAvara) -> None:
        response = await async_client.auto_scribe.studies.with_raw_response.viewer_only_reroute_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        study = await response.parse()
        assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_viewer_only_reroute_url(self, async_client: AsyncAvara) -> None:
        async with async_client.auto_scribe.studies.with_streaming_response.viewer_only_reroute_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            study = await response.parse()
            assert_matches_type(StudyViewerOnlyRerouteURLResponse, study, path=["response"])

        assert cast(Any, response.is_closed) is True
