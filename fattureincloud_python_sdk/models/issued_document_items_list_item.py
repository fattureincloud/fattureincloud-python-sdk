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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from fattureincloud_python_sdk.models.vat_type import VatType


class IssuedDocumentItemsListItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictInt] = Field(None, description="Unique identifier.")
    product_id: Optional[StrictInt] = Field(
        None, description="Unique identifier of the product."
    )
    code: Optional[StrictStr] = Field(None, description="Product code.")
    name: Optional[StrictStr] = Field(None, description="Product name.")
    category: Optional[StrictStr] = Field(None, description="Product category")
    description: Optional[StrictStr] = Field(None, description="Product description.")
    qty: Optional[StrictFloat] = Field(None, description="Items quantity,")
    measure: Optional[StrictStr] = Field(None, description="Item measure.")
    net_price: Optional[StrictFloat] = Field(None, description="Net price.")
    gross_price: Optional[StrictFloat] = Field(None, description="Gross price.")
    vat: Optional[VatType] = None
    not_taxable: Optional[StrictBool] = None
    apply_withholding_taxes: Optional[StrictBool] = Field(
        None, description="Apply withholding taxes, rivalsa and cassa."
    )
    discount: Optional[StrictFloat] = Field(
        None, description="Discount percentual value."
    )
    discount_highlight: Optional[StrictBool] = None
    in_dn: Optional[StrictBool] = None
    stock: Optional[StrictBool] = None
    ei_raw: Optional[Dict[str, Any]] = Field(
        None, description="Advanced raw attributes for e-invoices."
    )
    __properties = [
        "id",
        "product_id",
        "code",
        "name",
        "category",
        "description",
        "qty",
        "measure",
        "net_price",
        "gross_price",
        "vat",
        "not_taxable",
        "apply_withholding_taxes",
        "discount",
        "discount_highlight",
        "in_dn",
        "stock",
        "ei_raw",
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
    def from_json(cls, json_str: str) -> IssuedDocumentItemsListItem:
        """Create an instance of IssuedDocumentItemsListItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of vat
        if self.vat:
            _dict["vat"] = self.vat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssuedDocumentItemsListItem:
        """Create an instance of IssuedDocumentItemsListItem from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IssuedDocumentItemsListItem.parse_obj(obj)

        _obj = IssuedDocumentItemsListItem.parse_obj(
            {
                "id": obj.get("id") if obj.get("id") is not None else None,
                "product_id": obj.get("product_id")
                if obj.get("product_id") is not None
                else None,
                "code": obj.get("code") if obj.get("code") is not None else None,
                "name": obj.get("name") if obj.get("name") is not None else None,
                "category": obj.get("category")
                if obj.get("category") is not None
                else None,
                "description": obj.get("description")
                if obj.get("description") is not None
                else None,
                "qty": float(obj.get("qty")) if obj.get("qty") is not None else None,
                "measure": obj.get("measure")
                if obj.get("measure") is not None
                else None,
                "net_price": float(obj.get("net_price"))
                if obj.get("net_price") is not None
                else None,
                "gross_price": float(obj.get("gross_price"))
                if obj.get("gross_price") is not None
                else None,
                "vat": VatType.from_dict(obj.get("vat"))
                if obj.get("vat") is not None
                else None,
                "not_taxable": obj.get("not_taxable")
                if obj.get("not_taxable") is not None
                else None,
                "apply_withholding_taxes": obj.get("apply_withholding_taxes")
                if obj.get("apply_withholding_taxes") is not None
                else None,
                "discount": float(obj.get("discount"))
                if obj.get("discount") is not None
                else None,
                "discount_highlight": obj.get("discount_highlight")
                if obj.get("discount_highlight") is not None
                else None,
                "in_dn": obj.get("in_dn") if obj.get("in_dn") is not None else None,
                "stock": obj.get("stock") if obj.get("stock") is not None else None,
                "ei_raw": obj.get("ei_raw") if obj.get("ei_raw") is not None else None,
            }
        )
        return _obj
