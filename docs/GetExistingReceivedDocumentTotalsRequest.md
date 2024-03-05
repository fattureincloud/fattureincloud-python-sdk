# GetExistingReceivedDocumentTotalsRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReceivedDocument**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_existing_received_document_totals_request import GetExistingReceivedDocumentTotalsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetExistingReceivedDocumentTotalsRequest from a JSON string
get_existing_received_document_totals_request_instance = GetExistingReceivedDocumentTotalsRequest.from_json(json)
# print the JSON string representation of the object
print GetExistingReceivedDocumentTotalsRequest.to_json()

# convert the object into a dict
get_existing_received_document_totals_request_dict = get_existing_received_document_totals_request_instance.to_dict()
# create an instance of GetExistingReceivedDocumentTotalsRequest from a dict
get_existing_received_document_totals_request_form_dict = get_existing_received_document_totals_request.from_dict(get_existing_received_document_totals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


