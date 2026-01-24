# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExpressCustomerReference"]


class ExpressCustomerReference(BaseModel):
    """A reference to an Express customer with basic identifying information"""

    express_customer_id: str = FieldInfo(alias="expressCustomerId")
    """Unique Express customer identifier. Format: cus\\__{32-hex-chars}"""

    express_customer_name: str = FieldInfo(alias="expressCustomerName")
    """Name of the Express customer"""
