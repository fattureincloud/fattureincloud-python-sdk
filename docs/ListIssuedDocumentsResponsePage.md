# ListIssuedDocumentsResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IssuedDocument]**](IssuedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_issued_documents_response_page import ListIssuedDocumentsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListIssuedDocumentsResponsePage from a JSON string
list_issued_documents_response_page_instance = ListIssuedDocumentsResponsePage.from_json(json)
# print the JSON string representation of the object
print(ListIssuedDocumentsResponsePage.to_json())

# convert the object into a dict
list_issued_documents_response_page_dict = list_issued_documents_response_page_instance.to_dict()
# create an instance of ListIssuedDocumentsResponsePage from a dict
list_issued_documents_response_page_from_dict = ListIssuedDocumentsResponsePage.from_dict(list_issued_documents_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


