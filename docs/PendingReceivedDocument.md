# PendingReceivedDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Pending received document id | [optional] 
**var_date** | **date** | Pending received document date | [optional] 
**subject** | **str** | Pending received document subject | [optional] 
**filename** | **str** | Pending received document filename | [optional] 
**type** | [**PendingReceivedDocumentType**](PendingReceivedDocumentType.md) |  | [optional] [default to PendingReceivedDocumentType.AGYO]
**attachment_url** | **str** | [Temporary] [Read Only] Pending received document url of the attached file | [optional] [readonly] 
**amount_gross** | **float** | [Read Only] Pending received document total gross amount | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**document_type** | [**ReceivedDocumentType**](ReceivedDocumentType.md) |  | [optional] [default to ReceivedDocumentType.EXPENSE]
**supplier_name** | **str** | Pending received document supplier name | [optional] 
**cost_center** | **str** | Pending received document cost center | [optional] 
**category** | **str** | Pending received document category | [optional] 
**other_attachments** | [**List[Attachment]**](Attachment.md) | Pending received document other attachments | [optional] 
**emssion_date** | **date** | Pending received document emission date | [optional] 
**payments_list** | [**List[PendingReceivedDocumentPaymentsListItem]**](PendingReceivedDocumentPaymentsListItem.md) |  | [optional] 
**amount_net** | **float** | Pending received document total net amount | [optional] 
**amount_vat** | **float** | Pending received document total vat amount | [optional] 
**import_error** | **str** | Pending received document import error | [optional] 
**extracted_data** | [**PendingReceivedDocumentExtractedData**](PendingReceivedDocumentExtractedData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.pending_received_document import PendingReceivedDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PendingReceivedDocument from a JSON string
pending_received_document_instance = PendingReceivedDocument.from_json(json)
# print the JSON string representation of the object
print(PendingReceivedDocument.to_json())

# convert the object into a dict
pending_received_document_dict = pending_received_document_instance.to_dict()
# create an instance of PendingReceivedDocument from a dict
pending_received_document_from_dict = PendingReceivedDocument.from_dict(pending_received_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


