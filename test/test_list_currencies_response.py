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
from fattureincloud_python_sdk.model.currency import Currency
globals()['Currency'] = Currency
from fattureincloud_python_sdk.model.list_currencies_response import ListCurrenciesResponse


class TestListCurrenciesResponse(unittest.TestCase):
    """ListCurrenciesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListCurrenciesResponse(self):
        """Test ListCurrenciesResponse"""
        model = ListCurrenciesResponse(
            data=[
                Currency(
                    id="EUR",
                    symbol="e",
                    exchange_rate="1.000"
                ),
                Currency(
                    id="USD",
                    symbol="s",
                    exchange_rate="1.200"
                )
            ]
        )
        expected_json = "{'data': [{'exchange_rate': '1.000', 'id': 'EUR', 'symbol': 'e'},          {'exchange_rate': '1.200', 'id': 'USD', 'symbol': 's'}]}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json

if __name__ == '__main__':
    unittest.main()
