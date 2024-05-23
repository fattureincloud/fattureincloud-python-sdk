# CreateArchiveDocumentRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ArchiveDocument**](ArchiveDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_archive_document_request import CreateArchiveDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateArchiveDocumentRequest from a JSON string
create_archive_document_request_instance = CreateArchiveDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateArchiveDocumentRequest.to_json())

# convert the object into a dict
create_archive_document_request_dict = create_archive_document_request_instance.to_dict()
# create an instance of CreateArchiveDocumentRequest from a dict
create_archive_document_request_from_dict = CreateArchiveDocumentRequest.from_dict(create_archive_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


