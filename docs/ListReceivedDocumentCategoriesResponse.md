# ListReceivedDocumentCategoriesResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_received_document_categories_response import ListReceivedDocumentCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceivedDocumentCategoriesResponse from a JSON string
list_received_document_categories_response_instance = ListReceivedDocumentCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListReceivedDocumentCategoriesResponse.to_json())

# convert the object into a dict
list_received_document_categories_response_dict = list_received_document_categories_response_instance.to_dict()
# create an instance of ListReceivedDocumentCategoriesResponse from a dict
list_received_document_categories_response_from_dict = ListReceivedDocumentCategoriesResponse.from_dict(list_received_document_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


