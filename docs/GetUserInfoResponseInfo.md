# GetUserInfoResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**need_marketing_consents_confirmation** | **bool** |  | [optional] 
**need_password_change** | **bool** |  | [optional] 
**need_terms_of_service_confirmation** | **bool** |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_user_info_response_info import GetUserInfoResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserInfoResponseInfo from a JSON string
get_user_info_response_info_instance = GetUserInfoResponseInfo.from_json(json)
# print the JSON string representation of the object
print GetUserInfoResponseInfo.to_json()

# convert the object into a dict
get_user_info_response_info_dict = get_user_info_response_info_instance.to_dict()
# create an instance of GetUserInfoResponseInfo from a dict
get_user_info_response_info_form_dict = get_user_info_response_info.from_dict(get_user_info_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


