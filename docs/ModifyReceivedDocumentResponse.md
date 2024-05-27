# ModifyReceivedDocumentResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_received_document_response import ModifyReceivedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyReceivedDocumentResponse from a JSON string
modify_received_document_response_instance = ModifyReceivedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyReceivedDocumentResponse.to_json())

# convert the object into a dict
modify_received_document_response_dict = modify_received_document_response_instance.to_dict()
# create an instance of ModifyReceivedDocumentResponse from a dict
modify_received_document_response_from_dict = ModifyReceivedDocumentResponse.from_dict(modify_received_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


