# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorInvitations, AsyncCursorInvitations
from avara.types.viewer.users import (
    InvitationListResponse,
    InvitationRevokeResponse,
    InvitationUpdateResponse,
    InvitationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvitations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.retrieve(
            "inv_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.viewer.users.invitations.with_raw_response.retrieve(
            "inv_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.viewer.users.invitations.with_streaming_response.retrieve(
            "inv_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.viewer.users.invitations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
            can_manage_studies=True,
            clinic_role="Radiologist",
            first_name="Michael",
            has_dashboard_access=True,
            last_name="Chen",
            level="admin",
            middle_name="x",
            phone_number="5551234567",
            suffix1="x",
            suffix2="x",
        )
        assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Avara) -> None:
        response = client.viewer.users.invitations.with_raw_response.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Avara) -> None:
        with client.viewer.users.invitations.with_streaming_response.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.viewer.users.invitations.with_raw_response.update(
                invitation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.list()
        assert_matches_type(SyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            end_date="2024-12-31",
            expired="not-expired",
            limit=20,
            start_date="2024-01-01",
            status=["sent"],
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(SyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.viewer.users.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(SyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.viewer.users.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(SyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.revoke()
        assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_with_all_params(self, client: Avara) -> None:
        invitation = client.viewer.users.invitations.revoke(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Avara) -> None:
        response = client.viewer.users.invitations.with_raw_response.revoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Avara) -> None:
        with client.viewer.users.invitations.with_streaming_response.revoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvitations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.retrieve(
            "inv_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.invitations.with_raw_response.retrieve(
            "inv_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.invitations.with_streaming_response.retrieve(
            "inv_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationRetrieveResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.viewer.users.invitations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
            can_manage_studies=True,
            clinic_role="Radiologist",
            first_name="Michael",
            has_dashboard_access=True,
            last_name="Chen",
            level="admin",
            middle_name="x",
            phone_number="5551234567",
            suffix1="x",
            suffix2="x",
        )
        assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.invitations.with_raw_response.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.invitations.with_streaming_response.update(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationUpdateResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.viewer.users.invitations.with_raw_response.update(
                invitation_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.list()
        assert_matches_type(AsyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            end_date="2024-12-31",
            expired="not-expired",
            limit=20,
            start_date="2024-01-01",
            status=["sent"],
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(AsyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(AsyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(AsyncCursorInvitations[InvitationListResponse], invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.revoke()
        assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_with_all_params(self, async_client: AsyncAvara) -> None:
        invitation = await async_client.viewer.users.invitations.revoke(
            invitation_id="inv_1234567890abcdef1234567890abcdef",
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.invitations.with_raw_response.revoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.invitations.with_streaming_response.revoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationRevokeResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True
