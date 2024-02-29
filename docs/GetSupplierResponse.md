# GetSupplierResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_supplier_response import GetSupplierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupplierResponse from a JSON string
get_supplier_response_instance = GetSupplierResponse.from_json(json)
# print the JSON string representation of the object
print GetSupplierResponse.to_json()

# convert the object into a dict
get_supplier_response_dict = get_supplier_response_instance.to_dict()
# create an instance of GetSupplierResponse from a dict
get_supplier_response_form_dict = get_supplier_response.from_dict(get_supplier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


