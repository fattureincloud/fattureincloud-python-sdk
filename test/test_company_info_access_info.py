"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from doctest import master
import json
import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.permissions import Permissions
from fattureincloud_python_sdk.model.user_company_role import UserCompanyRole
globals()['Permissions'] = Permissions
globals()['UserCompanyRole'] = UserCompanyRole
from fattureincloud_python_sdk.model.company_info_access_info import CompanyInfoAccessInfo


class TestCompanyInfoAccessInfo(unittest.TestCase):
    """CompanyInfoAccessInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompanyInfoAccessInfo(self):
        """Test CompanyInfoAccessInfo"""
        model = CompanyInfoAccessInfo(
            role=UserCompanyRole("master"),
            permissions=Permissions(

            ),
            through_accountant=True
        )
        expected_json = "{'permissions': {}, 'role': 'master', 'through_accountant': True}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json

if __name__ == '__main__':
    unittest.main()
