# CreateF24Request



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**F24**](F24.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_f24_request import CreateF24Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateF24Request from a JSON string
create_f24_request_instance = CreateF24Request.from_json(json)
# print the JSON string representation of the object
print CreateF24Request.to_json()

# convert the object into a dict
create_f24_request_dict = create_f24_request_instance.to_dict()
# create an instance of CreateF24Request from a dict
create_f24_request_form_dict = create_f24_request.from_dict(create_f24_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


