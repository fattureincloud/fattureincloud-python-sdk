"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.issued_documents_api import IssuedDocumentsApi  # noqa: E501


class TestIssuedDocumentsApi(unittest.TestCase):
    """IssuedDocumentsApi unit test stubs"""

    def setUp(self):
        self.api = IssuedDocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_issued_document(self):
        """Test case for create_issued_document

        Create Issued Document  # noqa: E501
        """
        pass

    def test_delete_issued_document(self):
        """Test case for delete_issued_document

        Delete Issued Document  # noqa: E501
        """
        pass

    def test_delete_issued_document_attachment(self):
        """Test case for delete_issued_document_attachment

        Delete Issued Document Attachment  # noqa: E501
        """
        pass

    def test_get_email_data(self):
        """Test case for get_email_data

        Get Email Data  # noqa: E501
        """
        pass

    def test_get_existing_issued_document_totals(self):
        """Test case for get_existing_issued_document_totals

        Get Existing Issued Document Totals  # noqa: E501
        """
        pass

    def test_get_issued_document(self):
        """Test case for get_issued_document

        Get Issued Document  # noqa: E501
        """
        pass

    def test_get_issued_document_pre_create_info(self):
        """Test case for get_issued_document_pre_create_info

        Get Issued Document Pre-create info  # noqa: E501
        """
        pass

    def test_get_new_issued_document_totals(self):
        """Test case for get_new_issued_document_totals

        Get New Issued Document Totals  # noqa: E501
        """
        pass

    def test_list_issued_documents(self):
        """Test case for list_issued_documents

        List Issued Documents  # noqa: E501
        """
        pass

    def test_modify_issued_document(self):
        """Test case for modify_issued_document

        Modify Issued Document  # noqa: E501
        """
        pass

    def test_schedule_email(self):
        """Test case for schedule_email

        Schedule Email  # noqa: E501
        """
        pass

    def test_upload_issued_document_attachment(self):
        """Test case for upload_issued_document_attachment

        Upload Issued Document Attachment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
