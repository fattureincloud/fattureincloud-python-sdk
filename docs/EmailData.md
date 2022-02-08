# EmailData



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_email** | **str, none_type** | Recipient&#39;s email | 
**default_sender_email** | [**EmailDataDefaultSenderEmail**](EmailDataDefaultSenderEmail.md) |  | 
**sender_emails_list** | [**[SenderEmail]**](SenderEmail.md) | List of all emails from which the document can be sent | 
**cc_email** | **str** | By default is the logged company email. This is the email address to which a copy will be sent. | 
**subject** | **str** | Email subject | 
**body** | **str** | Email body | 
**document_exists** | **bool** | If the document is not a delivery note, this flag will be set to true | 
**delivery_note_exists** | **bool** | If the document is a delivery note, this flag will be set to true | 
**attachment_exists** | **bool** | If the document has one or more attachments, this flag will be set to true | 
**accompanying_invoice_exists** | **bool** | If an accompanying invoice exists, this flag will be set to true | 
**default_attach_pdf** | **bool** | If a pdf is attached, this flag will be set to true | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


