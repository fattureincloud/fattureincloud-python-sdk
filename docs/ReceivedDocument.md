# ReceivedDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the document. | [optional] 
**type** | [**ReceivedDocumentType**](ReceivedDocumentType.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**var_date** | **date** | Date of the document [If not specified, today date is used]. | [optional] 
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
**items_list** | [**List[ReceivedDocumentItemsListItem]**](ReceivedDocumentItemsListItem.md) |  | [optional] 
**payments_list** | [**List[ReceivedDocumentPaymentsListItem]**](ReceivedDocumentPaymentsListItem.md) |  | [optional] 
**attachment_url** | **str** | [Temporary] [Read Only]  Public url of the attached file. Authomatically set if a valid attachment token is passed via POST /received_documents or PUT /received_documents/{documentId}. | [optional] [readonly] 
**attachment_preview_url** | **str** | [Temporary] [Read Only]  Attachment preview url. | [optional] [readonly] 
**auto_calculate** | **bool** | If set to false total items amount and total payments amount can be different. | [optional] 
**attachment_token** | **str** | Uploaded attachement token. | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document import ReceivedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocument from a JSON string
received_document_instance = ReceivedDocument.from_json(json)
# print the JSON string representation of the object
print ReceivedDocument.to_json()

# convert the object into a dict
received_document_dict = received_document_instance.to_dict()
# create an instance of ReceivedDocument from a dict
received_document_form_dict = received_document.from_dict(received_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


