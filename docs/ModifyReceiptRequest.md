# ModifyReceiptRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Receipt**](Receipt.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.modify_receipt_request import ModifyReceiptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyReceiptRequest from a JSON string
modify_receipt_request_instance = ModifyReceiptRequest.from_json(json)
# print the JSON string representation of the object
print(ModifyReceiptRequest.to_json())

# convert the object into a dict
modify_receipt_request_dict = modify_receipt_request_instance.to_dict()
# create an instance of ModifyReceiptRequest from a dict
modify_receipt_request_from_dict = ModifyReceiptRequest.from_dict(modify_receipt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


