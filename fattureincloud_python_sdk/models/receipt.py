# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.receipt_items_list_item import (
    ReceiptItemsListItem,
)
from fattureincloud_python_sdk.models.receipt_type import ReceiptType


class Receipt(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Receipt unique identifier.")
    var_date: Optional[date] = Field(None, alias="date", description="Receipt date.")
    number: Optional[StrictFloat] = Field(None, description="Receipt number.")
    numeration: Optional[StrictStr] = Field(
        None, description="If it's null or empty string use the default numeration."
    )
    amount_net: Optional[StrictFloat] = Field(None, description="Total net amount.")
    amount_vat: Optional[StrictFloat] = Field(None, description="Total vat amount.")
    amount_gross: Optional[StrictFloat] = Field(None, description="Total gross amount.")
    use_gross_prices: Optional[StrictBool] = None
    type: Optional[ReceiptType] = None
    description: Optional[StrictStr] = Field(None, description="Receipt description.")
    rc_center: Optional[StrictStr] = Field(None, description="Revenue center.")
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    payment_account: Optional[PaymentAccount] = None
    items_list: Optional[List[ReceiptItemsListItem]] = None
    __properties = [
        "id",
        "date",
        "number",
        "numeration",
        "amount_net",
        "amount_vat",
        "amount_gross",
        "use_gross_prices",
        "type",
        "description",
        "rc_center",
        "created_at",
        "updated_at",
        "payment_account",
        "items_list",
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
    def from_json(cls, json_str: str) -> Receipt:
        """Create an instance of Receipt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_account
        if self.payment_account:
            _dict["payment_account"] = self.payment_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items_list (list)
        _items = []
        if self.items_list:
            for _item in self.items_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Receipt:
        """Create an instance of Receipt from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Receipt.parse_obj(obj)

        _obj = Receipt.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "var_date": obj.get("date") if obj.get("date") is not None else None,
                "number": float(obj.get("number"))
                if obj.get("number") is not None
                else None,
                "numeration": obj.get("numeration")
                if obj.get("numeration") is not None
                else None,
                "amount_net": float(obj.get("amount_net"))
                if obj.get("amount_net") is not None
                else None,
                "amount_vat": float(obj.get("amount_vat"))
                if obj.get("amount_vat") is not None
                else None,
                "amount_gross": float(obj.get("amount_gross"))
                if obj.get("amount_gross") is not None
                else None,
                "use_gross_prices": obj.get("use_gross_prices")
                if obj.get("use_gross_prices") is not None
                else None,
                "type": obj.get("type"),
                "description": obj.get("description")
                if obj.get("description") is not None
                else None,
                "rc_center": obj.get("rc_center")
                if obj.get("rc_center") is not None
                else None,
                "created_at": obj.get("created_at")
                if obj.get("created_at") is not None
                else None,
                "updated_at": obj.get("updated_at")
                if obj.get("updated_at") is not None
                else None,
                "payment_account": PaymentAccount.from_dict(obj.get("payment_account"))
                if obj.get("payment_account") is not None
                else None,
                "items_list": [
                    ReceiptItemsListItem.from_dict(_item)
                    for _item in obj.get("items_list")
                ]
                if obj.get("items_list") is not None
                else None,
            }
        )
        return _obj
