# CreateReceivedDocumentResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_received_document_response import CreateReceivedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReceivedDocumentResponse from a JSON string
create_received_document_response_instance = CreateReceivedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print CreateReceivedDocumentResponse.to_json()

# convert the object into a dict
create_received_document_response_dict = create_received_document_response_instance.to_dict()
# create an instance of CreateReceivedDocumentResponse from a dict
create_received_document_response_form_dict = create_received_document_response.from_dict(create_received_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


