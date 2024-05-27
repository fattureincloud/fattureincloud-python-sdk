# UploadArchiveAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentData**](AttachmentData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.upload_archive_attachment_response import UploadArchiveAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadArchiveAttachmentResponse from a JSON string
upload_archive_attachment_response_instance = UploadArchiveAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(UploadArchiveAttachmentResponse.to_json())

# convert the object into a dict
upload_archive_attachment_response_dict = upload_archive_attachment_response_instance.to_dict()
# create an instance of UploadArchiveAttachmentResponse from a dict
upload_archive_attachment_response_from_dict = UploadArchiveAttachmentResponse.from_dict(upload_archive_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


