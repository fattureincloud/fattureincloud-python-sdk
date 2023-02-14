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
from fattureincloud_python_sdk.models.f24 import F24
from fattureincloud_python_sdk.models.f24_status import F24Status
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType

globals()["F24"] = F24
from fattureincloud_python_sdk.models.create_f24_request import CreateF24Request


class TestCreateF24Request(unittest.TestCase):
    """CreateF24Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateF24Request(self):
        """Test CreateF24Request"""
        model = CreateF24Request(
            data=F24(
                id=1,
                due_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                status=F24Status("paid"),
                payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                amount=300.0,
                attachment_token="attachment_token_example",
                description="description_example",
            )
        )
        expected_json = '{"data": {"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
