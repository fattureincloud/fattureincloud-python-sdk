# EmailDataDefaultSenderEmail

Default sender email. (Other emails can be found in **sender_emails_list**)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Default sender email id | [optional] 
**email** | **str** | Default sender email address | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email_data_default_sender_email import EmailDataDefaultSenderEmail

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDataDefaultSenderEmail from a JSON string
email_data_default_sender_email_instance = EmailDataDefaultSenderEmail.from_json(json)
# print the JSON string representation of the object
print EmailDataDefaultSenderEmail.to_json()

# convert the object into a dict
email_data_default_sender_email_dict = email_data_default_sender_email_instance.to_dict()
# create an instance of EmailDataDefaultSenderEmail from a dict
email_data_default_sender_email_form_dict = email_data_default_sender_email.from_dict(email_data_default_sender_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


