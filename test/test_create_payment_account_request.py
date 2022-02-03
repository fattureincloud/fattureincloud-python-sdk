"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.8
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
globals()['PaymentAccount'] = PaymentAccount
from fattureincloud_python_sdk.model.create_payment_account_request import CreatePaymentAccountRequest


class TestCreatePaymentAccountRequest(unittest.TestCase):
    """CreatePaymentAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreatePaymentAccountRequest(self):
        """Test CreatePaymentAccountRequest"""
        model = CreatePaymentAccountRequest(
            data=PaymentAccount(
                id=1,
                name="Conto Banca Intesa",
                type=PaymentAccountType("standard"),
                iban="iban_example",
                sia="sia_example",
                cuc="cuc_example",
                virtual=True,
            )
        )
        expected_json = "{'data': {'cuc': 'cuc_example',          'iban': 'iban_example',          'id': 1,          'name': 'Conto Banca Intesa',          'sia': 'sia_example',          'type': 'standard',          'virtual': True}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
