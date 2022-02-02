"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.archive_document import ArchiveDocument
from fattureincloud_python_sdk.model.list_archive_documents_response_page import ListArchiveDocumentsResponsePage
from fattureincloud_python_sdk.model.pagination import Pagination
globals()['ArchiveDocument'] = ArchiveDocument
globals()['ListArchiveDocumentsResponsePage'] = ListArchiveDocumentsResponsePage
globals()['Pagination'] = Pagination
from fattureincloud_python_sdk.model.list_archive_documents_response import ListArchiveDocumentsResponse


class TestListArchiveDocumentsResponse(unittest.TestCase):
    """ListArchiveDocumentsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListArchiveDocumentsResponse(self):
        """Test ListArchiveDocumentsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListArchiveDocumentsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
