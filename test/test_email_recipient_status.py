"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.22
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.email_recipient_status import EmailRecipientStatus


class TestEmailRecipientStatus(unittest.TestCase):
    """EmailRecipientStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmailRecipientStatus(self):
        """Test EmailRecipientStatus"""
        model = EmailRecipientStatus("unknown")
        expected_json = "unknown"
        actual_json = model.value
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
