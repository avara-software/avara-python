# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OrgReference"]


class OrgReference(BaseModel):
    """A reference to an organization with basic identifying information"""

    org_id: str = FieldInfo(alias="orgId")
    """Unique organization identifier. Format: org\\__{32-hex-chars}"""

    org_name: str = FieldInfo(alias="orgName")
    """Name of the organization"""
