# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.29
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from fattureincloud_python_sdk.models.currency import Currency
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.received_document_info_default_values import (
    ReceivedDocumentInfoDefaultValues,
)
from fattureincloud_python_sdk.models.received_document_info_items_default_values import (
    ReceivedDocumentInfoItemsDefaultValues,
)
from fattureincloud_python_sdk.models.vat_type import VatType


class ReceivedDocumentInfo(BaseModel):
    """
    ReceivedDocumentInfo
    """

    default_values: Optional[ReceivedDocumentInfoDefaultValues] = None
    items_default_values: Optional[ReceivedDocumentInfoItemsDefaultValues] = None
    countries_list: Optional[conlist(StrictStr)] = Field(
        None, description="Countries list"
    )
    currencies_list: Optional[conlist(Currency)] = Field(
        None, description="Currencies list"
    )
    categories_list: Optional[conlist(StrictStr)] = Field(
        None, description="Categories list"
    )
    payment_accounts_list: Optional[conlist(PaymentAccount)] = Field(
        None, description="Payments accounts list"
    )
    vat_types_list: Optional[conlist(VatType)] = Field(
        None, description="Vat types list"
    )
    __properties = [
        "default_values",
        "items_default_values",
        "countries_list",
        "currencies_list",
        "categories_list",
        "payment_accounts_list",
        "vat_types_list",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ReceivedDocumentInfo:
        """Create an instance of ReceivedDocumentInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default_values
        if self.default_values:
            _dict["default_values"] = self.default_values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of items_default_values
        if self.items_default_values:
            _dict["items_default_values"] = self.items_default_values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in currencies_list (list)
        _items = []
        if self.currencies_list:
            for _item in self.currencies_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["currencies_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payment_accounts_list (list)
        _items = []
        if self.payment_accounts_list:
            for _item in self.payment_accounts_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["payment_accounts_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vat_types_list (list)
        _items = []
        if self.vat_types_list:
            for _item in self.vat_types_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["vat_types_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReceivedDocumentInfo:
        """Create an instance of ReceivedDocumentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReceivedDocumentInfo.parse_obj(obj)

        _obj = ReceivedDocumentInfo.parse_obj(
            {
                "default_values": ReceivedDocumentInfoDefaultValues.from_dict(
                    obj.get("default_values")
                )
                if obj.get("default_values") is not None
                else None,
                "items_default_values": ReceivedDocumentInfoItemsDefaultValues.from_dict(
                    obj.get("items_default_values")
                )
                if obj.get("items_default_values") is not None
                else None,
                "countries_list": obj.get("countries_list"),
                "currencies_list": [
                    Currency.from_dict(_item) for _item in obj.get("currencies_list")
                ]
                if obj.get("currencies_list") is not None
                else None,
                "categories_list": obj.get("categories_list"),
                "payment_accounts_list": [
                    PaymentAccount.from_dict(_item)
                    for _item in obj.get("payment_accounts_list")
                ]
                if obj.get("payment_accounts_list") is not None
                else None,
                "vat_types_list": [
                    VatType.from_dict(_item) for _item in obj.get("vat_types_list")
                ]
                if obj.get("vat_types_list") is not None
                else None,
            }
        )
        return _obj
