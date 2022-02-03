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
from fattureincloud_python_sdk.model.received_document import ReceivedDocument
from fattureincloud_python_sdk.model.currency import Currency
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.received_document_entity import ReceivedDocumentEntity
from fattureincloud_python_sdk.model.received_document_items_list import ReceivedDocumentItemsList
from fattureincloud_python_sdk.model.received_document_payment_terms import ReceivedDocumentPaymentTerms
from fattureincloud_python_sdk.model.received_document_payments_list import ReceivedDocumentPaymentsList
from fattureincloud_python_sdk.model.received_document_type import ReceivedDocumentType
from fattureincloud_python_sdk.model.vat_type import VatType
globals()['ReceivedDocument'] = ReceivedDocument
from fattureincloud_python_sdk.model.create_received_document_request import CreateReceivedDocumentRequest


class TestCreateReceivedDocumentRequest(unittest.TestCase):
    """CreateReceivedDocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateReceivedDocumentRequest(self):
        """Test CreateReceivedDocumentRequest"""
        model = CreateReceivedDocumentRequest(
            pending_id=1,
            data=ReceivedDocument(
                id=1,
                type=ReceivedDocumentType("expense"),
                entity=ReceivedDocumentEntity(
                    id=1,
                    name="name_example",
                ),
                date=dateutil.parser.parse('2022-01-01').date(),
                category="category_example",
                description="description_example",
                amount_net=3.14,
                amount_vat=3.14,
                amount_withholding_tax=3.14,
                amount_other_withholding_tax=3.14,
                amortization=3.14,
                rc_center="rc_center_example",
                invoice_number="invoice_number_example",
                is_marked=True,
                is_detailed=True,
                e_invoice=True,
                tax_deductibility=0.0,
                vat_deductibility=0.0,
                items_list=[
                    ReceivedDocumentItemsList(
                        id=1,
                        product_id=1,
                        code="code_example",
                        name="name_example",
                        measure="measure_example",
                        net_price=3.14,
                        category="category_example",
                        qty=3.14,
                        vat=VatType(
                            id=1,
                            value=22.0,
                            description="Non imponibile art. 123",
                            notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                            e_invoice=True,
                            ei_type="2",
                            ei_description="ei_description_example",
                            is_disabled=True,
                        ),
                        stock=3.14,
                    ),
                ]
            )
        )
        expected_json = "{'data': {'amortization': 3.14,          'amount_net': 3.14,          'amount_other_withholding_tax': 3.14,          'amount_vat': 3.14,          'amount_withholding_tax': 3.14,          'category': 'category_example',          'date': datetime.date(2022, 1, 1),          'description': 'description_example',          'e_invoice': True,          'entity': {'id': 1, 'name': 'name_example'},          'id': 1,          'invoice_number': 'invoice_number_example',          'is_detailed': True,          'is_marked': True,          'items_list': [{'category': 'category_example',                          'code': 'code_example',                          'id': 1,                          'measure': 'measure_example',                          'name': 'name_example',                          'net_price': 3.14,                          'product_id': 1,                          'qty': 3.14,                          'stock': 3.14,                          'vat': {'description': 'Non imponibile art. 123',                                  'e_invoice': True,                                  'ei_description': 'ei_description_example',                                  'ei_type': '2',                                  'id': 1,                                  'is_disabled': True,                                  'notes': 'IVA non imponibile ai sensi dell '                                           'articolo 123, comma 2',                                  'value': 22.0}}],          'rc_center': 'rc_center_example',          'tax_deductibility': 0.0,          'type': 'expense',          'vat_deductibility': 0.0}, 'pending_id': 1}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
