# CreateIssuedDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_issued_document_response import CreateIssuedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssuedDocumentResponse from a JSON string
create_issued_document_response_instance = CreateIssuedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateIssuedDocumentResponse.to_json())

# convert the object into a dict
create_issued_document_response_dict = create_issued_document_response_instance.to_dict()
# create an instance of CreateIssuedDocumentResponse from a dict
create_issued_document_response_from_dict = CreateIssuedDocumentResponse.from_dict(create_issued_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


