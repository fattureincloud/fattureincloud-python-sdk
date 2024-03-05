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
from fattureincloud_python_sdk.models.payment_method import PaymentMethod
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.models.payment_method_details import PaymentMethodDetails
from fattureincloud_python_sdk.models.payment_method_type import PaymentMethodType

globals()["PaymentMethod"] = PaymentMethod
from fattureincloud_python_sdk.models.create_payment_method_request import (
    CreatePaymentMethodRequest,
)


class TestCreatePaymentMethodRequest(unittest.TestCase):
    """CreatePaymentMethodRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreatePaymentMethodRequest(self):
        """Test CreatePaymentMethodRequest"""
        model = CreatePaymentMethodRequest(
            data=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            )
        )
        expected_json = '{"data": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
