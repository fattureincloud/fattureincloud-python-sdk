# ListVatTypesResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VatType]**](VatType.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_vat_types_response import ListVatTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListVatTypesResponse from a JSON string
list_vat_types_response_instance = ListVatTypesResponse.from_json(json)
# print the JSON string representation of the object
print(ListVatTypesResponse.to_json())

# convert the object into a dict
list_vat_types_response_dict = list_vat_types_response_instance.to_dict()
# create an instance of ListVatTypesResponse from a dict
list_vat_types_response_from_dict = ListVatTypesResponse.from_dict(list_vat_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


