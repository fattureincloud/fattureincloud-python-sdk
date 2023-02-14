# CreateReceiptRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Receipt**](Receipt.md) |  | [optional] 
**autocomplete_number** | **bool** | If true, the number is autocompleted progressively. | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.create_receipt_request import CreateReceiptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReceiptRequest from a JSON string
create_receipt_request_instance = CreateReceiptRequest.from_json(json)
# print the JSON string representation of the object
print CreateReceiptRequest.to_json()

# convert the object into a dict
create_receipt_request_dict = create_receipt_request_instance.to_dict()
# create an instance of CreateReceiptRequest from a dict
create_receipt_request_form_dict = create_receipt_request.from_dict(create_receipt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


