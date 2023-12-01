# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.30
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from fattureincloud_python_sdk.models.function_status import FunctionStatus


class CompanyInfoPlanInfoFunctionsStatus(BaseModel):
    """
    CompanyInfoPlanInfoFunctionsStatus
    """

    ts_digital: Optional[FunctionStatus] = None
    ts_pay: Optional[FunctionStatus] = None
    __properties = ["ts_digital", "ts_pay"]

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
    def from_json(cls, json_str: str) -> CompanyInfoPlanInfoFunctionsStatus:
        """Create an instance of CompanyInfoPlanInfoFunctionsStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ts_digital
        if self.ts_digital:
            _dict["ts_digital"] = self.ts_digital.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ts_pay
        if self.ts_pay:
            _dict["ts_pay"] = self.ts_pay.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompanyInfoPlanInfoFunctionsStatus:
        """Create an instance of CompanyInfoPlanInfoFunctionsStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompanyInfoPlanInfoFunctionsStatus.parse_obj(obj)

        _obj = CompanyInfoPlanInfoFunctionsStatus.parse_obj(
            {
                "ts_digital": FunctionStatus.from_dict(obj.get("ts_digital"))
                if obj.get("ts_digital") is not None
                else None,
                "ts_pay": FunctionStatus.from_dict(obj.get("ts_pay"))
                if obj.get("ts_pay") is not None
                else None,
            }
        )
        return _obj
