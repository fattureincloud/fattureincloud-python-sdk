# ModifyArchiveDocumentResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArchiveDocument**](ArchiveDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_archive_document_response import ModifyArchiveDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyArchiveDocumentResponse from a JSON string
modify_archive_document_response_instance = ModifyArchiveDocumentResponse.from_json(json)
# print the JSON string representation of the object
print ModifyArchiveDocumentResponse.to_json()

# convert the object into a dict
modify_archive_document_response_dict = modify_archive_document_response_instance.to_dict()
# create an instance of ModifyArchiveDocumentResponse from a dict
modify_archive_document_response_form_dict = modify_archive_document_response.from_dict(modify_archive_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


