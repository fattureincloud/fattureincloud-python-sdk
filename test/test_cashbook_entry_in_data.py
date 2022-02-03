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
from fattureincloud_python_sdk.model.cashbook_entry_data_document import CashbookEntryDataDocument
from fattureincloud_python_sdk.model.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.model.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
globals()['PaymentAccount'] = PaymentAccount
from fattureincloud_python_sdk.model.cashbook_entry_in_data import CashbookEntryInData


class TestCashbookEntryInData(unittest.TestCase):
    """CashbookEntryInData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCashbookEntryInData(self):
        """Test CashbookEntryInData"""
        model = CashbookEntryInData(
            id="1",
            date=dateutil.parser.parse("05.01.2015").date(),
            description="description",
            kind=CashbookEntryKind("cashbook"),
            type=CashbookEntryType("in"),
            entity_name="name",
                document=CashbookEntryDataDocument(
                id=1,
                path="/path",
                type="doc"
            ),
            amount_in=10.0,
            payment_account_in=PaymentAccount(
                id=1,
                name="banca"
            )
        )
        expected_json = "{'amount_in': 10.0, 'date': datetime.date(2015, 5, 1), 'description': 'description', 'document': {'id': 1, 'path': '/path', 'type': 'doc'}, 'entity_name': 'name', 'id': '1', 'kind': 'cashbook', 'payment_account_in': {'id': 1, 'name': 'banca'}, 'type': 'in'}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
