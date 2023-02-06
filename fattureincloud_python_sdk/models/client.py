# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.25
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from fattureincloud_python_sdk.models.client_type import ClientType
from fattureincloud_python_sdk.models.payment_method import PaymentMethod
from fattureincloud_python_sdk.models.payment_terms_type import PaymentTermsType
from fattureincloud_python_sdk.models.vat_type import VatType


class Client(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Unique identifier")
    code: Optional[StrictStr] = Field(None, description="Client code.")
    name: Optional[StrictStr] = Field(None, description="Client name")
    type: Optional[ClientType] = None
    first_name: Optional[StrictStr] = Field(None, description="Client first name.")
    last_name: Optional[StrictStr] = Field(None, description="Client last name.")
    contact_person: Optional[StrictStr] = None
    vat_number: Optional[StrictStr] = Field(None, description="Client vat number")
    tax_code: Optional[StrictStr] = Field(None, description="Client tax code.")
    address_street: Optional[StrictStr] = Field(
        None, description="Client street address."
    )
    address_postal_code: Optional[StrictStr] = Field(
        None, description="Client postal code."
    )
    address_city: Optional[StrictStr] = Field(None, description="Client city.")
    address_province: Optional[StrictStr] = Field(None, description="Client province.")
    address_extra: Optional[StrictStr] = Field(
        None, description="Client address extra info."
    )
    country: Optional[StrictStr] = Field(None, description="Client country")
    email: Optional[StrictStr] = Field(None, description="Client email.")
    certified_email: Optional[StrictStr] = Field(
        None, description="Client certified email."
    )
    phone: Optional[StrictStr] = Field(None, description="Client phone.")
    fax: Optional[StrictStr] = Field(None, description="Client fax.")
    notes: Optional[StrictStr] = Field(None, description="Extra notes.")
    default_vat: Optional[VatType] = None
    default_payment_terms: Optional[StrictInt] = None
    default_payment_terms_type: Optional[PaymentTermsType] = None
    default_payment_method: Optional[PaymentMethod] = None
    bank_name: Optional[StrictStr] = Field(None, description="Client bank name.")
    bank_iban: Optional[StrictStr] = Field(None, description="Client iban.")
    bank_swift_code: Optional[StrictStr] = Field(
        None, description="Client bank swift code."
    )
    shipping_address: Optional[StrictStr] = Field(
        None, description="Client shipping address."
    )
    e_invoice: Optional[StrictBool] = Field(
        None, description="Use e-invoices for this entity"
    )
    ei_code: Optional[StrictStr] = Field(None, description="E-invoice code")
    discount_highlight: Optional[StrictBool] = Field(
        None, description="Discount Highlight."
    )
    default_discount: Optional[StrictFloat] = Field(
        None, description="Default discount."
    )
    has_intent_declaration: Optional[StrictBool] = Field(
        None, description="Has intent declaration."
    )
    intent_declaration_protocol_number: Optional[StrictStr] = Field(
        None, description="Intent declaration protocol number."
    )
    intent_declaration_protocol_date: Optional[date] = Field(
        None, description="Intent declaration protocol date."
    )
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties = [
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
        "email",
        "certified_email",
        "phone",
        "fax",
        "notes",
        "default_vat",
        "default_payment_terms",
        "default_payment_terms_type",
        "default_payment_method",
        "bank_name",
        "bank_iban",
        "bank_swift_code",
        "shipping_address",
        "e_invoice",
        "ei_code",
        "discount_highlight",
        "default_discount",
        "has_intent_declaration",
        "intent_declaration_protocol_number",
        "intent_declaration_protocol_date",
        "created_at",
        "updated_at",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Client:
        """Create an instance of Client from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default_vat
        if self.default_vat:
            _dict["default_vat"] = self.default_vat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_payment_method
        if self.default_payment_method:
            _dict["default_payment_method"] = self.default_payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Client:
        """Create an instance of Client from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Client.parse_obj(obj)

        _obj = Client.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "code": obj.get("code") if obj.get("code") is not None else None,
                "name": obj.get("name") if obj.get("name") is not None else None,
                "type": obj.get("type"),
                "first_name": obj.get("first_name")
                if obj.get("first_name") is not None
                else None,
                "last_name": obj.get("last_name")
                if obj.get("last_name") is not None
                else None,
                "contact_person": obj.get("contact_person")
                if obj.get("contact_person") is not None
                else None,
                "vat_number": obj.get("vat_number")
                if obj.get("vat_number") is not None
                else None,
                "tax_code": obj.get("tax_code")
                if obj.get("tax_code") is not None
                else None,
                "address_street": obj.get("address_street")
                if obj.get("address_street") is not None
                else None,
                "address_postal_code": obj.get("address_postal_code")
                if obj.get("address_postal_code") is not None
                else None,
                "address_city": obj.get("address_city")
                if obj.get("address_city") is not None
                else None,
                "address_province": obj.get("address_province")
                if obj.get("address_province") is not None
                else None,
                "address_extra": obj.get("address_extra")
                if obj.get("address_extra") is not None
                else None,
                "country": obj.get("country")
                if obj.get("country") is not None
                else None,
                "email": obj.get("email") if obj.get("email") is not None else None,
                "certified_email": obj.get("certified_email")
                if obj.get("certified_email") is not None
                else None,
                "phone": obj.get("phone") if obj.get("phone") is not None else None,
                "fax": obj.get("fax") if obj.get("fax") is not None else None,
                "notes": obj.get("notes") if obj.get("notes") is not None else None,
                "default_vat": VatType.from_dict(obj.get("default_vat"))
                if obj.get("default_vat") is not None
                else None,
                "default_payment_terms": obj.get("default_payment_terms")
                if obj.get("default_payment_terms") is not None
                else None,
                "default_payment_terms_type": obj.get("default_payment_terms_type"),
                "default_payment_method": PaymentMethod.from_dict(
                    obj.get("default_payment_method")
                )
                if obj.get("default_payment_method") is not None
                else None,
                "bank_name": obj.get("bank_name")
                if obj.get("bank_name") is not None
                else None,
                "bank_iban": obj.get("bank_iban")
                if obj.get("bank_iban") is not None
                else None,
                "bank_swift_code": obj.get("bank_swift_code")
                if obj.get("bank_swift_code") is not None
                else None,
                "shipping_address": obj.get("shipping_address")
                if obj.get("shipping_address") is not None
                else None,
                "e_invoice": obj.get("e_invoice")
                if obj.get("e_invoice") is not None
                else None,
                "ei_code": obj.get("ei_code")
                if obj.get("ei_code") is not None
                else None,
                "discount_highlight": obj.get("discount_highlight")
                if obj.get("discount_highlight") is not None
                else None,
                "default_discount": float(obj.get("default_discount"))
                if obj.get("default_discount") is not None
                else None,
                "has_intent_declaration": obj.get("has_intent_declaration")
                if obj.get("has_intent_declaration") is not None
                else None,
                "intent_declaration_protocol_number": obj.get(
                    "intent_declaration_protocol_number"
                )
                if obj.get("intent_declaration_protocol_number") is not None
                else None,
                "intent_declaration_protocol_date": obj.get(
                    "intent_declaration_protocol_date"
                )
                if obj.get("intent_declaration_protocol_date") is not None
                else None,
                "created_at": obj.get("created_at")
                if obj.get("created_at") is not None
                else None,
                "updated_at": obj.get("updated_at")
                if obj.get("updated_at") is not None
                else None,
            }
        )
        return _obj
