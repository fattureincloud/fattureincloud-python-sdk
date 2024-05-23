# Email


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email id | [optional] 
**status** | [**EmailStatus**](EmailStatus.md) |  | [optional] 
**sent_date** | **datetime** | Email sent date | [optional] 
**errors_count** | **int** | Email errors count | [optional] 
**error_log** | **str** | Email errors log | [optional] 
**from_email** | **str** | Email sender email | [optional] 
**from_name** | **str** | Email sender name | [optional] 
**to_email** | **str** | Email recipient email | [optional] 
**to_name** | **str** | Email receipient name | [optional] 
**subject** | **str** | Email subject | [optional] 
**content** | **str** | Email content | [optional] 
**copy_to** | **str** | Email cc | [optional] 
**recipient_status** | [**EmailRecipientStatus**](EmailRecipientStatus.md) |  | [optional] 
**recipient_date** | **datetime** | Email recipient date | [optional] 
**kind** | **str** | Email kind | [optional] 
**attachments** | [**List[EmailAttachment]**](EmailAttachment.md) | Email attachments | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email import Email

# TODO update the JSON string below
json = "{}"
# create an instance of Email from a JSON string
email_instance = Email.from_json(json)
# print the JSON string representation of the object
print(Email.to_json())

# convert the object into a dict
email_dict = email_instance.to_dict()
# create an instance of Email from a dict
email_from_dict = Email.from_dict(email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


