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
import datetime
import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.receipt_items_list_item import ReceiptItemsListItem
from fattureincloud_python_sdk.model.receipt_type import ReceiptType
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.vat_type import VatType

globals()["PaymentAccount"] = PaymentAccount
globals()["ReceiptItemsListItem"] = ReceiptItemsListItem
globals()["ReceiptType"] = ReceiptType
from fattureincloud_python_sdk.model.receipt import Receipt


class TestReceipt(unittest.TestCase):
    """Receipt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReceipt(self):
        """Test Receipt"""
        model = Receipt(
            id=1,
            date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
            number=3.14,
            numeration="numeration_example",
            amount_net=3.14,
            amount_vat=3.14,
            amount_gross=3.14,
            use_gross_prices=False,
            type=ReceiptType("till_receipt"),
            description="description_example",
            rc_center="rc_center_example",
            created_at="created_at_example",
            updated_at="updated_at_example",
            payment_account=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            ),
            items_list=[
                ReceiptItemsListItem(
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
                ),
            ],
        )
        expected_json = '{"id": 1, "date": "2022-01-01", "number": 3.14, "numeration": "numeration_example", "amount_net": 3.14, "amount_vat": 3.14, "amount_gross": 3.14, "use_gross_prices": false, "type": "till_receipt", "description": "description_example", "rc_center": "rc_center_example", "created_at": "created_at_example", "updated_at": "updated_at_example", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "items_list": [{"id": 3, "amount_net": 3.14, "amount_gross": 3.14, "category": "category_example", "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}]}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
