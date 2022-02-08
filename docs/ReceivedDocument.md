# ReceivedDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the document. | [optional] 
**type** | [**ReceivedDocumentType**](ReceivedDocumentType.md) |  | [optional] 
**entity** | [**ReceivedDocumentEntity**](ReceivedDocumentEntity.md) |  | [optional] 
**date** | **date** | Date of the document [If not specified, today date is used]. | [optional] 
**category** | **str** | Document category. | [optional] 
**description** | **str** | Document description. | [optional] 
**amount_net** | **float** | Total net amount. | [optional] 
**amount_vat** | **float** | Total vat amount. | [optional] 
**amount_withholding_tax** | **float** | Withholding tax amount. | [optional] 
**amount_other_withholding_tax** | **float** | Other withholding tax amount. | [optional] 
**amount_gross** | **float** | [Read Only] Total gross amount. | [optional] [readonly] 
**amortization** | **float** | Amortization value | [optional] 
**rc_center** | **str** | Revenue center. | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**is_marked** | **bool** |  | [optional] 
**is_detailed** | **bool** |  | [optional] 
**e_invoice** | **bool** | [Read Only] Indicates if this is an e-invoice. | [optional] 
**next_due_date** | **date** | [Read Only] Next due date. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**tax_deductibility** | **float** | Tax deducibility percentage. | [optional] 
**vat_deductibility** | **float** | Vat deducibility percentage. | [optional] 
**items_list** | [**[ReceivedDocumentItemsListItem]**](ReceivedDocumentItemsListItem.md) |  | [optional] 
**payments_list** | [**[ReceivedDocumentPaymentsListItem]**](ReceivedDocumentPaymentsListItem.md) |  | [optional] 
**attachment_url** | **str** | [Read Only] Attachment url. | [optional] [readonly] 
**attachment_preview_url** | **str** | [Read Only] Attachment preview url. | [optional] [readonly] 
**attachment_token** | **str** | Uploaded attachement token. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


