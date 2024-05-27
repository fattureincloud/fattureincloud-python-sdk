# UploadF24AttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentData**](AttachmentData.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.upload_f24_attachment_response import UploadF24AttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadF24AttachmentResponse from a JSON string
upload_f24_attachment_response_instance = UploadF24AttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(UploadF24AttachmentResponse.to_json())

# convert the object into a dict
upload_f24_attachment_response_dict = upload_f24_attachment_response_instance.to_dict()
# create an instance of UploadF24AttachmentResponse from a dict
upload_f24_attachment_response_from_dict = UploadF24AttachmentResponse.from_dict(upload_f24_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


