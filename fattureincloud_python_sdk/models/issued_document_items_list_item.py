# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.33
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from fattureincloud_python_sdk.models.vat_type import VatType
from typing import Optional, Set
from typing_extensions import Self


class IssuedDocumentItemsListItem(BaseModel):
    """
    IssuedDocumentItemsListItem
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Issued document item id")
    product_id: Optional[StrictInt] = Field(
        default=None, description="Issued document item product id"
    )
    code: Optional[StrictStr] = Field(
        default=None, description="Issued document item product code"
    )
    name: Optional[StrictStr] = Field(
        default=None, description="Issued document item product name"
    )
    category: Optional[StrictStr] = Field(
        default=None, description="Issued document item product category"
    )
    description: Optional[StrictStr] = Field(
        default=None, description="Issued document product description"
    )
    qty: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document item quantity"
    )
    measure: Optional[StrictStr] = Field(
        default=None, description="Issued document item measure"
    )
    net_price: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document item net price"
    )
    gross_price: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document item gross price"
    )
    vat: Optional[VatType] = None
    not_taxable: Optional[StrictBool] = Field(
        default=None, description="Issued document item is not taxable"
    )
    apply_withholding_taxes: Optional[StrictBool] = Field(
        default=None,
        description="Issued document item apply withholding taxes, rivalsa and cassa",
    )
    discount: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, description="Issued document item discount percentual value"
    )
    discount_highlight: Optional[StrictBool] = Field(
        default=None, description="Issued document item highlight discount"
    )
    in_dn: Optional[StrictBool] = Field(
        default=None, description="Issued document item add in delivery note"
    )
    stock: Optional[StrictBool] = Field(
        default=None, description="Issued document item move stock"
    )
    ei_raw: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Issued document advanced raw attributes for e-invoices",
    )
    __properties: ClassVar[List[str]] = [
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
        """Create an instance of IssuedDocumentItemsListItem from a JSON string"""
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
        """Create an instance of IssuedDocumentItemsListItem from a dict"""
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
                "category": obj.get("category"),
                "description": obj.get("description"),
                "qty": obj.get("qty"),
                "measure": obj.get("measure"),
                "net_price": obj.get("net_price"),
                "gross_price": obj.get("gross_price"),
                "vat": (
                    VatType.from_dict(obj["vat"])
                    if obj.get("vat") is not None
                    else None
                ),
                "not_taxable": obj.get("not_taxable"),
                "apply_withholding_taxes": obj.get("apply_withholding_taxes"),
                "discount": obj.get("discount"),
                "discount_highlight": obj.get("discount_highlight"),
                "in_dn": obj.get("in_dn"),
                "stock": obj.get("stock"),
                "ei_raw": obj.get("ei_raw"),
            }
        )
        return _obj
