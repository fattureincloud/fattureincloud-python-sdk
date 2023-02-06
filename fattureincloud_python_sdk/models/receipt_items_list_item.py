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


from typing import Optional
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from fattureincloud_python_sdk.models.vat_type import VatType


class ReceiptItemsListItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Item unique identifier.")
    amount_net: Optional[StrictFloat] = Field(
        None, description="Item total net amount."
    )
    amount_gross: Optional[StrictFloat] = Field(
        None, description="Item total gross amount."
    )
    category: Optional[StrictStr] = Field(None, description="Item category.")
    vat: Optional[VatType] = None
    __properties = ["id", "amount_net", "amount_gross", "category", "vat"]

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
    def from_json(cls, json_str: str) -> ReceiptItemsListItem:
        """Create an instance of ReceiptItemsListItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of vat
        if self.vat:
            _dict["vat"] = self.vat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReceiptItemsListItem:
        """Create an instance of ReceiptItemsListItem from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReceiptItemsListItem.parse_obj(obj)

        _obj = ReceiptItemsListItem.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "amount_net": float(obj.get("amount_net"))
                if obj.get("amount_net") is not None
                else None,
                "amount_gross": float(obj.get("amount_gross"))
                if obj.get("amount_gross") is not None
                else None,
                "category": obj.get("category")
                if obj.get("category") is not None
                else None,
                "vat": VatType.from_dict(obj.get("vat"))
                if obj.get("vat") is not None
                else None,
            }
        )
        return _obj
