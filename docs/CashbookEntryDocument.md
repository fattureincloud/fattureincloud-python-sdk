# CashbookEntryDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Cashbook related document id | [optional] 
**type** | **str** | Cashbook related document type | [optional] 
**path** | **str** | Cashbook related document path | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.cashbook_entry_document import CashbookEntryDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CashbookEntryDocument from a JSON string
cashbook_entry_document_instance = CashbookEntryDocument.from_json(json)
# print the JSON string representation of the object
print(CashbookEntryDocument.to_json())

# convert the object into a dict
cashbook_entry_document_dict = cashbook_entry_document_instance.to_dict()
# create an instance of CashbookEntryDocument from a dict
cashbook_entry_document_from_dict = CashbookEntryDocument.from_dict(cashbook_entry_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


