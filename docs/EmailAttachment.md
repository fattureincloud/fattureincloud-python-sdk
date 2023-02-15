# EmailAttachment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Email attachment filename. | [optional] 
**url** | **str** | Email attachment url. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email_attachment import EmailAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAttachment from a JSON string
email_attachment_instance = EmailAttachment.from_json(json)
# print the JSON string representation of the object
print EmailAttachment.to_json()

# convert the object into a dict
email_attachment_dict = email_attachment_instance.to_dict()
# create an instance of EmailAttachment from a dict
email_attachment_form_dict = email_attachment.from_dict(email_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


