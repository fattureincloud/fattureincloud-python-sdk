# GetEmailDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EmailData**](EmailData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_email_data_response import GetEmailDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailDataResponse from a JSON string
get_email_data_response_instance = GetEmailDataResponse.from_json(json)
# print the JSON string representation of the object
print GetEmailDataResponse.to_json()

# convert the object into a dict
get_email_data_response_dict = get_email_data_response_instance.to_dict()
# create an instance of GetEmailDataResponse from a dict
get_email_data_response_form_dict = get_email_data_response.from_dict(get_email_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


