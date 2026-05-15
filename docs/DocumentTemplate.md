# DocumentTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template id | [optional] 
**privacy** | **str** | Template privacy | [optional] 
**type** | [**TemplateType**](TemplateType.md) |  | [optional] 
**name** | **str** | Template name | [optional] 
**can_disable_watermark** | **bool** | Can disable watermark | [optional] 
**author** | **str** | Template author | [optional] 
**content** | **str** | Template definition content | [optional] 
**supports_custom_taxable** | **bool** | Supports custom taxable | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.document_template import DocumentTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplate from a JSON string
document_template_instance = DocumentTemplate.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplate.to_json())

# convert the object into a dict
document_template_dict = document_template_instance.to_dict()
# create an instance of DocumentTemplate from a dict
document_template_from_dict = DocumentTemplate.from_dict(document_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


