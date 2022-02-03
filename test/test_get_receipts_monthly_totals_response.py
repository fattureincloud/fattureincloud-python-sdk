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
from fattureincloud_python_sdk.model.monthly_total import MonthlyTotal
globals()['MonthlyTotal'] = MonthlyTotal
from fattureincloud_python_sdk.model.get_receipts_monthly_totals_response import GetReceiptsMonthlyTotalsResponse


class TestGetReceiptsMonthlyTotalsResponse(unittest.TestCase):
    """GetReceiptsMonthlyTotalsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetReceiptsMonthlyTotalsResponse(self):
        """Test GetReceiptsMonthlyTotalsResponse"""
        model = GetReceiptsMonthlyTotalsResponse(
            data=[
                MonthlyTotal(
                    net=1000.0,
                    gross=1220.0,
                    count=10.0
                ),
                MonthlyTotal(
                    net=1500.0,
                    gross=1730.0,
                    count=15.0
                )
            ]
        )
        expected_json = "{'data': [{'count': 10.0, 'gross': 1220.0, 'net': 1000.0},          {'count': 15.0, 'gross': 1730.0, 'net': 1500.0}]}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
