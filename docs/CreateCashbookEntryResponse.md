# CreateCashbookEntryResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CashbookEntry**](CashbookEntry.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_cashbook_entry_response import CreateCashbookEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCashbookEntryResponse from a JSON string
create_cashbook_entry_response_instance = CreateCashbookEntryResponse.from_json(json)
# print the JSON string representation of the object
print CreateCashbookEntryResponse.to_json()

# convert the object into a dict
create_cashbook_entry_response_dict = create_cashbook_entry_response_instance.to_dict()
# create an instance of CreateCashbookEntryResponse from a dict
create_cashbook_entry_response_form_dict = create_cashbook_entry_response.from_dict(create_cashbook_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


