# CreateVatTypeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VatType**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_vat_type_request import CreateVatTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVatTypeRequest from a JSON string
create_vat_type_request_instance = CreateVatTypeRequest.from_json(json)
# print the JSON string representation of the object
print CreateVatTypeRequest.to_json()

# convert the object into a dict
create_vat_type_request_dict = create_vat_type_request_instance.to_dict()
# create an instance of CreateVatTypeRequest from a dict
create_vat_type_request_form_dict = create_vat_type_request.from_dict(create_vat_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


