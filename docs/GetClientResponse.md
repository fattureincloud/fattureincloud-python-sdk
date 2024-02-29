# GetClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Client**](Client.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_client_response import GetClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientResponse from a JSON string
get_client_response_instance = GetClientResponse.from_json(json)
# print the JSON string representation of the object
print GetClientResponse.to_json()

# convert the object into a dict
get_client_response_dict = get_client_response_instance.to_dict()
# create an instance of GetClientResponse from a dict
get_client_response_form_dict = get_client_response.from_dict(get_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


