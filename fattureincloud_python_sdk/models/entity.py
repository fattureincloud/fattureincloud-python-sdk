# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.3
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fattureincloud_python_sdk.models.entity_type import EntityType
from fattureincloud_python_sdk.models.payment_method import PaymentMethod
from fattureincloud_python_sdk.models.payment_terms_type import PaymentTermsType
from fattureincloud_python_sdk.models.vat_type import VatType
from typing import Optional, Set
from typing_extensions import Self


class Entity(BaseModel):
    """
    Entity
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Entity id")
    code: Optional[StrictStr] = Field(default=None, description="Entity code")
    name: Optional[StrictStr] = Field(default=None, description="Entity name")
    type: Optional[EntityType] = None
    first_name: Optional[StrictStr] = Field(
        default=None, description="Entity first name"
    )
    last_name: Optional[StrictStr] = Field(default=None, description="Entity last name")
    contact_person: Optional[StrictStr] = Field(
        default=None, description="Entity contact person"
    )
    vat_number: Optional[StrictStr] = Field(
        default=None, description="Entity vat number"
    )
    tax_code: Optional[StrictStr] = Field(default=None, description="Entity tax code")
    address_street: Optional[StrictStr] = Field(
        default=None, description="Entitity address street"
    )
    address_postal_code: Optional[StrictStr] = Field(
        default=None, description="Entity address postal code"
    )
    address_city: Optional[StrictStr] = Field(
        default=None, description="Entity address city"
    )
    address_province: Optional[StrictStr] = Field(
        default=None, description="Entity address province"
    )
    address_extra: Optional[StrictStr] = Field(
        default=None, description="Entity address extra info"
    )
    country: Optional[StrictStr] = Field(default=None, description="Entity country")
    country_iso: Optional[StrictStr] = Field(
        default=None, description="Entity country iso code"
    )
    email: Optional[StrictStr] = Field(default=None, description="Entity email")
    certified_email: Optional[StrictStr] = Field(
        default=None, description="Entity certified email"
    )
    phone: Optional[StrictStr] = Field(default=None, description="Entity phone")
    fax: Optional[StrictStr] = Field(default=None, description="Entity fax")
    notes: Optional[StrictStr] = Field(default=None, description="Entity extra")
    default_payment_terms: Optional[StrictInt] = Field(
        default=None, description="[Only for client] Client default payment terms"
    )
    default_vat: Optional[VatType] = None
    default_payment_terms_type: Optional[PaymentTermsType] = PaymentTermsType.STANDARD
    default_payment_method: Optional[PaymentMethod] = None
    bank_name: Optional[StrictStr] = Field(
        default=None, description="[Only for client] Client bank name"
    )
    bank_iban: Optional[StrictStr] = Field(
        default=None, description="[Only for client] Client bank iban"
    )
    bank_swift_code: Optional[StrictStr] = Field(
        default=None, description="[Only for client] Client bank swift code"
    )
    shipping_address: Optional[StrictStr] = Field(
        default=None, description="[Only for client] Client Shipping address"
    )
    e_invoice: Optional[StrictBool] = Field(
        default=None, description="[Only for client] Use e-invoices."
    )
    ei_code: Optional[StrictStr] = Field(
        default=None, description="[Only for client] E-invoices code."
    )
    has_intent_declaration: Optional[StrictBool] = Field(
        default=None, description="[Only for client] Has intent declaration."
    )
    intent_declaration_protocol_number: Optional[StrictStr] = Field(
        default=None,
        description="[Only for client] Client intent declaration protocol number",
    )
    intent_declaration_protocol_date: Optional[date] = Field(
        default=None,
        description="[Only for client] Client intent declaration protocol date",
    )
    created_at: Optional[StrictStr] = Field(
        default=None, description="Entity creation date"
    )
    updated_at: Optional[StrictStr] = Field(
        default=None, description="Entity last update date"
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
        "default_payment_terms",
        "default_vat",
        "default_payment_terms_type",
        "default_payment_method",
        "bank_name",
        "bank_iban",
        "bank_swift_code",
        "shipping_address",
        "e_invoice",
        "ei_code",
        "has_intent_declaration",
        "intent_declaration_protocol_number",
        "intent_declaration_protocol_date",
        "created_at",
        "updated_at",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Entity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_vat
        if self.default_vat:
            _dict["default_vat"] = self.default_vat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_payment_method
        if self.default_payment_method:
            _dict["default_payment_method"] = self.default_payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Entity from a dict"""
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
                "default_payment_terms": obj.get("default_payment_terms"),
                "default_vat": (
                    VatType.from_dict(obj["default_vat"])
                    if obj.get("default_vat") is not None
                    else None
                ),
                "default_payment_terms_type": (
                    obj.get("default_payment_terms_type")
                    if obj.get("default_payment_terms_type") is not None
                    else PaymentTermsType.STANDARD
                ),
                "default_payment_method": (
                    PaymentMethod.from_dict(obj["default_payment_method"])
                    if obj.get("default_payment_method") is not None
                    else None
                ),
                "bank_name": obj.get("bank_name"),
                "bank_iban": obj.get("bank_iban"),
                "bank_swift_code": obj.get("bank_swift_code"),
                "shipping_address": obj.get("shipping_address"),
                "e_invoice": obj.get("e_invoice"),
                "ei_code": obj.get("ei_code"),
                "has_intent_declaration": obj.get("has_intent_declaration"),
                "intent_declaration_protocol_number": obj.get(
                    "intent_declaration_protocol_number"
                ),
                "intent_declaration_protocol_date": obj.get(
                    "intent_declaration_protocol_date"
                ),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
