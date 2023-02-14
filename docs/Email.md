# Email



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email unique identifier. | [optional] 
**status** | [**EmailStatus**](EmailStatus.md) |  | [optional] 
**sent_date** | **datetime** | Email sent date. | [optional] 
**errors_count** | **int** | Errors count. | [optional] 
**error_log** | **str** | Error log. | [optional] 
**from_email** | **str** | Sender email. | [optional] 
**from_name** | **str** | Sender name. | [optional] 
**to_email** | **str** | Recipient email. | [optional] 
**to_name** | **str** | Receipient email. | [optional] 
**subject** | **str** | Email subject. | [optional] 
**content** | **str** | Email content. | [optional] 
**copy_to** | **str** |  | [optional] 
**recipient_status** | [**EmailRecipientStatus**](EmailRecipientStatus.md) |  | [optional] 
**recipient_date** | **datetime** |  | [optional] 
**kind** | **str** | Email kind. | [optional] 
**attachments** | [**List[EmailAttachment]**](EmailAttachment.md) | Email attachments. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print Email.to_json()

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_form_dict = email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


