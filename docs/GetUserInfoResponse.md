# GetUserInfoResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**User**](User.md) |  | [optional] 
**info** | [**GetUserInfoResponseInfo**](GetUserInfoResponseInfo.md) |  | [optional] 
**email_confirmation_state** | [**GetUserInfoResponseEmailConfirmationState**](GetUserInfoResponseEmailConfirmationState.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_user_info_response import GetUserInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserInfoResponse from a JSON string
get_user_info_response_instance = GetUserInfoResponse.from_json(json)
# print the JSON string representation of the object
print GetUserInfoResponse.to_json()

# convert the object into a dict
get_user_info_response_dict = get_user_info_response_instance.to_dict()
# create an instance of GetUserInfoResponse from a dict
get_user_info_response_form_dict = get_user_info_response.from_dict(get_user_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


