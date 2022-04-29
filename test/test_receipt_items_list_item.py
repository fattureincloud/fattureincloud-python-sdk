"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.vat_type import VatType

globals()["VatType"] = VatType
from fattureincloud_python_sdk.model.receipt_items_list_item import ReceiptItemsListItem


class TestReceiptItemsListItem(unittest.TestCase):
    """ReceiptItemsListItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReceiptItemsListItem(self):
        """Test ReceiptItemsListItem"""
        model = ReceiptItemsListItem(
            id=3,
            amount_net=3.14,
            amount_gross=3.14,
            category="category_example",
            vat=VatType(
                id=1,
                value=22.0,
                description="Non imponibile art. 123",
                notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                e_invoice=True,
                ei_type="2",
                ei_description="ei_description_example",
                is_disabled=True,
            ),
        )
        expected_json = '{"id": 3, "amount_net": 3.14, "amount_gross": 3.14, "category": "category_example", "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
