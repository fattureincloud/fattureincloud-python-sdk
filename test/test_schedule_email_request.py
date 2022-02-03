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
from fattureincloud_python_sdk.model.email_schedule import EmailSchedule
from fattureincloud_python_sdk.model.email_schedule_include import EmailScheduleInclude
globals()['EmailSchedule'] = EmailSchedule
from fattureincloud_python_sdk.model.schedule_email_request import ScheduleEmailRequest


class TestScheduleEmailRequest(unittest.TestCase):
    """ScheduleEmailRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScheduleEmailRequest(self):
        """Test ScheduleEmailRequest"""
        model = ScheduleEmailRequest(
            data=EmailSchedule(
                sender_id=1,
                sender_email="info@mail.com",
                recipient_email="recipient@mail.com",
                subject="important",
                body="you won a chest of apples",
                include=EmailScheduleInclude(
                    document=True,
                    delivery_note=False,
                    attachment=True,
                    accompanying_invoice=False
                ),
                attach_pdf=False,
                send_copy=True
            )
        )
        expected_json = "{'data': {'attach_pdf': False,          'body': 'you won a chest of apples',          'include': {'accompanying_invoice': False,                      'attachment': True,                      'delivery_note': False,                      'document': True},          'recipient_email': 'recipient@mail.com',          'send_copy': True,          'sender_email': 'info@mail.com',          'sender_id': 1,          'subject': 'important'}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json
        

if __name__ == '__main__':
    unittest.main()
