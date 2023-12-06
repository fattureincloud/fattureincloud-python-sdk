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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from fattureincloud_python_sdk.models.vat_type import VatType

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Product(BaseModel):
    """
    Product
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Product id")
    name: Optional[StrictStr] = Field(default=None, description="Product name")
    code: Optional[StrictStr] = Field(default=None, description="Product code")
    net_price: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Product net price"
    )
    gross_price: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Product gross price"
    )
    use_gross_price: Optional[StrictBool] = Field(
        default=None, description="Product uses gross prices"
    )
    default_vat: Optional[VatType] = None
    net_cost: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Product net cost"
    )
    measure: Optional[StrictStr] = Field(default=None, description="Product measure")
    description: Optional[StrictStr] = Field(
        default=None, description="Product description"
    )
    category: Optional[StrictStr] = Field(default=None, description="Product category")
    notes: Optional[StrictStr] = Field(default=None, description="Product extra notes")
    in_stock: Optional[StrictBool] = Field(
        default=None, description="Product has stock"
    )
    stock_initial: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Product initial stock"
    )
    stock_current: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="[Read Only] Product current stock"
    )
    average_cost: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Product average cost"
    )
    average_price: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Product average price"
    )
    created_at: Optional[StrictStr] = Field(
        default=None, description="Product creation date"
    )
    updated_at: Optional[StrictStr] = Field(
        default=None, description="Product last update date"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "code",
        "net_price",
        "gross_price",
        "use_gross_price",
        "default_vat",
        "net_cost",
        "measure",
        "description",
        "category",
        "notes",
        "in_stock",
        "stock_initial",
        "stock_current",
        "average_cost",
        "average_price",
        "created_at",
        "updated_at",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Product from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "stock_current",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of default_vat
        if self.default_vat:
            _dict["default_vat"] = self.default_vat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "code": obj.get("code"),
                "net_price": obj.get("net_price"),
                "gross_price": obj.get("gross_price"),
                "use_gross_price": obj.get("use_gross_price"),
                "default_vat": VatType.from_dict(obj.get("default_vat"))
                if obj.get("default_vat") is not None
                else None,
                "net_cost": obj.get("net_cost"),
                "measure": obj.get("measure"),
                "description": obj.get("description"),
                "category": obj.get("category"),
                "notes": obj.get("notes"),
                "in_stock": obj.get("in_stock"),
                "stock_initial": obj.get("stock_initial"),
                "stock_current": obj.get("stock_current"),
                "average_cost": obj.get("average_cost"),
                "average_price": obj.get("average_price"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
