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
from fattureincloud_python_sdk.model.company_info_access_info import CompanyInfoAccessInfo
from fattureincloud_python_sdk.model.company_info_plan_info import CompanyInfoPlanInfo
from fattureincloud_python_sdk.model.company_type import CompanyType
from fattureincloud_python_sdk.model.company_info_plan_info_functions import CompanyInfoPlanInfoFunctions
from fattureincloud_python_sdk.model.company_info_plan_info_functions_status import CompanyInfoPlanInfoFunctionsStatus
from fattureincloud_python_sdk.model.company_info_plan_info_limits import CompanyInfoPlanInfoLimits
from fattureincloud_python_sdk.model.function_status import FunctionStatus
from fattureincloud_python_sdk.model.permissions import Permissions
from fattureincloud_python_sdk.model.user_company_role import UserCompanyRole
globals()['CompanyInfoAccessInfo'] = CompanyInfoAccessInfo
globals()['CompanyInfoPlanInfo'] = CompanyInfoPlanInfo
globals()['CompanyType'] = CompanyType
from fattureincloud_python_sdk.model.company_info import CompanyInfo


class TestCompanyInfo(unittest.TestCase):
    """CompanyInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompanyInfo(self):
        """Test CompanyInfo"""
        model = CompanyInfo(
            id=1,
            name="mario",
            email="mariomail@gm.co",
            type=CompanyType("company"),
            accountant_id=10,
            is_accountant=True,
            access_info=CompanyInfoAccessInfo(
                role=UserCompanyRole("master"),
                permissions=Permissions(),
                through_accountant=True
            ),
            plan_info=CompanyInfoPlanInfo(
                limits=CompanyInfoPlanInfoLimits(
                    clients=4000,
                    suppliers=4000,
                    products=4000,
                    documents=4000
                ),
                functions=CompanyInfoPlanInfoFunctions(
                    archive=True,
                    cerved=True,
                    document_attachments=True
                ),
                functions_status=CompanyInfoPlanInfoFunctionsStatus(
                    ts_digitaL=FunctionStatus(
                        active=True
                    ),
                    ts_pay=FunctionStatus(
                        actiive=True
                    )
                )
            )
        )
        expected_json = "{'access_info': {'permissions': {},                 'role': 'master',                 'through_accountant': True}, 'accountant_id': 10, 'email': 'mariomail@gm.co', 'id': 1, 'is_accountant': True, 'name': 'mario', 'plan_info': {'functions': {'archive': True,                             'cerved': True,                             'document_attachments': True},               'functions_status': {'ts_digitaL': {'active': True},                                    'ts_pay': {'actiive': True}},               'limits': {'clients': 4000,                          'documents': 4000,                          'products': 4000,                          'suppliers': 4000}}, 'type': 'company'}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
