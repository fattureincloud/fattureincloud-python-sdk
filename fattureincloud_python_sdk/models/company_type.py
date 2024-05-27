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
import json
from enum import Enum
from typing_extensions import Self


class CompanyType(str, Enum):
    """
    Company type
    """

    """
    allowed enum values
    """
    COMPANY = "company"
    ACCOUNTANT = "accountant"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CompanyType from a JSON string"""
        return cls(json.loads(json_str))
