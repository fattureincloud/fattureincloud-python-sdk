# ListBinReceivedDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReceivedDocument]**](ReceivedDocument.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.list_bin_received_documents import ListBinReceivedDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of ListBinReceivedDocuments from a JSON string
list_bin_received_documents_instance = ListBinReceivedDocuments.from_json(json)
# print the JSON string representation of the object
print(ListBinReceivedDocuments.to_json())

# convert the object into a dict
list_bin_received_documents_dict = list_bin_received_documents_instance.to_dict()
# create an instance of ListBinReceivedDocuments from a dict
list_bin_received_documents_from_dict = ListBinReceivedDocuments.from_dict(list_bin_received_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


