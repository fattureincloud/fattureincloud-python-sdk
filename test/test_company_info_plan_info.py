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
from fattureincloud_python_sdk.model.company_info_plan_info_functions import (
    CompanyInfoPlanInfoFunctions,
)
from fattureincloud_python_sdk.model.company_info_plan_info_functions_status import (
    CompanyInfoPlanInfoFunctionsStatus,
)
from fattureincloud_python_sdk.model.company_info_plan_info_limits import (
    CompanyInfoPlanInfoLimits,
)
from fattureincloud_python_sdk.model.function_status import FunctionStatus

globals()["CompanyInfoPlanInfoFunctions"] = CompanyInfoPlanInfoFunctions
globals()["CompanyInfoPlanInfoFunctionsStatus"] = CompanyInfoPlanInfoFunctionsStatus
globals()["CompanyInfoPlanInfoLimits"] = CompanyInfoPlanInfoLimits
from fattureincloud_python_sdk.model.company_info_plan_info import CompanyInfoPlanInfo


class TestCompanyInfoPlanInfo(unittest.TestCase):
    """CompanyInfoPlanInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompanyInfoPlanInfo(self):
        """Test CompanyInfoPlanInfo"""
        model = CompanyInfoPlanInfo(
            limits=CompanyInfoPlanInfoLimits(
                clients=4000, suppliers=4000, products=4000, documents=4000
            ),
            functions=CompanyInfoPlanInfoFunctions(
                archive=True, cerved=True, document_attachments=True
            ),
            functions_status=CompanyInfoPlanInfoFunctionsStatus(
                ts_digitaL=FunctionStatus(active=True),
                ts_pay=FunctionStatus(actiive=True),
            ),
        )
        expected_json = '{"limits": {"clients": 4000, "suppliers": 4000, "products": 4000, "documents": 4000}, "functions": {"archive": true, "cerved": true, "document_attachments": true}, "functions_status": {"ts_digitaL": {"active": true}, "ts_pay": {"actiive": true}}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
