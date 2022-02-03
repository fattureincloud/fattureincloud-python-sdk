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
import dateutil
import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.receipt import Receipt
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.receipt_items_list_item import ReceiptItemsListItem
from fattureincloud_python_sdk.model.receipt_type import ReceiptType
from fattureincloud_python_sdk.model.vat_type import VatType
globals()['Receipt'] = Receipt
from fattureincloud_python_sdk.model.get_receipt_response import GetReceiptResponse


class TestGetReceiptResponse(unittest.TestCase):
    """GetReceiptResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetReceiptResponse(self):
        """Test GetReceiptResponse"""
        model = GetReceiptResponse(
            data=Receipt(
                id=1,
                date=dateutil.parser.parse('2022-01-01').date(),
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
        )
        expected_json = "{'data': {'amount_gross': 3.14,          'amount_net': 3.14,          'amount_vat': 3.14,          'created_at': 'created_at_example',          'date': datetime.date(2022, 1, 1),          'description': 'description_example',          'id': 1,          'items_list': [{'amount_gross': 3.14,                          'amount_net': 3.14,                          'category': 'category_example',                          'id': 3,                          'vat': {'description': 'Non imponibile art. 123',                                  'e_invoice': True,                                  'ei_description': 'ei_description_example',                                  'ei_type': '2',                                  'id': 1,                                  'is_disabled': True,                                  'notes': 'IVA non imponibile ai sensi dell '                                           'articolo 123, comma 2',                                  'value': 22.0}}],          'number': 3.14,          'numeration': 'numeration_example',          'payment_account': {'cuc': 'cuc_example',                              'iban': 'iban_example',                              'id': 1,                              'name': 'Conto Banca Intesa',                              'sia': 'sia_example',                              'type': 'standard',                              'virtual': True},          'rc_center': 'rc_center_example',          'type': 'till_receipt',          'updated_at': 'updated_at_example',          'use_gross_prices': False}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
