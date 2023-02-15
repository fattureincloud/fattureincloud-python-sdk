# TransformIssuedDocumentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 
**options** | [**IssuedDocumentOptions**](IssuedDocumentOptions.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.transform_issued_document_response import TransformIssuedDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransformIssuedDocumentResponse from a JSON string
transform_issued_document_response_instance = TransformIssuedDocumentResponse.from_json(json)
# print the JSON string representation of the object
print TransformIssuedDocumentResponse.to_json()

# convert the object into a dict
transform_issued_document_response_dict = transform_issued_document_response_instance.to_dict()
# create an instance of TransformIssuedDocumentResponse from a dict
transform_issued_document_response_form_dict = transform_issued_document_response.from_dict(transform_issued_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


