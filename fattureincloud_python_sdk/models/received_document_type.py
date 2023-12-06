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
import json
import pprint
import re  # noqa: F401
from enum import Enum


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ReceivedDocumentType(str, Enum):
    """
    Received document type
    """

    """
    allowed enum values
    """
    EXPENSE = "expense"
    PASSIVE_CREDIT_NOTE = "passive_credit_note"
    PASSIVE_DELIVERY_NOTE = "passive_delivery_note"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReceivedDocumentType from a JSON string"""
        return cls(json.loads(json_str))
