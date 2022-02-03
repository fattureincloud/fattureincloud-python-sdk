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
import dateutil
import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.archive_document import ArchiveDocument
globals()['ArchiveDocument'] = ArchiveDocument
from fattureincloud_python_sdk.model.list_archive_documents_response_page import ListArchiveDocumentsResponsePage


class TestListArchiveDocumentsResponsePage(unittest.TestCase):
    """ListArchiveDocumentsResponsePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListArchiveDocumentsResponsePage(self):
        """Test ListArchiveDocumentsResponsePage"""
        model = ListArchiveDocumentsResponsePage(
            data=[
                ArchiveDocument(
                    id=1,
                    date=dateutil.parser.parse('2022-01-01').date(),
                    description="description_example",
                    category="category_example",
                    attachment_token="attachment_token_example"
                ),
                ArchiveDocument(
                    id=10,
                    date=dateutil.parser.parse('2022-01-02').date(),
                    description="description_example",
                    category="category_example",
                    attachment_token="attachment_token_example"
                )
            ]
        )
        expected_json = "{'data': [{'attachment_token': 'attachment_token_example',           'category': 'category_example',           'date': datetime.date(2022, 1, 1),           'description': 'description_example',           'id': 1},          {'attachment_token': 'attachment_token_example',           'category': 'category_example',           'date': datetime.date(2022, 1, 2),           'description': 'description_example',           'id': 10}]}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json

if __name__ == '__main__':
    unittest.main()
