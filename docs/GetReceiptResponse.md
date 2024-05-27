# GetReceiptResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Receipt**](Receipt.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_receipt_response import GetReceiptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceiptResponse from a JSON string
get_receipt_response_instance = GetReceiptResponse.from_json(json)
# print the JSON string representation of the object
print(GetReceiptResponse.to_json())

# convert the object into a dict
get_receipt_response_dict = get_receipt_response_instance.to_dict()
# create an instance of GetReceiptResponse from a dict
get_receipt_response_from_dict = GetReceiptResponse.from_dict(get_receipt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


