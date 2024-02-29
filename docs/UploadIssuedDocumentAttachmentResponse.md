# UploadIssuedDocumentAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentData**](AttachmentData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.upload_issued_document_attachment_response import UploadIssuedDocumentAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadIssuedDocumentAttachmentResponse from a JSON string
upload_issued_document_attachment_response_instance = UploadIssuedDocumentAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print UploadIssuedDocumentAttachmentResponse.to_json()

# convert the object into a dict
upload_issued_document_attachment_response_dict = upload_issued_document_attachment_response_instance.to_dict()
# create an instance of UploadIssuedDocumentAttachmentResponse from a dict
upload_issued_document_attachment_response_form_dict = upload_issued_document_attachment_response.from_dict(upload_issued_document_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


