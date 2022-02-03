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
from fattureincloud_python_sdk.model.attachment_data import AttachmentData
globals()['AttachmentData'] = AttachmentData
from fattureincloud_python_sdk.model.upload_archive_attachment_response import UploadArchiveAttachmentResponse


class TestUploadArchiveAttachmentResponse(unittest.TestCase):
    """UploadArchiveAttachmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUploadArchiveAttachmentResponse(self):
        """Test UploadArchiveAttachmentResponse"""
        model = UploadArchiveAttachmentResponse(
            data=AttachmentData(attachment_token="bf98dhAJSHGD9dfyds9af8yd8f")
        )
        expected_json = "{'data': {'attachment_token': 'bf98dhAJSHGD9dfyds9af8yd8f'}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json

if __name__ == '__main__':
    unittest.main()
