# SenderEmail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sender email id | [optional] 
**email** | **str** | Sender email address | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.sender_email import SenderEmail

# TODO update the JSON string below
json = "{}"
# create an instance of SenderEmail from a JSON string
sender_email_instance = SenderEmail.from_json(json)
# print the JSON string representation of the object
print SenderEmail.to_json()

# convert the object into a dict
sender_email_dict = sender_email_instance.to_dict()
# create an instance of SenderEmail from a dict
sender_email_form_dict = sender_email.from_dict(sender_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


