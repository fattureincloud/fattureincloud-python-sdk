# ListProductsResponsePage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Product]**](Product.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_products_response_page import ListProductsResponsePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListProductsResponsePage from a JSON string
list_products_response_page_instance = ListProductsResponsePage.from_json(json)
# print the JSON string representation of the object
print ListProductsResponsePage.to_json()

# convert the object into a dict
list_products_response_page_dict = list_products_response_page_instance.to_dict()
# create an instance of ListProductsResponsePage from a dict
list_products_response_page_form_dict = list_products_response_page.from_dict(list_products_response_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


