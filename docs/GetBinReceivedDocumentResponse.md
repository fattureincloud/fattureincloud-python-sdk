# GetBinReceivedDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_bin_received_document_response import GetBinReceivedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinReceivedDocumentResponse from a JSON string
get_bin_received_document_response_instance = GetBinReceivedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(GetBinReceivedDocumentResponse.to_json())

# convert the object into a dict
get_bin_received_document_response_dict = get_bin_received_document_response_instance.to_dict()
# create an instance of GetBinReceivedDocumentResponse from a dict
get_bin_received_document_response_from_dict = GetBinReceivedDocumentResponse.from_dict(get_bin_received_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


