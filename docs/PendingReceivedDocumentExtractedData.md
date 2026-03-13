# PendingReceivedDocumentExtractedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mining** | [**PendingReceivedDocumentExtractedDataMining**](PendingReceivedDocumentExtractedDataMining.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.pending_received_document_extracted_data import PendingReceivedDocumentExtractedData

# TODO update the JSON string below
json = "{}"
# create an instance of PendingReceivedDocumentExtractedData from a JSON string
pending_received_document_extracted_data_instance = PendingReceivedDocumentExtractedData.from_json(json)
# print the JSON string representation of the object
print(PendingReceivedDocumentExtractedData.to_json())

# convert the object into a dict
pending_received_document_extracted_data_dict = pending_received_document_extracted_data_instance.to_dict()
# create an instance of PendingReceivedDocumentExtractedData from a dict
pending_received_document_extracted_data_from_dict = PendingReceivedDocumentExtractedData.from_dict(pending_received_document_extracted_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


