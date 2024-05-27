# CashbookEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cashbook id | [optional] 
**var_date** | **date** | Cashbook date | [optional] 
**description** | **str** | Cashbook description | [optional] 
**kind** | [**CashbookEntryKind**](CashbookEntryKind.md) |  | [optional] 
**type** | [**CashbookEntryType**](CashbookEntryType.md) |  | [optional] 
**entity_name** | **str** | Cashbook entity name | [optional] 
**document** | [**CashbookEntryDocument**](CashbookEntryDocument.md) |  | [optional] 
**amount_in** | **float** | [Only for cashbook entry in] Cashbook total amount in | [optional] 
**payment_account_in** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 
**amount_out** | **float** | [Only for cashbook entry out] Cashbook total amount out | [optional] 
**payment_account_out** | [**PaymentAccount**](PaymentAccount.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.cashbook_entry import CashbookEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CashbookEntry from a JSON string
cashbook_entry_instance = CashbookEntry.from_json(json)
# print the JSON string representation of the object
print(CashbookEntry.to_json())

# convert the object into a dict
cashbook_entry_dict = cashbook_entry_instance.to_dict()
# create an instance of CashbookEntry from a dict
cashbook_entry_from_dict = CashbookEntry.from_dict(cashbook_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


