# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import unittest
import datetime

import fattureincloud_python_sdk
from fattureincloud_python_sdk.models.event_type import EventType
from fattureincloud_python_sdk.models.list_webhooks_subscriptions_response import (
    ListWebhooksSubscriptionsResponse,
)
from fattureincloud_python_sdk.models.webhooks_subscription import WebhooksSubscription  # noqa: E501
from fattureincloud_python_sdk.rest import ApiException
from functions import json_serial


class TestListWebhooksSubscriptionsResponse(unittest.TestCase):
    """ListWebhooksSubscriptionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListWebhooksSubscriptionsResponse(self):
        """Test ListWebhooksSubscriptionsResponse"""
        model = ListWebhooksSubscriptionsResponse(
            data=[
                WebhooksSubscription(
                    id="SUB123",
                    sink="https://endpoint.test",
                    verified=True,
                    types=[EventType.IT_DOT_FATTUREINCLOUD_DOT_CASHBOOK_DOT_CREATE]
                ),
                WebhooksSubscription(
                    id="SUB12345",
                    sink="https://endpoint.test",
                    verified=True,
                    types=[EventType.IT_DOT_FATTUREINCLOUD_DOT_CASHBOOK_DOT_UPDATE]
                )
            ]
        )
        expected_json = '{"data": [{"id": "SUB123", "sink": "https://endpoint.test", "verified": true, "types": ["it.fattureincloud.cashbook.create"]}, {"id": "SUB12345", "sink": "https://endpoint.test", "verified": true, "types": ["it.fattureincloud.cashbook.update"]}]}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == "__main__":
    unittest.main()
