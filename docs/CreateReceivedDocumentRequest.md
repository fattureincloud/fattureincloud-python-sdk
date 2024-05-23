# CreateReceivedDocumentRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_id** | **int** | Pending received document id of the document from which the new document is created. | [optional] 
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_received_document_request import CreateReceivedDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReceivedDocumentRequest from a JSON string
create_received_document_request_instance = CreateReceivedDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReceivedDocumentRequest.to_json())

# convert the object into a dict
create_received_document_request_dict = create_received_document_request_instance.to_dict()
# create an instance of CreateReceivedDocumentRequest from a dict
create_received_document_request_from_dict = CreateReceivedDocumentRequest.from_dict(create_received_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


