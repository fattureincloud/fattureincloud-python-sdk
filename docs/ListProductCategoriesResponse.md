# ListProductCategoriesResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_product_categories_response import ListProductCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListProductCategoriesResponse from a JSON string
list_product_categories_response_instance = ListProductCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print ListProductCategoriesResponse.to_json()

# convert the object into a dict
list_product_categories_response_dict = list_product_categories_response_instance.to_dict()
# create an instance of ListProductCategoriesResponse from a dict
list_product_categories_response_form_dict = list_product_categories_response.from_dict(list_product_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


