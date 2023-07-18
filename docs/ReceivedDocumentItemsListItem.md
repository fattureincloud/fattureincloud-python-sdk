# ReceivedDocumentItemsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Received document item id | [optional] 
**product_id** | **int** | Received document product id | [optional] 
**code** | **str** | Received document item product code | [optional] 
**name** | **str** | Received document item product name | [optional] 
**measure** | **str** | Received document item measure | [optional] 
**net_price** | **float** | Received document item product net price | [optional] 
**category** | **str** | Received document item product category | [optional] 
**qty** | **float** | Received document item quantity | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 
**stock** | **float** | Received document item product number of items in stock | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.received_document_items_list_item import ReceivedDocumentItemsListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivedDocumentItemsListItem from a JSON string
received_document_items_list_item_instance = ReceivedDocumentItemsListItem.from_json(json)
# print the JSON string representation of the object
print ReceivedDocumentItemsListItem.to_json()

# convert the object into a dict
received_document_items_list_item_dict = received_document_items_list_item_instance.to_dict()
# create an instance of ReceivedDocumentItemsListItem from a dict
received_document_items_list_item_form_dict = received_document_items_list_item.from_dict(received_document_items_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


