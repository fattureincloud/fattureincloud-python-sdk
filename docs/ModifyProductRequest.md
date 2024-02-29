# ModifyProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Product**](Product.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_product_request import ModifyProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyProductRequest from a JSON string
modify_product_request_instance = ModifyProductRequest.from_json(json)
# print the JSON string representation of the object
print ModifyProductRequest.to_json()

# convert the object into a dict
modify_product_request_dict = modify_product_request_instance.to_dict()
# create an instance of ModifyProductRequest from a dict
modify_product_request_form_dict = modify_product_request.from_dict(modify_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


