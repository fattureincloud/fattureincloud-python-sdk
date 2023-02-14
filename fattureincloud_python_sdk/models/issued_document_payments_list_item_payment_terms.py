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
from pydantic import BaseModel, Field, StrictInt
from fattureincloud_python_sdk.models.payment_terms_type import PaymentTermsType


class IssuedDocumentPaymentsListItemPaymentTerms(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    days: Optional[StrictInt] = Field(
        None, description="The number of days by which the payment must be made."
    )
    type: Optional[PaymentTermsType] = None
    __properties = ["days", "type"]

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
    def from_json(cls, json_str: str) -> IssuedDocumentPaymentsListItemPaymentTerms:
        """Create an instance of IssuedDocumentPaymentsListItemPaymentTerms from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssuedDocumentPaymentsListItemPaymentTerms:
        """Create an instance of IssuedDocumentPaymentsListItemPaymentTerms from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IssuedDocumentPaymentsListItemPaymentTerms.parse_obj(obj)

        _obj = IssuedDocumentPaymentsListItemPaymentTerms.parse_obj(
            {
                "days": obj.get("days") if obj.get("days") is not None else None,
                "type": obj.get("type"),
            }
        )
        return _obj
