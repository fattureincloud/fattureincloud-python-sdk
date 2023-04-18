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
from fattureincloud_python_sdk.models.issued_document import IssuedDocument
from fattureincloud_python_sdk.models.issued_document_options import (
    IssuedDocumentOptions,
)


class JoinIssuedDocumentsResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    data: Optional[IssuedDocument] = None
    options: Optional[IssuedDocumentOptions] = None
    __properties = ["data", "options"]

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
    def from_json(cls, json_str: str) -> JoinIssuedDocumentsResponse:
        """Create an instance of JoinIssuedDocumentsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict["data"] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JoinIssuedDocumentsResponse:
        """Create an instance of JoinIssuedDocumentsResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return JoinIssuedDocumentsResponse.parse_obj(obj)

        _obj = JoinIssuedDocumentsResponse.parse_obj(
            {
                "data": IssuedDocument.from_dict(obj.get("data"))
                if obj.get("data") is not None
                else None,
                "options": IssuedDocumentOptions.from_dict(obj.get("options"))
                if obj.get("options") is not None
                else None,
            }
        )
        return _obj
