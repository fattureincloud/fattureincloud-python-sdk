# ListReceivedDocumentsResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReceivedDocument]**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_received_documents_response_page import ListReceivedDocumentsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivedDocumentsResponsePage from a JSON string
list_received_documents_response_page_instance = ListReceivedDocumentsResponsePage.from_json(json)
# print the JSON string representation of the object
print ListReceivedDocumentsResponsePage.to_json()

# convert the object into a dict
list_received_documents_response_page_dict = list_received_documents_response_page_instance.to_dict()
# create an instance of ListReceivedDocumentsResponsePage from a dict
list_received_documents_response_page_form_dict = list_received_documents_response_page.from_dict(list_received_documents_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


