"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.8
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import dateutil
import fattureincloud_python_sdk
from fattureincloud_python_sdk.api.issued_documents_api import IssuedDocumentsApi
from fattureincloud_python_sdk.model.attachment_data import AttachmentData
from fattureincloud_python_sdk.model.create_issued_document_response import CreateIssuedDocumentResponse
from fattureincloud_python_sdk.model.get_issued_document_response import GetIssuedDocumentResponse
from fattureincloud_python_sdk.model.issued_document import IssuedDocument
from fattureincloud_python_sdk.model.issued_document_totals import IssuedDocumentTotals
from fattureincloud_python_sdk.model.issued_document_type import IssuedDocumentType
from fattureincloud_python_sdk.model.list_issued_documents_response import ListIssuedDocumentsResponse
from fattureincloud_python_sdk.model.modify_issued_document_response import ModifyIssuedDocumentResponse
from fattureincloud_python_sdk.model.upload_issued_document_attachment_response import UploadIssuedDocumentAttachmentResponse
from fattureincloud_python_sdk.model.email_data import EmailData
from fattureincloud_python_sdk.model.email_data_default_sender_email import EmailDataDefaultSenderEmail
from fattureincloud_python_sdk.model.email_data_sender_emails_list import EmailDataSenderEmailsList
from fattureincloud_python_sdk.model.get_email_data_response import GetEmailDataResponse
from fattureincloud_python_sdk.model.get_existing_issued_document_totals_response import GetExistingIssuedDocumentTotalsResponse
from fattureincloud_python_sdk.model.get_issued_document_pre_create_info_response import GetIssuedDocumentPreCreateInfoResponse
from fattureincloud_python_sdk.model.get_new_issued_document_totals_response import GetNewIssuedDocumentTotalsResponse
from fattureincloud_python_sdk.model.issued_document_pre_create_info import IssuedDocumentPreCreateInfo
from fattureincloud_python_sdk.model.issued_document_pre_create_info_default_values import IssuedDocumentPreCreateInfoDefaultValues
from fattureincloud_python_sdk.model.issued_document_pre_create_info_extra_data_default_values import IssuedDocumentPreCreateInfoExtraDataDefaultValues
from fattureincloud_python_sdk.model.issued_document_pre_create_info_items_default_values import IssuedDocumentPreCreateInfoItemsDefaultValues
from fattureincloud_python_sdk.model.vat_type import VatType


class TestIssuedDocumentsApi(unittest.TestCase):
    """IssuedDocumentsApi unit test stubs"""

    def setUp(self):
        self.api = IssuedDocumentsApi()
        
        issued_document = IssuedDocument( id=1, type=IssuedDocumentType("invoice"), number=1, numeration="/A", date=dateutil.parser.parse('2022.01.01').date(), year=1, subject="subject_example", visible_subject="visible_subject_example", rc_center="rc_center_example", notes="notes_example", rivalsa=0.0, cassa=0.0, cassa_taxable=0.0, amount_cassa_taxable=3.14, cassa2=0.0, cassa2_taxable=0.0, amount_cassa2_taxable=3.14, global_cassa_taxable=0.0, amount_global_cassa_taxable=3.14 )
        totals = IssuedDocumentTotals( amount_net=10.0, amount_rivalsa=0.0, amount_net_with_rivalsa=10.0, amount_cassa=3.14, taxable_amount=0.0, amount_vat=22.0, amount_gross=12.2, amount_due=12.2, payments_sum=12.2 )
        pre_create_info = IssuedDocumentPreCreateInfo( numerations={}, dn_numerations={}, default_values=IssuedDocumentPreCreateInfoDefaultValues( rivalsa=10.0 ), extra_data_default_values=IssuedDocumentPreCreateInfoExtraDataDefaultValues( ts_communication=True, ts_tipo_spesa="string", ts_flag_tipo_spesa=0, ts_pagamento_tracciato=True ), items_default_values=IssuedDocumentPreCreateInfoItemsDefaultValues( vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), ), countries_list=[ "italy" ] )

        self.api.create_issued_document = unittest.mock.MagicMock(return_value = CreateIssuedDocumentResponse(data = issued_document))
        self.api.delete_issued_document = unittest.mock.MagicMock(return_value = "")
        self.api.get_issued_document = unittest.mock.MagicMock(return_value = GetIssuedDocumentResponse(data = issued_document))
        self.api.list_issued_documents = unittest.mock.MagicMock(return_value = ListIssuedDocumentsResponse(data = [issued_document, issued_document]))
        self.api.modify_issued_document = unittest.mock.MagicMock(return_value = ModifyIssuedDocumentResponse(data = issued_document))
        self.api.upload_issued_document_attachment = unittest.mock.MagicMock(return_value = UploadIssuedDocumentAttachmentResponse(data = AttachmentData(attachment_token = "aisdfvbgablsiw486r8o3qw36")))
        self.api.delete_issued_document_attachment = unittest.mock.MagicMock(return_value = "")
        self.api.get_existing_issued_document_totals = unittest.mock.MagicMock(return_value = GetExistingIssuedDocumentTotalsResponse(data = totals))
        self.api.get_new_issued_document_totals = unittest.mock.MagicMock(return_value = GetNewIssuedDocumentTotalsResponse(data = totals))
        self.api.get_email_data = unittest.mock.MagicMock(return_value = GetEmailDataResponse(data = EmailData( recipient_email="info@mail.com", cc_email="default@mail.com", subject="important", body="you won 13 billion indian rupies", document_exists=False, delivery_note_exists=False, attachment_exists=False, accompanying_invoice_exists=False, default_attach_pdf=False, default_sender_email=EmailDataDefaultSenderEmail( id=1, email="ex.email@provider.co" ), sender_emails_list=[ EmailDataSenderEmailsList( id=1, email="ex.email@provider.co" ) ] )))
        self.api.schedule_email = unittest.mock.MagicMock(return_value = "")
        self.api.get_issued_document_pre_create_info = unittest.mock.MagicMock(return_value = GetIssuedDocumentPreCreateInfoResponse(data = pre_create_info))

    def tearDown(self):
        pass

    def test_create_issued_document(self):
        expected = CreateIssuedDocumentResponse(data = IssuedDocument( id=2, type=IssuedDocumentType("invoice"), number=1, numeration="/A", date=dateutil.parser.parse('2022.01.01').date(), year=1, subject="subject_example", visible_subject="visible_subject_example", rc_center="rc_center_example", notes="notes_example", rivalsa=0.0, cassa=0.0, cassa_taxable=0.0, amount_cassa_taxable=3.14, cassa2=0.0, cassa2_taxable=0.0, amount_cassa2_taxable=3.14, global_cassa_taxable=0.0, amount_global_cassa_taxable=3.14 )  )
        actual = self.api.create_issued_document(2, None)
        actual.data.id = 2
        assert actual == expected
        self.api.create_issued_document.assert_called_with(2, None)

    def test_delete_issued_document(self):
        self.api.delete_issued_document(12345)
        self.api.delete_issued_document.assert_called_with(12345)

    def test_delete_issued_document_attachment(self):
        self.api.delete_issued_document_attachment(12345)
        self.api.delete_issued_document_attachment.assert_called_with(12345)

    def test_get_email_data(self):
        expected = GetEmailDataResponse(data = EmailData( recipient_email="info2@mail.com", cc_email="default@mail.com", subject="important", body="you won 13 billion indian rupies", document_exists=False, delivery_note_exists=False, attachment_exists=False, accompanying_invoice_exists=False, default_attach_pdf=False, default_sender_email=EmailDataDefaultSenderEmail( id=1, email="ex.email@provider.co" ), sender_emails_list=[ EmailDataSenderEmailsList( id=1, email="ex.email@provider.co" ) ] ))
        actual = self.api.get_email_data(2, None)
        actual.data.recipient_email = "info2@mail.com"
        assert actual == expected
        self.api.get_email_data.assert_called_with(2, None)

    def test_get_existing_issued_document_totals(self):
        expected = GetExistingIssuedDocumentTotalsResponse(data = IssuedDocumentTotals( amount_net=20.0, amount_rivalsa=0.0, amount_net_with_rivalsa=10.0, amount_cassa=3.14, taxable_amount=0.0, amount_vat=22.0, amount_gross=12.2, amount_due=12.2, payments_sum=12.2 )  )
        actual = self.api.get_existing_issued_document_totals(2, 12345, None)
        actual.data.amount_net = 20.0
        assert actual == expected
        self.api.get_existing_issued_document_totals.assert_called_with(2, 12345, None)

    def test_get_issued_document(self):
        expected = GetIssuedDocumentResponse(data = IssuedDocument( id=2, type=IssuedDocumentType("invoice"), number=1, numeration="/A", date=dateutil.parser.parse('2022.01.01').date(), year=1, subject="subject_example", visible_subject="visible_subject_example", rc_center="rc_center_example", notes="notes_example", rivalsa=0.0, cassa=0.0, cassa_taxable=0.0, amount_cassa_taxable=3.14, cassa2=0.0, cassa2_taxable=0.0, amount_cassa2_taxable=3.14, global_cassa_taxable=0.0, amount_global_cassa_taxable=3.14 )  )
        actual = self.api.get_issued_document(2, 12345)
        actual.data.id = 2
        assert actual == expected
        self.api.get_issued_document.assert_called_with(2, 12345)

    def test_get_issued_document_pre_create_info(self):
        expected = GetIssuedDocumentPreCreateInfoResponse(data = IssuedDocumentPreCreateInfo( numerations={}, dn_numerations={}, default_values=IssuedDocumentPreCreateInfoDefaultValues( rivalsa=10.0 ), extra_data_default_values=IssuedDocumentPreCreateInfoExtraDataDefaultValues( ts_communication=True, ts_tipo_spesa="string", ts_flag_tipo_spesa=0, ts_pagamento_tracciato=True ), items_default_values=IssuedDocumentPreCreateInfoItemsDefaultValues( vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), ), countries_list=[ "italy" ] )  )
        actual = self.api.get_issued_document_pre_create_info(2)
        assert actual == expected
        self.api.get_issued_document_pre_create_info.assert_called_with(2)

    def test_get_new_issued_document_totals(self):
        expected = GetNewIssuedDocumentTotalsResponse(data = IssuedDocumentTotals( amount_net=20.0, amount_rivalsa=0.0, amount_net_with_rivalsa=10.0, amount_cassa=3.14, taxable_amount=0.0, amount_vat=22.0, amount_gross=12.2, amount_due=12.2, payments_sum=12.2 )  )
        actual = self.api.get_new_issued_document_totals(2, None)
        actual.data.amount_net = 20.0
        assert actual == expected
        self.api.get_new_issued_document_totals.assert_called_with(2, None)

    def test_list_issued_documents(self):
        expected = ListIssuedDocumentsResponse(data = [IssuedDocument( id=2, type=IssuedDocumentType("invoice"), number=1, numeration="/A", date=dateutil.parser.parse('2022.01.01').date(), year=1, subject="subject_example", visible_subject="visible_subject_example", rc_center="rc_center_example", notes="notes_example", rivalsa=0.0, cassa=0.0, cassa_taxable=0.0, amount_cassa_taxable=3.14, cassa2=0.0, cassa2_taxable=0.0, amount_cassa2_taxable=3.14, global_cassa_taxable=0.0, amount_global_cassa_taxable=3.14 ), IssuedDocument( id=2, type=IssuedDocumentType("invoice"), number=1, numeration="/A", date=dateutil.parser.parse('2022.01.01').date(), year=1, subject="subject_example", visible_subject="visible_subject_example", rc_center="rc_center_example", notes="notes_example", rivalsa=0.0, cassa=0.0, cassa_taxable=0.0, amount_cassa_taxable=3.14, cassa2=0.0, cassa2_taxable=0.0, amount_cassa2_taxable=3.14, global_cassa_taxable=0.0, amount_global_cassa_taxable=3.14 )]  )
        actual = self.api.list_issued_documents(2)
        actual.data[0].id = 2
        assert actual == expected
        self.api.list_issued_documents.assert_called_with(2)

    def test_modify_issued_document(self):
        expected = ModifyIssuedDocumentResponse(data = IssuedDocument( id=2, type=IssuedDocumentType("invoice"), number=1, numeration="/A", date=dateutil.parser.parse('2022.01.01').date(), year=1, subject="subject_example", visible_subject="visible_subject_example", rc_center="rc_center_example", notes="notes_example", rivalsa=0.0, cassa=0.0, cassa_taxable=0.0, amount_cassa_taxable=3.14, cassa2=0.0, cassa2_taxable=0.0, amount_cassa2_taxable=3.14, global_cassa_taxable=0.0, amount_global_cassa_taxable=3.14 )  )
        actual = self.api.modify_issued_document(2, 12345, None)
        actual.data.id = 2
        assert actual == expected
        self.api.modify_issued_document.assert_called_with(2, 12345, None)

    def test_schedule_email(self):
        self.api.schedule_email(12345)
        self.api.schedule_email.assert_called_with(12345)

    def test_upload_issued_document_attachment(self):
        expected = UploadIssuedDocumentAttachmentResponse(data = AttachmentData(attachment_token = "aisdfvbgablsi9876r8o3qw36"))
        actual = self.api.upload_issued_document_attachment(2)
        actual.data.attachment_token = "aisdfvbgablsi9876r8o3qw36"
        assert actual == expected
        self.api.upload_issued_document_attachment.assert_called_with(2)


if __name__ == '__main__':
    unittest.main()
