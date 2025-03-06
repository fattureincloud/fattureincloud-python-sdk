# GetBinIssuedDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_bin_issued_document_response import GetBinIssuedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinIssuedDocumentResponse from a JSON string
get_bin_issued_document_response_instance = GetBinIssuedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(GetBinIssuedDocumentResponse.to_json())

# convert the object into a dict
get_bin_issued_document_response_dict = get_bin_issued_document_response_instance.to_dict()
# create an instance of GetBinIssuedDocumentResponse from a dict
get_bin_issued_document_response_from_dict = GetBinIssuedDocumentResponse.from_dict(get_bin_issued_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


