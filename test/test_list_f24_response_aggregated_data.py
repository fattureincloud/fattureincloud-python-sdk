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
from fattureincloud_python_sdk.model.list_f24_response_aggregated_data import ListF24ResponseAggregatedData
from fattureincloud_python_sdk.model.list_f24_response_aggregation import ListF24ResponseAggregation


class TestListF24ResponseAggregatedData(unittest.TestCase):
    """ListF24ResponseAggregatedData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListF24ResponseAggregatedData(self):
        """Test ListF24ResponseAggregatedData"""
        model = ListF24ResponseAggregatedData(
            aggregated_data=ListF24ResponseAggregation(
                amount=10.0
            )
        )
        expected_json = "{'aggregated_data': {'amount': 10.0}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json
        

if __name__ == '__main__':
    unittest.main()
