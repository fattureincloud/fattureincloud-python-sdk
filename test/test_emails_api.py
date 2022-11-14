"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.21
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.emails_api import EmailsApi  # noqa: E501


class TestEmailsApi(unittest.TestCase):
    """EmailsApi unit test stubs"""

    def setUp(self):
        self.api = EmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_emails(self):
        """Test case for list_emails

        List emails  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
