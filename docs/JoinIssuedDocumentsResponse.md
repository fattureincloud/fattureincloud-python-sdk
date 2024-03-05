# JoinIssuedDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 
**options** | [**IssuedDocumentOptions**](IssuedDocumentOptions.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.join_issued_documents_response import JoinIssuedDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JoinIssuedDocumentsResponse from a JSON string
join_issued_documents_response_instance = JoinIssuedDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print JoinIssuedDocumentsResponse.to_json()

# convert the object into a dict
join_issued_documents_response_dict = join_issued_documents_response_instance.to_dict()
# create an instance of JoinIssuedDocumentsResponse from a dict
join_issued_documents_response_form_dict = join_issued_documents_response.from_dict(join_issued_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


