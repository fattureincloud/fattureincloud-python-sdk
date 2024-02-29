# ModifyReceiptResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Receipt**](Receipt.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_receipt_response import ModifyReceiptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyReceiptResponse from a JSON string
modify_receipt_response_instance = ModifyReceiptResponse.from_json(json)
# print the JSON string representation of the object
print ModifyReceiptResponse.to_json()

# convert the object into a dict
modify_receipt_response_dict = modify_receipt_response_instance.to_dict()
# create an instance of ModifyReceiptResponse from a dict
modify_receipt_response_form_dict = modify_receipt_response.from_dict(modify_receipt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


