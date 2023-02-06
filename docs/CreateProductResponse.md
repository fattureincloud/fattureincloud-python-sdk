# CreateProductResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Product**](Product.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_product_response import CreateProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductResponse from a JSON string
create_product_response_instance = CreateProductResponse.from_json(json)
# print the JSON string representation of the object
print CreateProductResponse.to_json()

# convert the object into a dict
create_product_response_dict = create_product_response_instance.to_dict()
# create an instance of CreateProductResponse from a dict
create_product_response_form_dict = create_product_response.from_dict(create_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


