# GetEntityClientPreCreateInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EntityClientPreCreateInfo**](EntityClientPreCreateInfo.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_entity_client_pre_create_info_response import GetEntityClientPreCreateInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityClientPreCreateInfoResponse from a JSON string
get_entity_client_pre_create_info_response_instance = GetEntityClientPreCreateInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityClientPreCreateInfoResponse.to_json())

# convert the object into a dict
get_entity_client_pre_create_info_response_dict = get_entity_client_pre_create_info_response_instance.to_dict()
# create an instance of GetEntityClientPreCreateInfoResponse from a dict
get_entity_client_pre_create_info_response_from_dict = GetEntityClientPreCreateInfoResponse.from_dict(get_entity_client_pre_create_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


