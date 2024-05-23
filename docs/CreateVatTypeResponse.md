# CreateVatTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_vat_type_response import CreateVatTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVatTypeResponse from a JSON string
create_vat_type_response_instance = CreateVatTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateVatTypeResponse.to_json())

# convert the object into a dict
create_vat_type_response_dict = create_vat_type_response_instance.to_dict()
# create an instance of CreateVatTypeResponse from a dict
create_vat_type_response_from_dict = CreateVatTypeResponse.from_dict(create_vat_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


