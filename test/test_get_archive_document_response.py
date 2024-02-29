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
import datetime
import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.models.archive_document import ArchiveDocument

globals()["ArchiveDocument"] = ArchiveDocument
from fattureincloud_python_sdk.models.get_archive_document_response import (
    GetArchiveDocumentResponse,
)


class TestGetArchiveDocumentResponse(unittest.TestCase):
    """GetArchiveDocumentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetArchiveDocumentResponse(self):
        """Test GetArchiveDocumentResponse"""
        model = GetArchiveDocumentResponse(
            data=ArchiveDocument(
                id=1,
                date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                description="description_example",
                category="category_example",
                attachment_token="attachment_token_example",
            )
        )
        expected_json = '{"data": {"id": 1, "date": "2022-01-01", "description": "description_example", "category": "category_example", "attachment_token": "attachment_token_example"}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
