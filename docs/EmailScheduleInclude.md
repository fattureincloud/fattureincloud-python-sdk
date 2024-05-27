# EmailScheduleInclude


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **bool** | Include a button to view the document | [optional] 
**delivery_note** | **bool** | Include a button to view the delivery note | [optional] 
**attachment** | **bool** | Include a button to view the attachment | [optional] 
**accompanying_invoice** | **bool** | Include a button to view the accompanying invoice | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.email_schedule_include import EmailScheduleInclude

# TODO update the JSON string below
json = "{}"
# create an instance of EmailScheduleInclude from a JSON string
email_schedule_include_instance = EmailScheduleInclude.from_json(json)
# print the JSON string representation of the object
print(EmailScheduleInclude.to_json())

# convert the object into a dict
email_schedule_include_dict = email_schedule_include_instance.to_dict()
# create an instance of EmailScheduleInclude from a dict
email_schedule_include_from_dict = EmailScheduleInclude.from_dict(email_schedule_include_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


