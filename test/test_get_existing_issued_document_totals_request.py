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
import dateutil
import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.issued_document import IssuedDocument
from fattureincloud_python_sdk.model.issued_document_type import IssuedDocumentType
globals()['IssuedDocument'] = IssuedDocument
from fattureincloud_python_sdk.model.get_existing_issued_document_totals_request import GetExistingIssuedDocumentTotalsRequest


class TestGetExistingIssuedDocumentTotalsRequest(unittest.TestCase):
    """GetExistingIssuedDocumentTotalsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetExistingIssuedDocumentTotalsRequest(self):
        """Test GetExistingIssuedDocumentTotalsRequest"""
        model = GetExistingIssuedDocumentTotalsRequest(
            data=IssuedDocument(
                id=1,
                type=IssuedDocumentType("invoice"),
                number=1,
                numeration="/A",
                date=dateutil.parser.parse('2022.01.01').date(),
                year=1,
                subject="subject_example",
                visible_subject="visible_subject_example",
                rc_center="rc_center_example",
                notes="notes_example",
                rivalsa=0.0,
                cassa=0.0,
                cassa_taxable=0.0,
                amount_cassa_taxable=3.14,
                cassa2=0.0,
                cassa2_taxable=0.0,
                amount_cassa2_taxable=3.14,
                global_cassa_taxable=0.0,
                amount_global_cassa_taxable=3.14
            )
        )
        expected_json = "{'data': {'amount_cassa2_taxable': 3.14,          'amount_cassa_taxable': 3.14,          'amount_global_cassa_taxable': 3.14,          'cassa': 0.0,          'cassa2': 0.0,          'cassa2_taxable': 0.0,          'cassa_taxable': 0.0,          'date': datetime.date(2022, 1, 1),          'global_cassa_taxable': 0.0,          'id': 1,          'notes': 'notes_example',          'number': 1,          'numeration': '/A',          'rc_center': 'rc_center_example',          'rivalsa': 0.0,          'subject': 'subject_example',          'type': 'invoice',          'visible_subject': 'visible_subject_example',          'year': 1}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
