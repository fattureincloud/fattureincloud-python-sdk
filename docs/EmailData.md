# EmailData



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_email** | **str, none_type** | Recipient&#39;s email | [optional] 
**default_sender_email** | [**EmailDataDefaultSenderEmail**](EmailDataDefaultSenderEmail.md) |  | [optional] 
**sender_emails_list** | [**[SenderEmail], none_type**](SenderEmail.md) | List of all emails from which the document can be sent | [optional] 
**cc_email** | **str, none_type** | By default is the logged company email. This is the email address to which a copy will be sent. | [optional] 
**subject** | **str, none_type** | Email subject | [optional] 
**body** | **str, none_type** | Email body | [optional] 
**document_exists** | **bool, none_type** | If the document is not a delivery note, this flag will be set to true | [optional] 
**delivery_note_exists** | **bool, none_type** | If the document is a delivery note, this flag will be set to true | [optional] 
**attachment_exists** | **bool, none_type** | If the document has one or more attachments, this flag will be set to true | [optional] 
**accompanying_invoice_exists** | **bool, none_type** | If an accompanying invoice exists, this flag will be set to true | [optional] 
**default_attach_pdf** | **bool, none_type** | If a pdf is attached, this flag will be set to true | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


