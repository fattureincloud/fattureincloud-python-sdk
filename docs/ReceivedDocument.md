# ReceivedDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Received document id | [optional] 
**type** | [**ReceivedDocumentType**](ReceivedDocumentType.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**var_date** | **date** | Received document date [defaults to today&#39;s date] | [optional] 
**category** | **str** | Received document category | [optional] 
**description** | **str** | Received document description | [optional] 
**amount_net** | **float** | Received document total net amount | [optional] 
**amount_vat** | **float** | Received document total vat amount | [optional] 
**amount_withholding_tax** | **float** | Received document withholding tax amount | [optional] 
**amount_other_withholding_tax** | **float** | Received document other withholding tax amount | [optional] 
**amount_gross** | **float** | [Read Only] Received document total gross amount | [optional] [readonly] 
**amortization** | **float** | Received document amortization value | [optional] 
**rc_center** | **str** | Received document revenue center | [optional] 
**invoice_number** | **str** | Received document invoice number | [optional] 
**is_marked** | **bool** | Received document is marked | [optional] 
**is_detailed** | **bool** | Received document has items | [optional] 
**e_invoice** | **bool** | [Read Only] Received document is an e-invoice | [optional] 
**next_due_date** | **date** | [Read Only] Received document date of the next not paid payment | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**tax_deductibility** | **float** | Received document tax deducibility percentage | [optional] 
**vat_deductibility** | **float** | Received document vat deducibility percentage | [optional] 
**items_list** | [**List[ReceivedDocumentItemsListItem]**](ReceivedDocumentItemsListItem.md) |  | [optional] 
**payments_list** | [**List[ReceivedDocumentPaymentsListItem]**](ReceivedDocumentPaymentsListItem.md) |  | [optional] 
**attachment_url** | **str** | [Temporary] [Read Only] Received document url of the attached file | [optional] [readonly] 
**attachment_preview_url** | **str** | [Temporary] [Read Only] Received document url of the attachment preview | [optional] [readonly] 
**auto_calculate** | **bool** | Received document total items amount and total payments amount can differ if this field is set to false | [optional] 
**attachment_token** | **str** | [Write Only] Received document attachment token returned by POST /received_documents/attachment | [optional] 
**locked** | **bool** | Received Document can&#39;t be edited | [optional] 
**created_at** | **str** | Received document creation date | [optional] 
**updated_at** | **str** | Received document last update date | [optional] 

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


