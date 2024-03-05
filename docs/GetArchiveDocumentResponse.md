# GetArchiveDocumentResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArchiveDocument**](ArchiveDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_archive_document_response import GetArchiveDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetArchiveDocumentResponse from a JSON string
get_archive_document_response_instance = GetArchiveDocumentResponse.from_json(json)
# print the JSON string representation of the object
print GetArchiveDocumentResponse.to_json()

# convert the object into a dict
get_archive_document_response_dict = get_archive_document_response_instance.to_dict()
# create an instance of GetArchiveDocumentResponse from a dict
get_archive_document_response_form_dict = get_archive_document_response.from_dict(get_archive_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


