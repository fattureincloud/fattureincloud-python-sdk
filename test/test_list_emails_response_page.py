"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.22
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import datetime
import json
import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.email import Email
from fattureincloud_python_sdk.models.email_recipient_status import EmailRecipientStatus
from fattureincloud_python_sdk.models.email_status import EmailStatus
from functions import json_serial

globals()["Email"] = Email
from fattureincloud_python_sdk.models.list_emails_response_page import (
    ListEmailsResponsePage,
)


class TestListEmailsResponsePage(unittest.TestCase):
    """ListEmailsResponsePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListEmailsResponsePage(self):
        """Test ListEmailsResponsePage"""
        model = ListEmailsResponsePage(
            data=[
                Email(
                    id=1,
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
            ]
        )
        expected_json = '{"data": [{"id": 1, "status": "sent", "sent_date": "2022-07-17T13:53:12", "errors_count": 0, "error_log": "", "from_email": "test@mail.it", "from_name": "Test mail", "to_email": "mail@test.it", "to_name": "Mario", "subject": "Test", "content": "Test send email", "copy_to": "", "recipient_status": "unknown", "recipient_date": "2022-07-17T13:53:12", "kind": "Fatture", "attachments": []}, {"id": 2, "status": "sent", "sent_date": "2022-07-17T13:53:12", "errors_count": 0, "error_log": "", "from_email": "test@mail.it", "from_name": "Test mail", "to_email": "mail@test.it", "to_name": "Mario", "subject": "Test", "content": "Test send email", "copy_to": "", "recipient_status": "unknown", "recipient_date": "2022-07-17T13:53:12", "kind": "Fatture", "attachments": []}]}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
