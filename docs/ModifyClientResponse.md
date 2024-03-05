# ModifyClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Client**](Client.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_client_response import ModifyClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyClientResponse from a JSON string
modify_client_response_instance = ModifyClientResponse.from_json(json)
# print the JSON string representation of the object
print ModifyClientResponse.to_json()

# convert the object into a dict
modify_client_response_dict = modify_client_response_instance.to_dict()
# create an instance of ModifyClientResponse from a dict
modify_client_response_form_dict = modify_client_response.from_dict(modify_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


