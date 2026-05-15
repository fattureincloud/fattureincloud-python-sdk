# GetPendingReceivedDocumentResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PendingReceivedDocument**](PendingReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_pending_received_document_response import GetPendingReceivedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPendingReceivedDocumentResponse from a JSON string
get_pending_received_document_response_instance = GetPendingReceivedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(GetPendingReceivedDocumentResponse.to_json())

# convert the object into a dict
get_pending_received_document_response_dict = get_pending_received_document_response_instance.to_dict()
# create an instance of GetPendingReceivedDocumentResponse from a dict
get_pending_received_document_response_from_dict = GetPendingReceivedDocumentResponse.from_dict(get_pending_received_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


