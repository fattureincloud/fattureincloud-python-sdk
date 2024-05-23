# GetReceiptPreCreateInfoResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceiptPreCreateInfo**](ReceiptPreCreateInfo.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_receipt_pre_create_info_response import GetReceiptPreCreateInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceiptPreCreateInfoResponse from a JSON string
get_receipt_pre_create_info_response_instance = GetReceiptPreCreateInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetReceiptPreCreateInfoResponse.to_json())

# convert the object into a dict
get_receipt_pre_create_info_response_dict = get_receipt_pre_create_info_response_instance.to_dict()
# create an instance of GetReceiptPreCreateInfoResponse from a dict
get_receipt_pre_create_info_response_from_dict = GetReceiptPreCreateInfoResponse.from_dict(get_receipt_pre_create_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


