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
from pydantic import BaseModel
from fattureincloud_python_sdk.models.permission_level import PermissionLevel


class PermissionsFicIssuedDocumentsDetailed(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    quotes: Optional[PermissionLevel] = None
    proformas: Optional[PermissionLevel] = None
    invoices: Optional[PermissionLevel] = None
    receipts: Optional[PermissionLevel] = None
    delivery_notes: Optional[PermissionLevel] = None
    credit_notes: Optional[PermissionLevel] = None
    orders: Optional[PermissionLevel] = None
    work_reports: Optional[PermissionLevel] = None
    supplier_orders: Optional[PermissionLevel] = None
    self_invoices: Optional[PermissionLevel] = None
    __properties = [
        "quotes",
        "proformas",
        "invoices",
        "receipts",
        "delivery_notes",
        "credit_notes",
        "orders",
        "work_reports",
        "supplier_orders",
        "self_invoices",
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
    def from_json(cls, json_str: str) -> PermissionsFicIssuedDocumentsDetailed:
        """Create an instance of PermissionsFicIssuedDocumentsDetailed from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermissionsFicIssuedDocumentsDetailed:
        """Create an instance of PermissionsFicIssuedDocumentsDetailed from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PermissionsFicIssuedDocumentsDetailed.parse_obj(obj)

        _obj = PermissionsFicIssuedDocumentsDetailed.parse_obj(
            {
                "quotes": obj.get("quotes"),
                "proformas": obj.get("proformas"),
                "invoices": obj.get("invoices"),
                "receipts": obj.get("receipts"),
                "delivery_notes": obj.get("delivery_notes"),
                "credit_notes": obj.get("credit_notes"),
                "orders": obj.get("orders"),
                "work_reports": obj.get("work_reports"),
                "supplier_orders": obj.get("supplier_orders"),
                "self_invoices": obj.get("self_invoices"),
            }
        )
        return _obj
