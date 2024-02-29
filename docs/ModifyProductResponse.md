# ModifyProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Product**](Product.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_product_response import ModifyProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyProductResponse from a JSON string
modify_product_response_instance = ModifyProductResponse.from_json(json)
# print the JSON string representation of the object
print ModifyProductResponse.to_json()

# convert the object into a dict
modify_product_response_dict = modify_product_response_instance.to_dict()
# create an instance of ModifyProductResponse from a dict
modify_product_response_form_dict = modify_product_response.from_dict(modify_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


