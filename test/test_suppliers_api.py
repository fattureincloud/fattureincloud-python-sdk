"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.8
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.suppliers_api import SuppliersApi
from fattureincloud_python_sdk.model.create_supplier_response import CreateSupplierResponse
from fattureincloud_python_sdk.model.supplier import Supplier
from fattureincloud_python_sdk.model.supplier_type import SupplierType
from fattureincloud_python_sdk.model.get_supplier_response import GetSupplierResponse
from fattureincloud_python_sdk.model.list_suppliers_response import ListSuppliersResponse
from fattureincloud_python_sdk.model.modify_supplier_response import ModifySupplierResponse  # noqa: E501


class TestSuppliersApi(unittest.TestCase):
    """SuppliersApi unit test stubs"""

    def setUp(self):
        self.api = SuppliersApi()

        supplier = Supplier( id=1, code="123", name="Rossi S.r.l.", type=SupplierType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", created_at="created_at_example", updated_at="updated_at_example" )
        
        self.api.create_supplier = unittest.mock.MagicMock(return_value = CreateSupplierResponse(data = supplier))
        self.api.delete_supplier = unittest.mock.MagicMock(return_value = "")
        self.api.get_supplier = unittest.mock.MagicMock(return_value = GetSupplierResponse(data = supplier))
        self.api.list_suppliers = unittest.mock.MagicMock(return_value = ListSuppliersResponse(data = [supplier, supplier]))
        self.api.modify_supplier = unittest.mock.MagicMock(return_value = ModifySupplierResponse(data = supplier))

    def tearDown(self):
        pass

    def test_create_supplier(self):
        expected = CreateSupplierResponse(data = Supplier( id=2, code="123", name="Rossi S.r.l.", type=SupplierType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", created_at="created_at_example", updated_at="updated_at_example" ) )
        actual = self.api.create_supplier(2, None)
        actual.data.id = 2
        assert actual == expected
        self.api.create_supplier.assert_called_with(2, None)

    def test_delete_supplier(self):
        self.api.delete_supplier(12345)
        self.api.delete_supplier.assert_called_with(12345)

    def test_get_supplier(self):
        expected = GetSupplierResponse(data = Supplier( id=2, code="123", name="Rossi S.r.l.", type=SupplierType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", created_at="created_at_example", updated_at="updated_at_example" ) )
        actual = self.api.get_supplier(2, 12345)
        actual.data.id = 2
        assert actual == expected
        self.api.get_supplier.assert_called_with(2, 12345)

    def test_list_suppliers(self):
        expected = ListSuppliersResponse(data = [Supplier( id=2, code="123", name="Rossi S.r.l.", type=SupplierType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", created_at="created_at_example", updated_at="updated_at_example" ), Supplier( id=2, code="123", name="Rossi S.r.l.", type=SupplierType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", created_at="created_at_example", updated_at="updated_at_example" )] )
        actual = self.api.list_suppliers(2, 12345)
        actual.data[0].id = 2
        assert actual == expected
        self.api.list_suppliers.assert_called_with(2, 12345)

    def test_modify_supplier(self):
        expected = ModifySupplierResponse(data = Supplier( id=2, code="123", name="Rossi S.r.l.", type=SupplierType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", created_at="created_at_example", updated_at="updated_at_example" ) )
        actual = self.api.modify_supplier(2, 12345, None)
        actual.data.id = 2
        assert actual == expected
        self.api.modify_supplier.assert_called_with(2, 12345, None)


if __name__ == '__main__':
    unittest.main()
