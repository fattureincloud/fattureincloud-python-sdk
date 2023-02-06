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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr


class VatType(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Unique identifier")
    value: Optional[StrictFloat] = Field(
        None, description="[Read Only] Percentual value."
    )
    description: Optional[StrictStr] = Field(None, description="Short description.")
    notes: Optional[StrictStr] = Field(
        None, description="Long description and notes shown in documents."
    )
    e_invoice: Optional[StrictBool] = Field(None, description="Usable for e-invoices.")
    ei_type: Optional[StrictStr] = Field(None, description="E-invoice type (natura).")
    ei_description: Optional[StrictStr] = Field(
        None, description="E-invoice description."
    )
    editable: Optional[StrictBool] = Field(
        None, description="[Read Only] Determine if this vat type is editable."
    )
    is_disabled: Optional[StrictBool] = Field(
        None, description="Determine if the vat type is disabled."
    )
    __properties = [
        "id",
        "value",
        "description",
        "notes",
        "e_invoice",
        "ei_type",
        "ei_description",
        "editable",
        "is_disabled",
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
    def from_json(cls, json_str: str) -> VatType:
        """Create an instance of VatType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(
            by_alias=True,
            exclude={
                "editable",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VatType:
        """Create an instance of VatType from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return VatType.parse_obj(obj)

        _obj = VatType.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "value": float(obj.get("value"))
                if obj.get("value") is not None
                else None,
                "description": obj.get("description")
                if obj.get("description") is not None
                else None,
                "notes": obj.get("notes") if obj.get("notes") is not None else None,
                "e_invoice": obj.get("e_invoice")
                if obj.get("e_invoice") is not None
                else None,
                "ei_type": obj.get("ei_type")
                if obj.get("ei_type") is not None
                else None,
                "ei_description": obj.get("ei_description")
                if obj.get("ei_description") is not None
                else None,
                "editable": obj.get("editable")
                if obj.get("editable") is not None
                else None,
                "is_disabled": obj.get("is_disabled")
                if obj.get("is_disabled") is not None
                else None,
            }
        )
        return _obj
