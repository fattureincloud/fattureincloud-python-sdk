"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa=E501

    The version of the OpenAPI document=2.0.8
    Contact=info@fattureincloud.it
    Generated by=https://openapi-generator.tech
"""


import json
import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.issued_document_pre_create_info import IssuedDocumentPreCreateInfo
from fattureincloud_python_sdk.model.issued_document_pre_create_info_default_values import IssuedDocumentPreCreateInfoDefaultValues
from fattureincloud_python_sdk.model.issued_document_pre_create_info_extra_data_default_values import IssuedDocumentPreCreateInfoExtraDataDefaultValues
from fattureincloud_python_sdk.model.issued_document_pre_create_info_items_default_values import IssuedDocumentPreCreateInfoItemsDefaultValues
from fattureincloud_python_sdk.model.vat_type import VatType
globals()['IssuedDocumentPreCreateInfo'] = IssuedDocumentPreCreateInfo
from fattureincloud_python_sdk.model.get_issued_document_pre_create_info_response import GetIssuedDocumentPreCreateInfoResponse


class TestGetIssuedDocumentPreCreateInfoResponse(unittest.TestCase):
    """GetIssuedDocumentPreCreateInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetIssuedDocumentPreCreateInfoResponse(self):
        """Test GetIssuedDocumentPreCreateInfoResponse"""
        model = GetIssuedDocumentPreCreateInfoResponse(
            data=IssuedDocumentPreCreateInfo(
                numerations={},
                dn_numerations={},
                default_values=IssuedDocumentPreCreateInfoDefaultValues(
                    rivalsa=10.0
                ),
                extra_data_default_values=IssuedDocumentPreCreateInfoExtraDataDefaultValues(
                    ts_communication=True,
                    ts_tipo_spesa="string",
                    ts_flag_tipo_spesa=0,
                    ts_pagamento_tracciato=True
                ),
                items_default_values=IssuedDocumentPreCreateInfoItemsDefaultValues(
                    vat=VatType(
                        id=1,
                        value=22.0,
                        description="Non imponibile art. 123",
                        notes="IVA non imponibile ai sensi dell articolo 123, comma 2",
                        e_invoice=True,
                        ei_type="2",
                        ei_description="ei_description_example",
                        is_disabled=True,
                    ),
                ),
                countries_list=[
                    "italy"
                ]
            )
        )
        expected_json = "{'data': {'countries_list': ['italy'],          'default_values': {'rivalsa': 10.0},          'dn_numerations': {},          'extra_data_default_values': {'ts_communication': True,                                        'ts_flag_tipo_spesa': 0,                                        'ts_pagamento_tracciato': True,                                        'ts_tipo_spesa': 'string'},          'items_default_values': {'vat': {'description': 'Non imponibile art. '                                                          '123',                                           'e_invoice': True,                                           'ei_description': 'ei_description_example',                                           'ei_type': '2',                                           'id': 1,                                           'is_disabled': True,                                           'notes': 'IVA non imponibile ai '                                                    'sensi dell articolo 123, '                                                    'comma 2',                                           'value': 22.0}},          'numerations': {}}}"
        actual_json = json.dumps(model, default=str).replace('\\n', '').replace('"', "")
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
