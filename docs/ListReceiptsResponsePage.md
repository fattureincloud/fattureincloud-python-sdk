# ListReceiptsResponsePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Receipt]**](Receipt.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_receipts_response_page import ListReceiptsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListReceiptsResponsePage from a JSON string
list_receipts_response_page_instance = ListReceiptsResponsePage.from_json(json)
# print the JSON string representation of the object
print ListReceiptsResponsePage.to_json()

# convert the object into a dict
list_receipts_response_page_dict = list_receipts_response_page_instance.to_dict()
# create an instance of ListReceiptsResponsePage from a dict
list_receipts_response_page_form_dict = list_receipts_response_page.from_dict(list_receipts_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


