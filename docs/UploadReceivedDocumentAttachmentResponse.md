# UploadReceivedDocumentAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentData**](AttachmentData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.upload_received_document_attachment_response import UploadReceivedDocumentAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadReceivedDocumentAttachmentResponse from a JSON string
upload_received_document_attachment_response_instance = UploadReceivedDocumentAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(UploadReceivedDocumentAttachmentResponse.to_json())

# convert the object into a dict
upload_received_document_attachment_response_dict = upload_received_document_attachment_response_instance.to_dict()
# create an instance of UploadReceivedDocumentAttachmentResponse from a dict
upload_received_document_attachment_response_from_dict = UploadReceivedDocumentAttachmentResponse.from_dict(upload_received_document_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


