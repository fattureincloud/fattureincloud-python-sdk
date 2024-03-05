# ModifyF24Request



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**F24**](F24.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_f24_request import ModifyF24Request

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyF24Request from a JSON string
modify_f24_request_instance = ModifyF24Request.from_json(json)
# print the JSON string representation of the object
print ModifyF24Request.to_json()

# convert the object into a dict
modify_f24_request_dict = modify_f24_request_instance.to_dict()
# create an instance of ModifyF24Request from a dict
modify_f24_request_form_dict = modify_f24_request.from_dict(modify_f24_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


