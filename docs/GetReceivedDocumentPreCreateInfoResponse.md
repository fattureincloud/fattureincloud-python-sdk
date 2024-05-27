# GetReceivedDocumentPreCreateInfoResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocumentInfo**](ReceivedDocumentInfo.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_received_document_pre_create_info_response import GetReceivedDocumentPreCreateInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceivedDocumentPreCreateInfoResponse from a JSON string
get_received_document_pre_create_info_response_instance = GetReceivedDocumentPreCreateInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetReceivedDocumentPreCreateInfoResponse.to_json())

# convert the object into a dict
get_received_document_pre_create_info_response_dict = get_received_document_pre_create_info_response_instance.to_dict()
# create an instance of GetReceivedDocumentPreCreateInfoResponse from a dict
get_received_document_pre_create_info_response_from_dict = GetReceivedDocumentPreCreateInfoResponse.from_dict(get_received_document_pre_create_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


