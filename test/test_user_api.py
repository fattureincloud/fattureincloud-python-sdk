"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_info(self):
        """Test case for get_user_info

        Get User Info  # noqa: E501
        """
        pass

    def test_list_user_companies(self):
        """Test case for list_user_companies

        List User Companies  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
