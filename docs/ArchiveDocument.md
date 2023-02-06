# ArchiveDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Archive document unique identifier. | [optional] 
**var_date** | **date** | Archive document date. | [optional] 
**description** | **str** | Archive Document description. | [optional] 
**attachment_url** | **str** | [Temporary] [Read Only] Absolute url of the attached file. Authomatically set if a valid attachment token is passed via POST /archive or PUT /archive/{documentId}. | [optional] [readonly] 
**category** | **str** | Archive document category. | [optional] 
**attachment_token** | **str** | [Write Only]  [Required] Attachment token returned by POST /archive/attachment. Used to attach the file already uploaded. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.archive_document import ArchiveDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveDocument from a JSON string
archive_document_instance = ArchiveDocument.from_json(json)
# print the JSON string representation of the object
print ArchiveDocument.to_json()

# convert the object into a dict
archive_document_dict = archive_document_instance.to_dict()
# create an instance of ArchiveDocument from a dict
archive_document_form_dict = archive_document.from_dict(archive_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


