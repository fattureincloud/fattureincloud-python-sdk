# ModifyCashbookEntryResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CashbookEntry**](CashbookEntry.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_cashbook_entry_response import ModifyCashbookEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyCashbookEntryResponse from a JSON string
modify_cashbook_entry_response_instance = ModifyCashbookEntryResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyCashbookEntryResponse.to_json())

# convert the object into a dict
modify_cashbook_entry_response_dict = modify_cashbook_entry_response_instance.to_dict()
# create an instance of ModifyCashbookEntryResponse from a dict
modify_cashbook_entry_response_from_dict = ModifyCashbookEntryResponse.from_dict(modify_cashbook_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


