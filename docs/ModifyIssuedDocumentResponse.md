# ModifyIssuedDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_issued_document_response import ModifyIssuedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyIssuedDocumentResponse from a JSON string
modify_issued_document_response_instance = ModifyIssuedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyIssuedDocumentResponse.to_json())

# convert the object into a dict
modify_issued_document_response_dict = modify_issued_document_response_instance.to_dict()
# create an instance of ModifyIssuedDocumentResponse from a dict
modify_issued_document_response_from_dict = ModifyIssuedDocumentResponse.from_dict(modify_issued_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


