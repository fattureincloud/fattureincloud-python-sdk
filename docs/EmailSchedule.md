# EmailSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **int** | Sender id. Required if &#x60;sender_email&#x60; is not specified | [optional] 
**sender_email** | **str** | Sender email. Required if &#x60;sender_id&#x60; is not specified | [optional] 
**recipient_email** | **str** | One or more comma separated recipient emails | [optional] 
**subject** | **str** | Email subject | [optional] 
**body** | **str** | Email body [HTML Escaped] [max size 50KiB] | [optional] 
**include** | [**EmailScheduleInclude**](EmailScheduleInclude.md) |  | [optional] 
**attach_pdf** | **bool** | If set to true, documents will be sent as PDF attachments too | [optional] 
**send_copy** | **bool** | If set to true, a copy of the email will be sent to the &#x60;cc_email&#x60; specified by &#x60;Get email data&#x60; | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email_schedule import EmailSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSchedule from a JSON string
email_schedule_instance = EmailSchedule.from_json(json)
# print the JSON string representation of the object
print EmailSchedule.to_json()

# convert the object into a dict
email_schedule_dict = email_schedule_instance.to_dict()
# create an instance of EmailSchedule from a dict
email_schedule_form_dict = email_schedule.from_dict(email_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


