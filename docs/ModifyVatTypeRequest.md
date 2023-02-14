# ModifyVatTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_vat_type_request import ModifyVatTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyVatTypeRequest from a JSON string
modify_vat_type_request_instance = ModifyVatTypeRequest.from_json(json)
# print the JSON string representation of the object
print ModifyVatTypeRequest.to_json()

# convert the object into a dict
modify_vat_type_request_dict = modify_vat_type_request_instance.to_dict()
# create an instance of ModifyVatTypeRequest from a dict
modify_vat_type_request_form_dict = modify_vat_type_request.from_dict(modify_vat_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


