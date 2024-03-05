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
from fattureincloud_python_sdk.models.cashbook_entry_document import (
    CashbookEntryDocument,
)
from fattureincloud_python_sdk.models.cashbook_entry import CashbookEntry
from fattureincloud_python_sdk.models.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.models.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.models.payment_account import PaymentAccount

globals()["CashbookEntryDocument"] = CashbookEntryDocument
globals()["CashbookEntry"] = CashbookEntry
globals()["CashbookEntryKind"] = CashbookEntryKind
globals()["CashbookEntryType"] = CashbookEntryType
globals()["PaymentAccount"] = PaymentAccount


class TestCashbookEntry(unittest.TestCase):
    """CashbookEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCashbookEntry(self):
        """Test CashbookEntry"""
        model = CashbookEntry(
            id="1",
            date=datetime.datetime.strptime("2022-02-02", "%Y-%m-%d").date(),
            description="description",
            kind=CashbookEntryKind("cashbook"),
            type=CashbookEntryType("in"),
            entity_name="name",
            document=CashbookEntryDocument(id=1, path="/path", type="doc"),
            amount_in=10.0,
            payment_account_in=PaymentAccount(id=1, name="banca"),
            amount_out=0.0,
            payment_account_out=PaymentAccount(id=1, name="banca"),
        )
        expected_json = '{"id": "1", "date": "2022-02-02", "description": "description", "kind": "cashbook", "type": "in", "entity_name": "name", "document": {"id": 1, "type": "doc", "path": "/path"}, "amount_in": 10.0, "payment_account_in": {"id": 1, "name": "banca"}, "amount_out": 0.0, "payment_account_out": {"id": 1, "name": "banca"}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
