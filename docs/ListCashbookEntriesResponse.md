# ListCashbookEntriesResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CashbookEntry]**](CashbookEntry.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_cashbook_entries_response import ListCashbookEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCashbookEntriesResponse from a JSON string
list_cashbook_entries_response_instance = ListCashbookEntriesResponse.from_json(json)
# print the JSON string representation of the object
print ListCashbookEntriesResponse.to_json()

# convert the object into a dict
list_cashbook_entries_response_dict = list_cashbook_entries_response_instance.to_dict()
# create an instance of ListCashbookEntriesResponse from a dict
list_cashbook_entries_response_form_dict = list_cashbook_entries_response.from_dict(list_cashbook_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


