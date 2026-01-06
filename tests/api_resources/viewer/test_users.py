# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avara import Avara, AsyncAvara
from tests.utils import assert_matches_type
from avara.pagination import SyncCursorUsers, AsyncCursorUsers
from avara.types.viewer import (
    UserListResponse,
    UserCreateResponse,
    UserUpdateResponse,
    UserRetrieveResponse,
    UserReactivateResponse,
    UserRevokeAccessResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Avara) -> None:
        user = client.viewer.users.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Avara) -> None:
        user = client.viewer.users.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
            middle_name="x",
            phone_number="321669910225610",
            suffix1="x",
            suffix2="x",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Avara) -> None:
        response = client.viewer.users.with_raw_response.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Avara) -> None:
        with client.viewer.users.with_streaming_response.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Avara) -> None:
        user = client.viewer.users.retrieve(
            "usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Avara) -> None:
        response = client.viewer.users.with_raw_response.retrieve(
            "usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Avara) -> None:
        with client.viewer.users.with_streaming_response.retrieve(
            "usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.viewer.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Avara) -> None:
        user = client.viewer.users.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Avara) -> None:
        user = client.viewer.users.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
            can_manage_studies=True,
            clinic_role="Radiologist",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
            middle_name="x",
            phone_number="321669910225610",
            suffix1="x",
            suffix2="x",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Avara) -> None:
        response = client.viewer.users.with_raw_response.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Avara) -> None:
        with client.viewer.users.with_streaming_response.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Avara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.viewer.users.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Avara) -> None:
        user = client.viewer.users.list()
        assert_matches_type(SyncCursorUsers[UserListResponse], user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Avara) -> None:
        user = client.viewer.users.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            email="user@example.com",
            first_name="John",
            invited_source="api",
            last_name="Doe",
            level="member",
            limit=20,
        )
        assert_matches_type(SyncCursorUsers[UserListResponse], user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Avara) -> None:
        response = client.viewer.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncCursorUsers[UserListResponse], user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Avara) -> None:
        with client.viewer.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncCursorUsers[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reactivate(self, client: Avara) -> None:
        user = client.viewer.users.reactivate(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(UserReactivateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reactivate(self, client: Avara) -> None:
        response = client.viewer.users.with_raw_response.reactivate(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserReactivateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reactivate(self, client: Avara) -> None:
        with client.viewer.users.with_streaming_response.reactivate(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserReactivateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revoke_access(self, client: Avara) -> None:
        user = client.viewer.users.revoke_access(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(UserRevokeAccessResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revoke_access(self, client: Avara) -> None:
        response = client.viewer.users.with_raw_response.revoke_access(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRevokeAccessResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revoke_access(self, client: Avara) -> None:
        with client.viewer.users.with_streaming_response.revoke_access(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRevokeAccessResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
            middle_name="x",
            phone_number="321669910225610",
            suffix1="x",
            suffix2="x",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.with_raw_response.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.with_streaming_response.create(
            can_manage_studies=True,
            clinic_role="Radiologist",
            email="S%+_FW+l+.n-@1F.-.eVZe",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.retrieve(
            "usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.with_raw_response.retrieve(
            "usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.with_streaming_response.retrieve(
            "usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.viewer.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
            can_manage_studies=True,
            clinic_role="Radiologist",
            first_name="x",
            has_dashboard_access=True,
            last_name="x",
            level="admin",
            middle_name="x",
            phone_number="321669910225610",
            suffix1="x",
            suffix2="x",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.with_raw_response.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.with_streaming_response.update(
            user_id="usr_1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncAvara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.viewer.users.with_raw_response.update(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.list()
        assert_matches_type(AsyncCursorUsers[UserListResponse], user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.list(
            cursor="eyJvZmZzZXQiOjIwfQ==",
            email="user@example.com",
            first_name="John",
            invited_source="api",
            last_name="Doe",
            level="member",
            limit=20,
        )
        assert_matches_type(AsyncCursorUsers[UserListResponse], user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncCursorUsers[UserListResponse], user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncCursorUsers[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reactivate(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.reactivate(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(UserReactivateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reactivate(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.with_raw_response.reactivate(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserReactivateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reactivate(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.with_streaming_response.reactivate(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserReactivateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revoke_access(self, async_client: AsyncAvara) -> None:
        user = await async_client.viewer.users.revoke_access(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )
        assert_matches_type(UserRevokeAccessResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revoke_access(self, async_client: AsyncAvara) -> None:
        response = await async_client.viewer.users.with_raw_response.revoke_access(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRevokeAccessResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_access(self, async_client: AsyncAvara) -> None:
        async with async_client.viewer.users.with_streaming_response.revoke_access(
            user_id="usr_E1CB97d8EBbDbaAae6d9B1ca0D1cFaAD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRevokeAccessResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
