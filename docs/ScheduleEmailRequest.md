# ScheduleEmailRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EmailSchedule**](EmailSchedule.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.schedule_email_request import ScheduleEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEmailRequest from a JSON string
schedule_email_request_instance = ScheduleEmailRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleEmailRequest.to_json())

# convert the object into a dict
schedule_email_request_dict = schedule_email_request_instance.to_dict()
# create an instance of ScheduleEmailRequest from a dict
schedule_email_request_from_dict = ScheduleEmailRequest.from_dict(schedule_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


