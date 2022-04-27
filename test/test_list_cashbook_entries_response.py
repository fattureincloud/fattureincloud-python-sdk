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
from fattureincloud_python_sdk.model.cashbook_entry import CashbookEntry
from fattureincloud_python_sdk.model.cashbook_entry_document import (
    CashbookEntryDocument,
)
from fattureincloud_python_sdk.model.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.model.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.model.payment_account import PaymentAccount

globals()["CashbookEntry"] = CashbookEntry
from fattureincloud_python_sdk.model.list_cashbook_entries_response import (
    ListCashbookEntriesResponse,
)


class TestListCashbookEntriesResponse(unittest.TestCase):
    """ListCashbookEntriesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListCashbookEntriesResponse(self):
        """Test ListCashbookEntriesResponse"""
        model = ListCashbookEntriesResponse(
            data=[
                CashbookEntry(
                    id="1",
                    date=datetime.datetime.strptime("2022-02-02", "%Y-%m-%d").date(),
                    description="description",
                    kind=CashbookEntryKind("cashbook"),
                    type=CashbookEntryType("in"),
                    entity_name="name",
                    document=CashbookEntryDocument(id=1, path="/path", type="doc"),
                    amount_in=10.0,
                    payment_account_in=PaymentAccount(id=1, name="banca"),
                )
            ],
            current_page=10,
            first_page_url="http://url.com",
            last_page=10,
            last_page_url="http://url.com",
            next_page_url="http://url.com",
            path="http://url.com",
            per_page=10,
            prev_page_url="http://url.com",
            to=10,
            total=10,
        )
        expected_json = '{"data": [{"id": "1", "date": "2022-02-02", "description": "description", "kind": "cashbook", "type": "in", "entity_name": "name", "document": {"id": 1, "path": "/path", "type": "doc"}, "amount_in": 10.0, "payment_account_in": {"id": 1, "name": "banca"}}], "current_page": 10, "first_page_url": "http://url.com", "last_page": 10, "last_page_url": "http://url.com", "next_page_url": "http://url.com", "path": "http://url.com", "per_page": 10, "prev_page_url": "http://url.com", "to": 10, "total": 10}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
