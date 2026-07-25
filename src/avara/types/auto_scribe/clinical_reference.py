# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..clinical_reference_type import ClinicalReferenceType
from ..shared.express_customer_reference import ExpressCustomerReference

__all__ = ["ClinicalReference"]


class ClinicalReference(BaseModel):
    """
    A canonical clinical reference value for study workflow pickers and normalization
    """

    clinical_reference_id: str = FieldInfo(alias="clinicalReferenceId")
    """Unique clinical reference identifier. Format: ref\\__{32-hex-chars}"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the clinical reference was created"""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether this reference is active and available for pickers"""

    name: str
    """Canonical display name for this reference value"""

    type: ClinicalReferenceType
    """
    Category of canonical clinical reference value used for study workflow pickers
    and normalization.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the clinical reference was last updated"""

    express_customer: Optional[ExpressCustomerReference] = FieldInfo(alias="expressCustomer", default=None)
    """A reference to an Express customer with basic identifying information"""

    external_reference_id: Optional[str] = FieldInfo(alias="externalReferenceId", default=None)
    """Integrator-provided stable identifier for mapping inbound data"""

    metadata: Optional[Dict[str, str]] = None
    """Optional key-value metadata. Maximum 50 pairs"""
