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
from pydantic import BaseModel, Field, StrictFloat


class MonthlyTotal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    net: Optional[StrictFloat] = Field(None, description="Monthly total net amount.")
    gross: Optional[StrictFloat] = Field(
        None, description="Monthly total gross amount."
    )
    count: Optional[StrictFloat] = Field(
        None, description="Monthly total receipt number."
    )
    __properties = ["net", "gross", "count"]

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
    def from_json(cls, json_str: str) -> MonthlyTotal:
        """Create an instance of MonthlyTotal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MonthlyTotal:
        """Create an instance of MonthlyTotal from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MonthlyTotal.parse_obj(obj)

        _obj = MonthlyTotal.parse_obj(
            {
                "net": float(obj.get("net")) if obj.get("net") is not None else None,
                "gross": float(obj.get("gross"))
                if obj.get("gross") is not None
                else None,
                "count": float(obj.get("count"))
                if obj.get("count") is not None
                else None,
            }
        )
        return _obj
