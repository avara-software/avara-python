# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserReference"]


class UserReference(BaseModel):
    """A reference to a user with basic identifying information"""

    email: str

    user_id: str = FieldInfo(alias="userId")

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)

    suffix1: Optional[str] = None

    suffix2: Optional[str] = None
