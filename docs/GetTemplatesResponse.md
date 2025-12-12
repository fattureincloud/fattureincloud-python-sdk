# GetTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentTemplate**](DocumentTemplate.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_templates_response import GetTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplatesResponse from a JSON string
get_templates_response_instance = GetTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetTemplatesResponse.to_json())

# convert the object into a dict
get_templates_response_dict = get_templates_response_instance.to_dict()
# create an instance of GetTemplatesResponse from a dict
get_templates_response_from_dict = GetTemplatesResponse.from_dict(get_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


