"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from email import message
import json
import sys
import unittest

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.models.verify_e_invoice_xml_error_response_error import (
    VerifyEInvoiceXmlErrorResponseError,
)


class TestVerifyEInvoiceXmlErrorResponseError(unittest.TestCase):
    """VerifyEInvoiceXmlErrorResponseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVerifyEInvoiceXmlErrorResponseError(self):
        """Test VerifyEInvoiceXmlErrorResponseError"""
        model = VerifyEInvoiceXmlErrorResponseError(
            message="something is broken man", validation_result={}
        )
        expected_json = (
            '{"message": "something is broken man", "validation_result": {}}'
        )
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
