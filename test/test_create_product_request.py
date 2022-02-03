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

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.product import Product
from fattureincloud_python_sdk.model.vat_type import VatType
globals()['Product'] = Product
from fattureincloud_python_sdk.model.create_product_request import CreateProductRequest


class TestCreateProductRequest(unittest.TestCase):
    """CreateProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateProductRequest(self):
        """Test CreateProductRequest"""
        model = CreateProductRequest(  
            data=Product(
                id=1,
                name="name_example",
                code="code_example",
                net_price=3.14,
                gross_price=3.14,
                use_gross_price=True,
                default_vat=VatType(
                    id=1,
                    value=22.0,
                    description="Non imponibile art. 123",
                    notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                    e_invoice=True,
                    ei_type="2",
                    ei_description="ei_description_example",
                    is_disabled=True,
                ),
                net_cost=3.14,
                measure="measure_example",
                description="description_example",
                category="category_example",
                notes="notes_example",
                in_stock=True,
                stock_initial=3.14,
                average_cost=3.14,
                average_price=3.14,
                created_at="created_at_example",
                updated_at="updated_at_example",
            )
        )
        expected_json = "{'data': {'average_cost': 3.14,          'average_price': 3.14,          'category': 'category_example',          'code': 'code_example',          'created_at': 'created_at_example',          'default_vat': {'description': 'Non imponibile art. 123',                          'e_invoice': True,                          'ei_description': 'ei_description_example',                          'ei_type': '2',                          'id': 1,                          'is_disabled': True,                          'notes': 'IVA non imponibile ai sensi dell articolo '                                   '123, comma 2',                          'value': 22.0},          'description': 'description_example',          'gross_price': 3.14,          'id': 1,          'in_stock': True,          'measure': 'measure_example',          'name': 'name_example',          'net_cost': 3.14,          'net_price': 3.14,          'notes': 'notes_example',          'stock_initial': 3.14,          'updated_at': 'updated_at_example',          'use_gross_price': True}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
