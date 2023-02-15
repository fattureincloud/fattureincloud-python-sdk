# ModifyReceivedDocumentRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_received_document_request import ModifyReceivedDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyReceivedDocumentRequest from a JSON string
modify_received_document_request_instance = ModifyReceivedDocumentRequest.from_json(json)
# print the JSON string representation of the object
print ModifyReceivedDocumentRequest.to_json()

# convert the object into a dict
modify_received_document_request_dict = modify_received_document_request_instance.to_dict()
# create an instance of ModifyReceivedDocumentRequest from a dict
modify_received_document_request_form_dict = modify_received_document_request.from_dict(modify_received_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


