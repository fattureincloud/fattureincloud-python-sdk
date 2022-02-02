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
from fattureincloud_python_sdk.model.cashbook_entry_data_document import CashbookEntryDataDocument
from fattureincloud_python_sdk.model.cashbook_entry_in import CashbookEntryIn
from fattureincloud_python_sdk.model.cashbook_entry_kind import CashbookEntryKind
from fattureincloud_python_sdk.model.cashbook_entry_out import CashbookEntryOut
from fattureincloud_python_sdk.model.cashbook_entry_type import CashbookEntryType
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
globals()['CashbookEntryDataDocument'] = CashbookEntryDataDocument
globals()['CashbookEntryIn'] = CashbookEntryIn
globals()['CashbookEntryKind'] = CashbookEntryKind
globals()['CashbookEntryOut'] = CashbookEntryOut
globals()['CashbookEntryType'] = CashbookEntryType
globals()['PaymentAccount'] = PaymentAccount
from fattureincloud_python_sdk.model.cashbook_entry import CashbookEntry


class TestCashbookEntry(unittest.TestCase):
    """CashbookEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCashbookEntry(self):
        """Test CashbookEntry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CashbookEntry()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
