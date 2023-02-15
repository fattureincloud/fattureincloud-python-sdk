# ModifyIssuedDocumentRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**IssuedDocument**](IssuedDocument.md) |  | [optional] 
**options** | [**IssuedDocumentOptions**](IssuedDocumentOptions.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_issued_document_request import ModifyIssuedDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyIssuedDocumentRequest from a JSON string
modify_issued_document_request_instance = ModifyIssuedDocumentRequest.from_json(json)
# print the JSON string representation of the object
print ModifyIssuedDocumentRequest.to_json()

# convert the object into a dict
modify_issued_document_request_dict = modify_issued_document_request_instance.to_dict()
# create an instance of ModifyIssuedDocumentRequest from a dict
modify_issued_document_request_form_dict = modify_issued_document_request.from_dict(modify_issued_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


