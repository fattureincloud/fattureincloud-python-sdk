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


from typing import Optional
from pydantic import BaseModel, Field, StrictFloat


class ReceivedDocumentTotals(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    amount_net: Optional[StrictFloat] = Field(None, description="Total net amount.")
    amount_vat: Optional[StrictFloat] = Field(None, description="Total vat amount.")
    amount_gross: Optional[StrictFloat] = Field(None, description="Total gross amount.")
    amount_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Total withholding tax amount."
    )
    amount_other_withholding_tax: Optional[StrictFloat] = Field(
        None, description="Total other withholding tax amount."
    )
    amount_due: Optional[StrictFloat] = Field(None, description="Total amount due.")
    payments_sum: Optional[StrictFloat] = Field(None, description="Payments sum.")
    __properties = [
        "amount_net",
        "amount_vat",
        "amount_gross",
        "amount_withholding_tax",
        "amount_other_withholding_tax",
        "amount_due",
        "payments_sum",
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
    def from_json(cls, json_str: str) -> ReceivedDocumentTotals:
        """Create an instance of ReceivedDocumentTotals from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReceivedDocumentTotals:
        """Create an instance of ReceivedDocumentTotals from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReceivedDocumentTotals.parse_obj(obj)

        _obj = ReceivedDocumentTotals.parse_obj(
            {
                "amount_net": float(obj.get("amount_net"))
                if obj.get("amount_net") is not None
                else None,
                "amount_vat": float(obj.get("amount_vat"))
                if obj.get("amount_vat") is not None
                else None,
                "amount_gross": float(obj.get("amount_gross"))
                if obj.get("amount_gross") is not None
                else None,
                "amount_withholding_tax": float(obj.get("amount_withholding_tax"))
                if obj.get("amount_withholding_tax") is not None
                else None,
                "amount_other_withholding_tax": float(
                    obj.get("amount_other_withholding_tax")
                )
                if obj.get("amount_other_withholding_tax") is not None
                else None,
                "amount_due": float(obj.get("amount_due"))
                if obj.get("amount_due") is not None
                else None,
                "payments_sum": float(obj.get("payments_sum"))
                if obj.get("payments_sum") is not None
                else None,
            }
        )
        return _obj
