# CreateArchiveDocumentResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArchiveDocument**](ArchiveDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_archive_document_response import CreateArchiveDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateArchiveDocumentResponse from a JSON string
create_archive_document_response_instance = CreateArchiveDocumentResponse.from_json(json)
# print the JSON string representation of the object
print CreateArchiveDocumentResponse.to_json()

# convert the object into a dict
create_archive_document_response_dict = create_archive_document_response_instance.to_dict()
# create an instance of CreateArchiveDocumentResponse from a dict
create_archive_document_response_form_dict = create_archive_document_response.from_dict(create_archive_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


