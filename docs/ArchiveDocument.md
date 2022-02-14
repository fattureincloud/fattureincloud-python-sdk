# ArchiveDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Archive document unique identifier. | [optional] 
**date** | **date, none_type** | Archive document date. | [optional] 
**description** | **str, none_type** | Archive Document description. | [optional] 
**attachment_url** | **str, none_type** | [Read Only] Absolute url of the attached file. Authomatically set if a valid attachment token is passed via POST /archive or PUT /archive/{documentId}. | [optional] [readonly] 
**category** | **str, none_type** | Archive document category. | [optional] 
**attachment_token** | **str, none_type** | [Write Only]  [Required] Attachment token returned by POST /archive/attachment. Used to attach the file already uploaded. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


