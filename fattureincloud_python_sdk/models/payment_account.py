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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType


class PaymentAccount(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Unique identifier")
    name: Optional[StrictStr] = Field(None, description="Payment account name.")
    type: Optional[PaymentAccountType] = None
    iban: Optional[StrictStr] = Field(None, description="Payment account iban.")
    sia: Optional[StrictStr] = Field(None, description="Payment account sia.")
    cuc: Optional[StrictStr] = Field(None, description="Payment account cuc.")
    virtual: Optional[StrictBool] = Field(
        None, description="Determine if the payment method is virtual."
    )
    __properties = ["id", "name", "type", "iban", "sia", "cuc", "virtual"]

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
    def from_json(cls, json_str: str) -> PaymentAccount:
        """Create an instance of PaymentAccount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentAccount:
        """Create an instance of PaymentAccount from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaymentAccount.parse_obj(obj)

        _obj = PaymentAccount.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "name": obj.get("name") if obj.get("name") is not None else None,
                "type": obj.get("type"),
                "iban": obj.get("iban") if obj.get("iban") is not None else None,
                "sia": obj.get("sia") if obj.get("sia") is not None else None,
                "cuc": obj.get("cuc") if obj.get("cuc") is not None else None,
                "virtual": obj.get("virtual")
                if obj.get("virtual") is not None
                else None,
            }
        )
        return _obj
