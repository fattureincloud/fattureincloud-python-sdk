# IssuedDocumentItemsListItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Issued document item id | [optional] 
**product_id** | **int** | Issued document item product id | [optional] 
**code** | **str** | Issued document item product code | [optional] 
**name** | **str** | Issued document item product name | [optional] 
**category** | **str** | Issued document item product category | [optional] 
**description** | **str** | Issued document product description | [optional] 
**qty** | **float** | Issued document item quantity | [optional] 
**measure** | **str** | Issued document item measure | [optional] 
**net_price** | **float** | Issued document item net price | [optional] 
**gross_price** | **float** | Issued document item gross price | [optional] 
**vat** | [**VatType**](VatType.md) |  | [optional] 
**not_taxable** | **bool** | Issued document item is not taxable | [optional] 
**apply_withholding_taxes** | **bool** | Issued document item apply withholding taxes, rivalsa and cassa | [optional] 
**discount** | **float** | Issued document item discount percentual value | [optional] 
**discount_highlight** | **bool** | Issued document item highlight discount | [optional] 
**in_dn** | **bool** | Issued document item add in delivery note | [optional] 
**stock** | **bool** | Issued document item move stock | [optional] 
**ei_raw** | **object** | Issued document advanced raw attributes for e-invoices | [optional] 

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


