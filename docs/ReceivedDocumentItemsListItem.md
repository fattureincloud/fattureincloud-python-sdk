# ReceivedDocumentItemsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. | [optional] 
**product_id** | **int** | Unique identifier of the product | [optional] 
**code** | **str** | Product code. | [optional] 
**name** | **str** | Product name. | [optional] 
**measure** | **str** | Product measure. | [optional] 
**net_price** | **float** | Product net price. | [optional] 
**category** | **str** | Product category. | [optional] 
**qty** | **float** | Product quantity. | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 
**stock** | **float** | Number of items in stock | [optional] 

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


