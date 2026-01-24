# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncCursorUsers",
    "AsyncCursorUsers",
    "SyncCursorStudies",
    "AsyncCursorStudies",
    "SyncCursorInvitations",
    "AsyncCursorInvitations",
    "SyncCursorExpressCustomers",
    "AsyncCursorExpressCustomers",
]

_T = TypeVar("_T")


class SyncCursorUsers(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    users: List[_T]
    """Array of user objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        users = self.users
        if not users:
            return []
        return users

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorUsers(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    users: List[_T]
    """Array of user objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        users = self.users
        if not users:
            return []
        return users

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class SyncCursorStudies(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    studies: List[_T]
    """Array of study objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        studies = self.studies
        if not studies:
            return []
        return studies

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorStudies(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    studies: List[_T]
    """Array of study objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        studies = self.studies
        if not studies:
            return []
        return studies

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class SyncCursorInvitations(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    invitations: List[_T]
    """Array of invitation objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        invitations = self.invitations
        if not invitations:
            return []
        return invitations

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorInvitations(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    invitations: List[_T]
    """Array of invitation objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        invitations = self.invitations
        if not invitations:
            return []
        return invitations

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class SyncCursorExpressCustomers(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    express_customers: List[_T] = FieldInfo(alias="expressCustomers")
    """Array of Express customer objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        express_customers = self.express_customers
        if not express_customers:
            return []
        return express_customers

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorExpressCustomers(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    express_customers: List[_T] = FieldInfo(alias="expressCustomers")
    """Array of Express customer objects"""
    cursor: Optional[str] = None
    """Next page cursor. Pass this to the next request to get the next page of results"""
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether there are more results available"""

    @override
    def _get_page_items(self) -> List[_T]:
        express_customers = self.express_customers
        if not express_customers:
            return []
        return express_customers

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.cursor
        if not cursor:
            return None

        return PageInfo(params={"cursor": cursor})
