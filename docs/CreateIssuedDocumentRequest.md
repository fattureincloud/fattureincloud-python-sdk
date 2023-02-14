# CreateIssuedDocumentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 
**options** | [**IssuedDocumentOptions**](IssuedDocumentOptions.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_issued_document_request import CreateIssuedDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssuedDocumentRequest from a JSON string
create_issued_document_request_instance = CreateIssuedDocumentRequest.from_json(json)
# print the JSON string representation of the object
print CreateIssuedDocumentRequest.to_json()

# convert the object into a dict
create_issued_document_request_dict = create_issued_document_request_instance.to_dict()
# create an instance of CreateIssuedDocumentRequest from a dict
create_issued_document_request_form_dict = create_issued_document_request.from_dict(create_issued_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


