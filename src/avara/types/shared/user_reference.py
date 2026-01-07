# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserReference"]


class UserReference(BaseModel):
    """A reference to a user with basic identifying information"""

    email: str
    """User's email address"""

    user_id: str = FieldInfo(alias="userId")
    """Unique user identifier. Format: usr\\__{32-hex-chars}"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """User's first name"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """User's last name"""

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)
    """User's middle name"""

    suffix1: Optional[str] = None
    """Name suffix (e.g., 'MD', 'Jr.')"""

    suffix2: Optional[str] = None
    """Additional name suffix"""
