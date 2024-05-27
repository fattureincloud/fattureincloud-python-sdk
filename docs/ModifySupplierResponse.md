# ModifySupplierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_supplier_response import ModifySupplierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySupplierResponse from a JSON string
modify_supplier_response_instance = ModifySupplierResponse.from_json(json)
# print the JSON string representation of the object
print(ModifySupplierResponse.to_json())

# convert the object into a dict
modify_supplier_response_dict = modify_supplier_response_instance.to_dict()
# create an instance of ModifySupplierResponse from a dict
modify_supplier_response_from_dict = ModifySupplierResponse.from_dict(modify_supplier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


