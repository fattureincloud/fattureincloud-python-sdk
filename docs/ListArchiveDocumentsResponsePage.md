# ListArchiveDocumentsResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArchiveDocument]**](ArchiveDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_archive_documents_response_page import ListArchiveDocumentsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListArchiveDocumentsResponsePage from a JSON string
list_archive_documents_response_page_instance = ListArchiveDocumentsResponsePage.from_json(json)
# print the JSON string representation of the object
print(ListArchiveDocumentsResponsePage.to_json())

# convert the object into a dict
list_archive_documents_response_page_dict = list_archive_documents_response_page_instance.to_dict()
# create an instance of ListArchiveDocumentsResponsePage from a dict
list_archive_documents_response_page_from_dict = ListArchiveDocumentsResponsePage.from_dict(list_archive_documents_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


