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
from fattureincloud_python_sdk.model.pagination import Pagination


class TestPagination(unittest.TestCase):
    """Pagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagination(self):
        """Test Pagination"""
        model = Pagination(
            current_page=10,
            first_page_url="http://url.com",
            last_page=10,
            last_page_url="http://url.com",
            next_page_url="http://url.com",
            path="http://url.com",
            per_page=10,
            prev_page_url="http://url.com",
            to=10,
            total=10
        )
        expected_json = "{'current_page': 10, 'first_page_url': 'http://url.com', 'last_page': 10, 'last_page_url': 'http://url.com', 'next_page_url': 'http://url.com', 'path': 'http://url.com', 'per_page': 10, 'prev_page_url': 'http://url.com', 'to': 10, 'total': 10}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json
        

if __name__ == '__main__':
    unittest.main()
