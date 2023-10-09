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


from typing import Optional
from pydantic import BaseModel
from fattureincloud_python_sdk.models.list_f24_response_aggregated_data import (
    ListF24ResponseAggregatedData,
)


class ListF24ResponseAggregation(BaseModel):
    """
    ListF24ResponseAggregation
    """

    aggregated_data: Optional[ListF24ResponseAggregatedData] = None
    __properties = ["aggregated_data"]

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
    def from_json(cls, json_str: str) -> ListF24ResponseAggregation:
        """Create an instance of ListF24ResponseAggregation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of aggregated_data
        if self.aggregated_data:
            _dict["aggregated_data"] = self.aggregated_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListF24ResponseAggregation:
        """Create an instance of ListF24ResponseAggregation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListF24ResponseAggregation.parse_obj(obj)

        _obj = ListF24ResponseAggregation.parse_obj(
            {
                "aggregated_data": ListF24ResponseAggregatedData.from_dict(
                    obj.get("aggregated_data")
                )
                if obj.get("aggregated_data") is not None
                else None
            }
        )
        return _obj
