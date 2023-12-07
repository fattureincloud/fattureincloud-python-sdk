"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from re import M
import unittest
import unittest.mock
import datetime
import fattureincloud_python_sdk
import functions
from fattureincloud_python_sdk.rest import RESTResponse
from fattureincloud_python_sdk.api.taxes_api import TaxesApi
from fattureincloud_python_sdk.models.attachment_data import AttachmentData
from fattureincloud_python_sdk.models.create_f24_response import CreateF24Response
from fattureincloud_python_sdk.models.f24 import F24
from fattureincloud_python_sdk.models.f24_status import F24Status
from fattureincloud_python_sdk.models.get_f24_response import GetF24Response
from fattureincloud_python_sdk.models.list_f24_response import ListF24Response
from fattureincloud_python_sdk.models.modify_f24_response import ModifyF24Response
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.models.upload_f24_attachment_response import (
    UploadF24AttachmentResponse,
)  # noqa: E501


class TestTaxesApi(unittest.TestCase):
    """TaxesApi unit test stubs"""

    def setUp(self):
        self.api = TaxesApi()

    def tearDown(self):
        pass

    def test_create_f24(self):
        resp = {
            "status": 200,
            "data": b'{"data": {"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"}}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = CreateF24Response(
            data=F24(
                id=2,
                due_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                status=F24Status("paid"),
                payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                amount=300.0,
                attachment_token="attachment_token_example",
                description="description_example",
            )
        )
        actual = self.api.create_f24(2)
        actual.data.id = 2
        assert actual == expected

    def test_delete_f24(self):
        pass

    def test_delete_f24_attachment(self):
        pass

    def test_get_f24(self):
        resp = {
            "status": 200,
            "data": b'{"data": {"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"}}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = GetF24Response(
            data=F24(
                id=2,
                due_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                status=F24Status("paid"),
                payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                amount=300.0,
                attachment_token="attachment_token_example",
                description="description_example",
            )
        )
        actual = self.api.get_f24(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_list_f24(self):
        resp = {
            "status": 200,
            "data": b'{"data": [{"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"},{"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"}]}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = ListF24Response(
            data=[
                F24(
                    id=2,
                    due_date=datetime.datetime.strptime(
                        "2022-01-01", "%Y-%m-%d"
                    ).date(),
                    status=F24Status("paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    amount=300.0,
                    attachment_token="attachment_token_example",
                    description="description_example",
                ),
                F24(
                    id=2,
                    due_date=datetime.datetime.strptime(
                        "2022-01-01", "%Y-%m-%d"
                    ).date(),
                    status=F24Status("paid"),
                    payment_account=PaymentAccount(
                        id=1,
                        name="Conto Banca Intesa",
                        type=PaymentAccountType("standard"),
                        iban="iban_example",
                        sia="sia_example",
                        cuc="cuc_example",
                        virtual=True,
                    ),
                    amount=300.0,
                    attachment_token="attachment_token_example",
                    description="description_example",
                ),
            ]
        )
        actual = self.api.list_f24(2)
        actual.data[0].id = 2
        actual.data[1].id = 2
        assert actual == expected

    def test_modify_f24(self):
        resp = {
            "status": 200,
            "data": b'{"data": {"id": 1, "due_date": "2022-01-01", "status": "paid", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "amount": 300.0, "attachment_token": "attachment_token_example", "description": "description_example"}}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = ModifyF24Response(
            data=F24(
                id=2,
                due_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                status=F24Status("paid"),
                payment_account=PaymentAccount(
                    id=1,
                    name="Conto Banca Intesa",
                    type=PaymentAccountType("standard"),
                    iban="iban_example",
                    sia="sia_example",
                    cuc="cuc_example",
                    virtual=True,
                ),
                amount=300.0,
                attachment_token="attachment_token_example",
                description="description_example",
            )
        )
        actual = self.api.modify_f24(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_upload_f24_attachment(self):
        resp = {
            "status": 200,
            "data": b'{"data": {"attachment_token": "aisdfvbgablsi9876r8o3qw36"}}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = UploadF24AttachmentResponse(
            data=AttachmentData(attachment_token="aisdfvbgablsi9876r8o3qw36")
        )
        actual = self.api.upload_f24_attachment(2)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
