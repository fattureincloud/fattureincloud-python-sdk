# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Product id | [optional] 
**name** | **str** | Product name | [optional] 
**code** | **str** | Product code | [optional] 
**net_price** | **float** | Product net price | [optional] 
**gross_price** | **float** | Product gross price | [optional] 
**use_gross_price** | **bool** | Product uses gross prices | [optional] 
**default_vat** | [**VatType**](VatType.md) |  | [optional] 
**net_cost** | **float** | Product net cost | [optional] 
**measure** | **str** | Product measure | [optional] 
**description** | **str** | Product description | [optional] 
**category** | **str** | Product category | [optional] 
**notes** | **str** | Product extra notes | [optional] 
**in_stock** | **bool** | Product has stock | [optional] 
**stock_initial** | **float** | Product initial stock | [optional] 
**stock_current** | **float** | [Read Only] Product current stock | [optional] [readonly] 
**average_cost** | **float** | Product average cost | [optional] 
**average_price** | **float** | Product average price | [optional] 
**created_at** | **str** | Product creation date | [optional] 
**updated_at** | **str** | Product last update date | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


