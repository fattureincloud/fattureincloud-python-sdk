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
from fattureincloud_python_sdk.model.supplier import Supplier
from fattureincloud_python_sdk.model.supplier_type import SupplierType
globals()['Supplier'] = Supplier
from fattureincloud_python_sdk.model.get_supplier_response import GetSupplierResponse


class TestGetSupplierResponse(unittest.TestCase):
    """GetSupplierResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetSupplierResponse(self):
        """Test GetSupplierResponse"""
        model = GetSupplierResponse(
            data=Supplier(
                id=1,
                code="123",
                name="Rossi S.r.l.",
                type=SupplierType("company"),
                first_name="first_name_example",
                last_name="last_name_example",
                contact_person="contact_person_example",
                vat_number="IT01234567890",
                tax_code="RSSMRA44A12E890Q",
                address_street="Via dei tigli, 12",
                address_postal_code="24010",
                address_city="Bergamo",
                address_province="BG",
                address_extra="address_extra_example",
                country="Italia",
                email="mario.rossi@example.it",
                certified_email="mario.rossi@pec.example.it",
                phone="phone_example",
                fax="fax_example",
                notes="notes_example",
                created_at="created_at_example",
                updated_at="updated_at_example",
            )
        )
        expected_json = "{'data': {'address_city': 'Bergamo',          'address_extra': 'address_extra_example',          'address_postal_code': '24010',          'address_province': 'BG',          'address_street': 'Via dei tigli, 12',          'certified_email': 'mario.rossi@pec.example.it',          'code': '123',          'contact_person': 'contact_person_example',          'country': 'Italia',          'created_at': 'created_at_example',          'email': 'mario.rossi@example.it',          'fax': 'fax_example',          'first_name': 'first_name_example',          'id': 1,          'last_name': 'last_name_example',          'name': 'Rossi S.r.l.',          'notes': 'notes_example',          'phone': 'phone_example',          'tax_code': 'RSSMRA44A12E890Q',          'type': 'company',          'updated_at': 'updated_at_example',          'vat_number': 'IT01234567890'}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
