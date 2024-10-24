# GetTaxProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaxProfile**](TaxProfile.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_tax_profile_response import GetTaxProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxProfileResponse from a JSON string
get_tax_profile_response_instance = GetTaxProfileResponse.from_json(json)
# print the JSON string representation of the object
print(GetTaxProfileResponse.to_json())

# convert the object into a dict
get_tax_profile_response_dict = get_tax_profile_response_instance.to_dict()
# create an instance of GetTaxProfileResponse from a dict
get_tax_profile_response_from_dict = GetTaxProfileResponse.from_dict(get_tax_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


