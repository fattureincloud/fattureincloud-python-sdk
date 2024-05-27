# EmailSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **int** | Email sender id [required if **sender_email** is not specified] | [optional] 
**sender_email** | **str** | Email sender address [required if **sender_id** is not specified] | [optional] 
**recipient_email** | **str** | Email recipient emails [comma separated] | [optional] 
**subject** | **str** | Email subject | [optional] 
**body** | **str** | Email body [HTML Escaped] [max size 50KiB] | [optional] 
**include** | [**EmailScheduleInclude**](EmailScheduleInclude.md) |  | [optional] 
**attach_pdf** | **bool** | Attach the pdf of the document | [optional] 
**send_copy** | **bool** | Send a copy of the email to the **cc_email** specified by **Get email data** | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email_schedule import EmailSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSchedule from a JSON string
email_schedule_instance = EmailSchedule.from_json(json)
# print the JSON string representation of the object
print(EmailSchedule.to_json())

# convert the object into a dict
email_schedule_dict = email_schedule_instance.to_dict()
# create an instance of EmailSchedule from a dict
email_schedule_from_dict = EmailSchedule.from_dict(email_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


