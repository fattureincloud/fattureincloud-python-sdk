# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.1.0
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fattureincloud_python_sdk.models.vat_type import VatType
from typing import Optional, Set
from typing_extensions import Self


class ReceivedDocumentItemsListItem(BaseModel):
    """
    ReceivedDocumentItemsListItem
    """  # noqa: E501

    id: Optional[StrictInt] = Field(
        default=None, description="Received document item id"
    )
    product_id: Optional[StrictInt] = Field(
        default=None, description="Received document product id"
    )
    code: Optional[StrictStr] = Field(
        default=None, description="Received document item product code"
    )
    name: Optional[StrictStr] = Field(
        default=None, description="Received document item product name"
    )
    measure: Optional[StrictStr] = Field(
        default=None, description="Received document item measure"
    )
    net_price: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Received document item product net price"
    )
    category: Optional[StrictStr] = Field(
        default=None, description="Received document item product category"
    )
    qty: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Received document item quantity"
    )
    vat: Optional[VatType] = None
    stock: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Received document item product number of items in stock",
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "product_id",
        "code",
        "name",
        "measure",
        "net_price",
        "category",
        "qty",
        "vat",
        "stock",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReceivedDocumentItemsListItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of vat
        if self.vat:
            _dict["vat"] = self.vat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReceivedDocumentItemsListItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "product_id": obj.get("product_id"),
                "code": obj.get("code"),
                "name": obj.get("name"),
                "measure": obj.get("measure"),
                "net_price": obj.get("net_price"),
                "category": obj.get("category"),
                "qty": obj.get("qty"),
                "vat": (
                    VatType.from_dict(obj["vat"])
                    if obj.get("vat") is not None
                    else None
                ),
                "stock": obj.get("stock"),
            }
        )
        return _obj
