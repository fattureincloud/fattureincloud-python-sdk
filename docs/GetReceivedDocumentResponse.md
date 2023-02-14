# GetReceivedDocumentResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_received_document_response import GetReceivedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivedDocumentResponse from a JSON string
get_received_document_response_instance = GetReceivedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print GetReceivedDocumentResponse.to_json()

# convert the object into a dict
get_received_document_response_dict = get_received_document_response_instance.to_dict()
# create an instance of GetReceivedDocumentResponse from a dict
get_received_document_response_form_dict = get_received_document_response.from_dict(get_received_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


