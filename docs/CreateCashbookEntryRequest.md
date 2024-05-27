# CreateCashbookEntryRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CashbookEntry**](CashbookEntry.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_cashbook_entry_request import CreateCashbookEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCashbookEntryRequest from a JSON string
create_cashbook_entry_request_instance = CreateCashbookEntryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCashbookEntryRequest.to_json())

# convert the object into a dict
create_cashbook_entry_request_dict = create_cashbook_entry_request_instance.to_dict()
# create an instance of CreateCashbookEntryRequest from a dict
create_cashbook_entry_request_from_dict = CreateCashbookEntryRequest.from_dict(create_cashbook_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


