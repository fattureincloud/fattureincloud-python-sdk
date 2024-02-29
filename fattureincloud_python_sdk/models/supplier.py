# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.32
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.supplier_type import SupplierType
from typing import Optional, Set
from typing_extensions import Self


class Supplier(BaseModel):
    """
    Supplier
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Supplier id")
    code: Optional[StrictStr] = Field(default=None, description="Supplier code")
    name: Optional[StrictStr] = Field(default=None, description="Supplier name")
    type: Optional[SupplierType] = None
    first_name: Optional[StrictStr] = Field(
        default=None, description="Supplier first name"
    )
    last_name: Optional[StrictStr] = Field(
        default=None, description="Supplier last name"
    )
    contact_person: Optional[StrictStr] = Field(
        default=None, description="Supplier contact person"
    )
    vat_number: Optional[StrictStr] = Field(
        default=None, description="Supplier vat number"
    )
    tax_code: Optional[StrictStr] = Field(default=None, description="Supplier tax code")
    address_street: Optional[StrictStr] = Field(
        default=None, description="Supplier street address"
    )
    address_postal_code: Optional[StrictStr] = Field(
        default=None, description="Supplier postal code"
    )
    address_city: Optional[StrictStr] = Field(default=None, description="Supplier city")
    address_province: Optional[StrictStr] = Field(
        default=None, description="Supplier province"
    )
    address_extra: Optional[StrictStr] = Field(
        default=None, description="Supplier address extra info"
    )
    country: Optional[StrictStr] = Field(default=None, description="Supplier country")
    country_iso: Optional[StrictStr] = Field(
        default=None, description="Supplier country iso code"
    )
    email: Optional[StrictStr] = Field(default=None, description="Supplier email")
    certified_email: Optional[StrictStr] = Field(
        default=None, description="Supplier certified email"
    )
    phone: Optional[StrictStr] = Field(default=None, description="Supplier phone")
    fax: Optional[StrictStr] = Field(default=None, description="Supplier fax")
    notes: Optional[StrictStr] = Field(default=None, description="Supplier extra notes")
    bank_iban: Optional[StrictStr] = Field(
        default=None, description="Supplier bank IBAN"
    )
    created_at: Optional[StrictStr] = Field(
        default=None, description="Supplier creation date"
    )
    updated_at: Optional[StrictStr] = Field(
        default=None, description="Supplier last update date"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "code",
        "name",
        "type",
        "first_name",
        "last_name",
        "contact_person",
        "vat_number",
        "tax_code",
        "address_street",
        "address_postal_code",
        "address_city",
        "address_province",
        "address_extra",
        "country",
        "country_iso",
        "email",
        "certified_email",
        "phone",
        "fax",
        "notes",
        "bank_iban",
        "created_at",
        "updated_at",
    ]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Supplier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Supplier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "code": obj.get("code"),
                "name": obj.get("name"),
                "type": obj.get("type"),
                "first_name": obj.get("first_name"),
                "last_name": obj.get("last_name"),
                "contact_person": obj.get("contact_person"),
                "vat_number": obj.get("vat_number"),
                "tax_code": obj.get("tax_code"),
                "address_street": obj.get("address_street"),
                "address_postal_code": obj.get("address_postal_code"),
                "address_city": obj.get("address_city"),
                "address_province": obj.get("address_province"),
                "address_extra": obj.get("address_extra"),
                "country": obj.get("country"),
                "country_iso": obj.get("country_iso"),
                "email": obj.get("email"),
                "certified_email": obj.get("certified_email"),
                "phone": obj.get("phone"),
                "fax": obj.get("fax"),
                "notes": obj.get("notes"),
                "bank_iban": obj.get("bank_iban"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
