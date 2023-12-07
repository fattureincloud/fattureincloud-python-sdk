"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.22
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import datetime
import unittest
from fattureincloud_python_sdk.models.email import Email
from fattureincloud_python_sdk.models.email_recipient_status import EmailRecipientStatus
from fattureincloud_python_sdk.models.email_status import EmailStatus
from fattureincloud_python_sdk.models.list_emails_response import ListEmailsResponse
import functions
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.emails_api import EmailsApi
from fattureincloud_python_sdk.rest import RESTResponse  # noqa: E501


class TestEmailsApi(unittest.TestCase):
    """EmailsApi unit test stubs"""

    def setUp(self):
        self.api = EmailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_emails(self):
        resp = {
            "status": 200,
            "data": b'{"data": [{"id": 1, "status": "sent", "sent_date": "2022-07-17T13:53:12", "errors_count": 0, "error_log": "", "from_email": "test@mail.it", "from_name": "Test mail", "to_email": "mail@test.it", "to_name": "Mario", "subject": "Test", "content": "Test send email", "copy_to": "", "recipient_status": "unknown", "recipient_date": "2022-07-17T13:53:12", "kind": "Fatture", "attachments": []}, {"id": 2, "status": "sent", "sent_date": "2022-07-17T13:53:12", "errors_count": 0, "error_log": "", "from_email": "test@mail.it", "from_name": "Test mail", "to_email": "mail@test.it", "to_name": "Mario", "subject": "Test", "content": "Test send email", "copy_to": "", "recipient_status": "unknown", "recipient_date": "2022-07-17T13:53:12", "kind": "Fatture", "attachments": []}], "current_page": 10, "first_page_url": "http://url.com", "last_page": 10, "last_page_url": "http://url.com", "next_page_url": "http://url.com", "path": "http://url.com", "per_page": 10, "prev_page_url": "http://url.com", "to": 10, "total": 10}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = ListEmailsResponse(
            data=[
                Email(
                    id=2,
                    status=EmailStatus("sent"),
                    sent_date=datetime.datetime.strptime(
                        "2022-07-17 13:53:12", "%Y-%m-%d %H:%M:%S"
                    ),
                    errors_count=0,
                    error_log="",
                    from_email="test@mail.it",
                    from_name="Test mail",
                    to_email="mail@test.it",
                    to_name="Mario",
                    subject="Test",
                    content="Test send email",
                    copy_to="",
                    recipient_status=EmailRecipientStatus("unknown"),
                    recipient_date=datetime.datetime.strptime(
                        "2022-07-17 13:53:12", "%Y-%m-%d %H:%M:%S"
                    ),
                    kind="Fatture",
                    attachments=[],
                ),
                Email(
                    id=2,
                    status=EmailStatus("sent"),
                    sent_date=datetime.datetime.strptime(
                        "2022-07-17 13:53:12", "%Y-%m-%d %H:%M:%S"
                    ),
                    errors_count=0,
                    error_log="",
                    from_email="test@mail.it",
                    from_name="Test mail",
                    to_email="mail@test.it",
                    to_name="Mario",
                    subject="Test",
                    content="Test send email",
                    copy_to="",
                    recipient_status=EmailRecipientStatus("unknown"),
                    recipient_date=datetime.datetime.strptime(
                        "2022-07-17 13:53:12", "%Y-%m-%d %H:%M:%S"
                    ),
                    kind="Fatture",
                    attachments=[],
                ),
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
        actual = self.api.list_emails(2)
        actual.data[0].id = 2
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
