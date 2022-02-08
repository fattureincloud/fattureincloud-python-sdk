# EmailSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **int** | Sender id. Required if &#x60;sender_email&#x60; is not specified | [optional] 
**sender_email** | **str** | Sender email. Required if &#x60;sender_id&#x60; is not specified | [optional] 
**recipient_email** | **str** | One or more comma separated recipient emails | [optional] 
**subject** | **str** | Email subject | [optional] 
**body** | **str** | Email body | [optional] 
**include** | [**EmailScheduleInclude**](EmailScheduleInclude.md) |  | [optional] 
**attach_pdf** | **bool** | If set to true, documents will be sent as PDF attachments too | [optional] 
**send_copy** | **bool** | If set to true, a copy of the email will be sent to the &#x60;cc_email&#x60; specified by &#x60;Get email data&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


