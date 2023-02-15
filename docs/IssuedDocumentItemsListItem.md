# IssuedDocumentItemsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier. | [optional] 
**product_id** | **int** | Unique identifier of the product. | [optional] 
**code** | **str** | Product code. | [optional] 
**name** | **str** | Product name. | [optional] 
**category** | **str** | Product category | [optional] 
**description** | **str** | Product description. | [optional] 
**qty** | **float** | Items quantity, | [optional] 
**measure** | **str** | Item measure. | [optional] 
**net_price** | **float** | Net price. | [optional] 
**gross_price** | **float** | Gross price. | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 
**not_taxable** | **bool** |  | [optional] 
**apply_withholding_taxes** | **bool** | Apply withholding taxes, rivalsa and cassa. | [optional] 
**discount** | **float** | Discount percentual value. | [optional] 
**discount_highlight** | **bool** |  | [optional] 
**in_dn** | **bool** |  | [optional] 
**stock** | **bool** |  | [optional] 
**ei_raw** | **object** | Advanced raw attributes for e-invoices. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_items_list_item import IssuedDocumentItemsListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentItemsListItem from a JSON string
issued_document_items_list_item_instance = IssuedDocumentItemsListItem.from_json(json)
# print the JSON string representation of the object
print IssuedDocumentItemsListItem.to_json()

# convert the object into a dict
issued_document_items_list_item_dict = issued_document_items_list_item_instance.to_dict()
# create an instance of IssuedDocumentItemsListItem from a dict
issued_document_items_list_item_form_dict = issued_document_items_list_item.from_dict(issued_document_items_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


