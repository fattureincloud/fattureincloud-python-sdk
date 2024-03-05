# DocumentTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template id | [optional] 
**name** | **str** | Template name | [optional] 
**type** | **str** | Template type | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.document_template import DocumentTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplate from a JSON string
document_template_instance = DocumentTemplate.from_json(json)
# print the JSON string representation of the object
print DocumentTemplate.to_json()

# convert the object into a dict
document_template_dict = document_template_instance.to_dict()
# create an instance of DocumentTemplate from a dict
document_template_form_dict = document_template.from_dict(document_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


