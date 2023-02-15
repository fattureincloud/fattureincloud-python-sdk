# ReceiptItemsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Item unique identifier. | [optional] 
**amount_net** | **float** | Item total net amount. | [optional] 
**amount_gross** | **float** | Item total gross amount. | [optional] 
**category** | **str** | Item category. | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.receipt_items_list_item import ReceiptItemsListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptItemsListItem from a JSON string
receipt_items_list_item_instance = ReceiptItemsListItem.from_json(json)
# print the JSON string representation of the object
print ReceiptItemsListItem.to_json()

# convert the object into a dict
receipt_items_list_item_dict = receipt_items_list_item_instance.to_dict()
# create an instance of ReceiptItemsListItem from a dict
receipt_items_list_item_form_dict = receipt_items_list_item.from_dict(receipt_items_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


