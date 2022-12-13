# ReceivedDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Unique identifier of the document. | [optional] 
**type** | [**ReceivedDocumentType**](ReceivedDocumentType.md) |  | [optional] 
**entity** | [**ReceivedDocumentEntity**](ReceivedDocumentEntity.md) |  | [optional] 
**date** | **date, none_type** | Date of the document [If not specified, today date is used]. | [optional] 
**category** | **str, none_type** | Document category. | [optional] 
**description** | **str, none_type** | Document description. | [optional] 
**amount_net** | **float, none_type** | Total net amount. | [optional] 
**amount_vat** | **float, none_type** | Total vat amount. | [optional] 
**amount_withholding_tax** | **float, none_type** | Withholding tax amount. | [optional] 
**amount_other_withholding_tax** | **float, none_type** | Other withholding tax amount. | [optional] 
**amount_gross** | **float, none_type** | [Read Only] Total gross amount. | [optional] [readonly] 
**amortization** | **float, none_type** | Amortization value | [optional] 
**rc_center** | **str, none_type** | Revenue center. | [optional] 
**invoice_number** | **str, none_type** | Invoice number | [optional] 
**is_marked** | **bool, none_type** |  | [optional] 
**is_detailed** | **bool, none_type** |  | [optional] 
**e_invoice** | **bool, none_type** | [Read Only] Indicates if this is an e-invoice. | [optional] 
**next_due_date** | **date, none_type** | [Read Only] Next due date. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**tax_deductibility** | **float, none_type** | Tax deducibility percentage. | [optional] 
**vat_deductibility** | **float, none_type** | Vat deducibility percentage. | [optional] 
**items_list** | [**[ReceivedDocumentItemsListItem], none_type**](ReceivedDocumentItemsListItem.md) |  | [optional] 
**payments_list** | [**[ReceivedDocumentPaymentsListItem], none_type**](ReceivedDocumentPaymentsListItem.md) |  | [optional] 
**attachment_url** | **str, none_type** | [Temporary] [Read Only]  Public url of the attached file. Authomatically set if a valid attachment token is passed via POST /received_documents or PUT /received_documents/{documentId}. | [optional] [readonly] 
**attachment_preview_url** | **str, none_type** | [Temporary] [Read Only]  Attachment preview url. | [optional] [readonly] 
**attachment_token** | **str, none_type** | Uploaded attachement token. | [optional] 
**created_at** | **str, none_type** |  | [optional] 
**updated_at** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


