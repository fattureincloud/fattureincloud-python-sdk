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
**attachments** | [**[EmailAttachment]**](EmailAttachment.md) | Email attachments. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


