# CreateSupplierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_supplier_request import CreateSupplierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupplierRequest from a JSON string
create_supplier_request_instance = CreateSupplierRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSupplierRequest.to_json())

# convert the object into a dict
create_supplier_request_dict = create_supplier_request_instance.to_dict()
# create an instance of CreateSupplierRequest from a dict
create_supplier_request_from_dict = CreateSupplierRequest.from_dict(create_supplier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


