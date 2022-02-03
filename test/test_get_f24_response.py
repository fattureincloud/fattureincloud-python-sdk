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
import dateutil
import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.f24 import F24
from fattureincloud_python_sdk.model.f24_status import F24Status
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
globals()['F24'] = F24
from fattureincloud_python_sdk.model.get_f24_response import GetF24Response


class TestGetF24Response(unittest.TestCase):
    """GetF24Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetF24Response(self):
        """Test GetF24Response"""
        model = GetF24Response(
            data=F24(
                id=1,
                due_date=dateutil.parser.parse('2022.01.01').date(),
                status=F24Status("paid"),
                payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True
                ),
                amount=300.0,
                attachment_token="attachment_token_example",
                description="description_example"
            )
        )
        expected_json = "{'data': {'amount': 300.0,          'attachment_token': 'attachment_token_example',          'description': 'description_example',          'due_date': datetime.date(2022, 1, 1),          'id': 1,          'payment_account': {'cuc': 'cuc_example',                              'iban': 'iban_example',                              'id': 1,                              'name': 'Conto Banca Intesa',                              'sia': 'sia_example',                              'type': 'standard',                              'virtual': True},          'status': 'paid'}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
