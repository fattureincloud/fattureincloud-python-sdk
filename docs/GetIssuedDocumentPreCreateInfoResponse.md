# GetIssuedDocumentPreCreateInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocumentPreCreateInfo**](IssuedDocumentPreCreateInfo.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_issued_document_pre_create_info_response import GetIssuedDocumentPreCreateInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssuedDocumentPreCreateInfoResponse from a JSON string
get_issued_document_pre_create_info_response_instance = GetIssuedDocumentPreCreateInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetIssuedDocumentPreCreateInfoResponse.to_json())

# convert the object into a dict
get_issued_document_pre_create_info_response_dict = get_issued_document_pre_create_info_response_instance.to_dict()
# create an instance of GetIssuedDocumentPreCreateInfoResponse from a dict
get_issued_document_pre_create_info_response_from_dict = GetIssuedDocumentPreCreateInfoResponse.from_dict(get_issued_document_pre_create_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


