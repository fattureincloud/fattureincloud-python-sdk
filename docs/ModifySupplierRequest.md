# ModifySupplierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_supplier_request import ModifySupplierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySupplierRequest from a JSON string
modify_supplier_request_instance = ModifySupplierRequest.from_json(json)
# print the JSON string representation of the object
print(ModifySupplierRequest.to_json())

# convert the object into a dict
modify_supplier_request_dict = modify_supplier_request_instance.to_dict()
# create an instance of ModifySupplierRequest from a dict
modify_supplier_request_from_dict = ModifySupplierRequest.from_dict(modify_supplier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


