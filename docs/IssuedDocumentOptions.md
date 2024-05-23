# IssuedDocumentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fix_payments** | **bool** | Fixes your last payment amount to match your document total | [optional] 
**create_from** | **List[str]** | Original documents ids [only for join/transform] | [optional] 
**transform** | **bool** | Tranform a document [only for transform] | [optional] 
**keep_copy** | **bool** | Keep original document [only for transform] | [optional] 
**join_type** | **str** | Join type [only for join] | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.issued_document_options import IssuedDocumentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedDocumentOptions from a JSON string
issued_document_options_instance = IssuedDocumentOptions.from_json(json)
# print the JSON string representation of the object
print(IssuedDocumentOptions.to_json())

# convert the object into a dict
issued_document_options_dict = issued_document_options_instance.to_dict()
# create an instance of IssuedDocumentOptions from a dict
issued_document_options_from_dict = IssuedDocumentOptions.from_dict(issued_document_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


