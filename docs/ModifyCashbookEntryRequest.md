# ModifyCashbookEntryRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CashbookEntry**](CashbookEntry.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_cashbook_entry_request import ModifyCashbookEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyCashbookEntryRequest from a JSON string
modify_cashbook_entry_request_instance = ModifyCashbookEntryRequest.from_json(json)
# print the JSON string representation of the object
print ModifyCashbookEntryRequest.to_json()

# convert the object into a dict
modify_cashbook_entry_request_dict = modify_cashbook_entry_request_instance.to_dict()
# create an instance of ModifyCashbookEntryRequest from a dict
modify_cashbook_entry_request_form_dict = modify_cashbook_entry_request.from_dict(modify_cashbook_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


