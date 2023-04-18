# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_error import (
    VerifyEInvoiceXmlErrorResponseError,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_extra import (
    VerifyEInvoiceXmlErrorResponseExtra,
)


class VerifyEInvoiceXmlErrorResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    error: Optional[VerifyEInvoiceXmlErrorResponseError] = None
    extra: Optional[VerifyEInvoiceXmlErrorResponseExtra] = None
    __properties = ["error", "extra"]

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
    def from_json(cls, json_str: str) -> VerifyEInvoiceXmlErrorResponse:
        """Create an instance of VerifyEInvoiceXmlErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extra
        if self.extra:
            _dict["extra"] = self.extra.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyEInvoiceXmlErrorResponse:
        """Create an instance of VerifyEInvoiceXmlErrorResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return VerifyEInvoiceXmlErrorResponse.parse_obj(obj)

        _obj = VerifyEInvoiceXmlErrorResponse.parse_obj(
            {
                "error": VerifyEInvoiceXmlErrorResponseError.from_dict(obj.get("error"))
                if obj.get("error") is not None
                else None,
                "extra": VerifyEInvoiceXmlErrorResponseExtra.from_dict(obj.get("extra"))
                if obj.get("extra") is not None
                else None,
            }
        )
        return _obj
