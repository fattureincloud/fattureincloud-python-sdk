# ModifyVatTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_vat_type_response import ModifyVatTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyVatTypeResponse from a JSON string
modify_vat_type_response_instance = ModifyVatTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyVatTypeResponse.to_json())

# convert the object into a dict
modify_vat_type_response_dict = modify_vat_type_response_instance.to_dict()
# create an instance of ModifyVatTypeResponse from a dict
modify_vat_type_response_from_dict = ModifyVatTypeResponse.from_dict(modify_vat_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


