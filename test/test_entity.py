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

import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.payment_terms_type import PaymentTermsType
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.models.client import Client

from fattureincloud_python_sdk.models.entity_type import EntityType
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.models.payment_method import PaymentMethod
from fattureincloud_python_sdk.models.payment_method_details import PaymentMethodDetails
from fattureincloud_python_sdk.models.payment_method_type import PaymentMethodType
from fattureincloud_python_sdk.models.supplier import Supplier
from fattureincloud_python_sdk.models.supplier_type import SupplierType
from fattureincloud_python_sdk.models.vat_type import VatType
from fattureincloud_python_sdk.models.entity import Entity

globals()["Client"] = Client
globals()["PaymentTermsType"] = PaymentTermsType
globals()["PaymentMethod"] = PaymentMethod
globals()["Supplier"] = Supplier
globals()["SupplierType"] = SupplierType
globals()["VatType"] = VatType


class TestEntity(unittest.TestCase):
    """Entity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntity(self):
        """Test Entity"""
        model = Entity(
            id=1,
            code="123",
            name="Rossi S.r.l.",
            type=EntityType("company"),
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
            default_payment_terms=30,
            default_payment_terms_type=PaymentTermsType("standard"),
            default_payment_method=PaymentMethod(
                id=1,
                name="name_example",
                type=PaymentMethodType("standard"),
                is_default=True,
                default_payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                details=[
                    PaymentMethodDetails(
                        title="title_example",
                        description="description_example",
                    ),
                ],
                bank_iban="bank_iban_example",
                bank_name="bank_name_example",
                bank_beneficiary="bank_beneficiary_example",
                ei_payment_method="ei_payment_method_example",
            ),
            bank_name="bank_name_example",
            bank_iban="bank_iban_example",
            bank_swift_code="bank_swift_code_example",
            shipping_address="shipping_address_example",
            e_invoice=False,
            ei_code="ei_code_example",
            created_at="created_at_example",
            updated_at="updated_at_example",
        )
        expected_json = '{"id": 1, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "default_payment_terms": 30, "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "default_payment_terms_type": "standard", "default_payment_method": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}, "bank_name": "bank_name_example", "bank_iban": "bank_iban_example", "bank_swift_code": "bank_swift_code_example", "shipping_address": "shipping_address_example", "e_invoice": false, "ei_code": "ei_code_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
