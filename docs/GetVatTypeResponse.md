# GetVatTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_vat_type_response import GetVatTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVatTypeResponse from a JSON string
get_vat_type_response_instance = GetVatTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetVatTypeResponse.to_json())

# convert the object into a dict
get_vat_type_response_dict = get_vat_type_response_instance.to_dict()
# create an instance of GetVatTypeResponse from a dict
get_vat_type_response_from_dict = GetVatTypeResponse.from_dict(get_vat_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


