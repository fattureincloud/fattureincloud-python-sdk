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
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.models.email_schedule_include import EmailScheduleInclude

globals()["EmailScheduleInclude"] = EmailScheduleInclude
from fattureincloud_python_sdk.models.email_schedule import EmailSchedule


class TestEmailSchedule(unittest.TestCase):
    """EmailSchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmailSchedule(self):
        """Test EmailSchedule"""
        model = EmailSchedule(
            sender_id=1,
            sender_email="info@mail.com",
            recipient_email="recipient@mail.com",
            subject="important",
            body="you won a chest of apples",
            include=EmailScheduleInclude(
                document=True,
                delivery_note=False,
                attachment=True,
                accompanying_invoice=False,
            ),
            attach_pdf=False,
            send_copy=True,
        )
        expected_json = '{"sender_id": 1, "sender_email": "info@mail.com", "recipient_email": "recipient@mail.com", "subject": "important", "body": "you won a chest of apples", "include": {"document": true, "delivery_note": false, "attachment": true, "accompanying_invoice": false}, "attach_pdf": false, "send_copy": true}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
