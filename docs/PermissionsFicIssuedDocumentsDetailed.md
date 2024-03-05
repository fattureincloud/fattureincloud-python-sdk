# PermissionsFicIssuedDocumentsDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotes** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**proformas** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**invoices** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**receipts** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**delivery_notes** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**credit_notes** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**orders** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**work_reports** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**supplier_orders** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 
**self_invoices** | [**PermissionLevel**](PermissionLevel.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.permissions_fic_issued_documents_detailed import PermissionsFicIssuedDocumentsDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsFicIssuedDocumentsDetailed from a JSON string
permissions_fic_issued_documents_detailed_instance = PermissionsFicIssuedDocumentsDetailed.from_json(json)
# print the JSON string representation of the object
print PermissionsFicIssuedDocumentsDetailed.to_json()

# convert the object into a dict
permissions_fic_issued_documents_detailed_dict = permissions_fic_issued_documents_detailed_instance.to_dict()
# create an instance of PermissionsFicIssuedDocumentsDetailed from a dict
permissions_fic_issued_documents_detailed_form_dict = permissions_fic_issued_documents_detailed.from_dict(permissions_fic_issued_documents_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


