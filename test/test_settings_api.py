"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import RESTResponse
import functions
from fattureincloud_python_sdk.api.settings_api import SettingsApi
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.payment_method import PaymentMethod
from fattureincloud_python_sdk.model.payment_method_details import PaymentMethodDetails
from fattureincloud_python_sdk.model.payment_method_type import PaymentMethodType
from fattureincloud_python_sdk.model.vat_type import VatType
from fattureincloud_python_sdk.model.create_payment_account_response import CreatePaymentAccountResponse
from fattureincloud_python_sdk.model.create_payment_method_response import CreatePaymentMethodResponse
from fattureincloud_python_sdk.model.create_vat_type_response import CreateVatTypeResponse
from fattureincloud_python_sdk.model.get_payment_account_response import GetPaymentAccountResponse
from fattureincloud_python_sdk.model.get_payment_method_response import GetPaymentMethodResponse
from fattureincloud_python_sdk.model.get_vat_type_response import GetVatTypeResponse
from fattureincloud_python_sdk.model.modify_payment_account_response import ModifyPaymentAccountResponse
from fattureincloud_python_sdk.model.modify_payment_method_response import ModifyPaymentMethodResponse
from fattureincloud_python_sdk.model.modify_vat_type_response import ModifyVatTypeResponse


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = SettingsApi()

    def tearDown(self):
        pass

    def test_create_payment_account(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.POST = unittest.mock.MagicMock(return_value = mock_resp)
        expected = CreatePaymentAccountResponse(data = PaymentAccount( id=2, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True ) )
        actual = self.api.create_payment_account(2)
        actual.data.id = 2
        assert actual == expected

    def test_create_payment_method(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.POST = unittest.mock.MagicMock(return_value = mock_resp)
        expected = CreatePaymentMethodResponse(data = PaymentMethod( id=2, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example" ) )
        actual = self.api.create_payment_method(2)
        actual.data.id = 2
        assert actual == expected

    def test_create_vat_type(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.POST = unittest.mock.MagicMock(return_value = mock_resp)
        expected = CreateVatTypeResponse(data = VatType( id=2, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True ) )
        actual = self.api.create_vat_type(2)
        actual.data.id = 2
        assert actual == expected

    def test_delete_payment_account(self):
        pass

    def test_delete_payment_method(self):
        pass

    def test_delete_vat_type(self):
        pass

    def test_get_payment_account(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetPaymentAccountResponse(data = PaymentAccount( id=2, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True ) )
        actual = self.api.get_payment_account(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_get_payment_method(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetPaymentMethodResponse(data = PaymentMethod( id=2, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example" ) )
        actual = self.api.get_payment_method(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_get_vat_type(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetVatTypeResponse(data = VatType( id=2, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True ) )
        actual = self.api.get_vat_type(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_modify_payment_account(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.PUT = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ModifyPaymentAccountResponse(data = PaymentAccount( id=2, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True ) )
        actual = self.api.modify_payment_account(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_modify_payment_method(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.PUT = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ModifyPaymentMethodResponse(data = PaymentMethod( id=2, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example" ) )
        actual = self.api.modify_payment_method(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_modify_vat_type(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.PUT = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ModifyVatTypeResponse(data = VatType( id=2, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True ) )
        actual = self.api.modify_vat_type(2, 12345)
        actual.data.id = 2
        assert actual == expected


if __name__ == '__main__':
    unittest.main()
