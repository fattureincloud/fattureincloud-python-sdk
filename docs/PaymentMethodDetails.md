# PaymentMethodDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Payment method details title | [optional] 
**description** | **str** | Payment method details description | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.payment_method_details import PaymentMethodDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodDetails from a JSON string
payment_method_details_instance = PaymentMethodDetails.from_json(json)
# print the JSON string representation of the object
print PaymentMethodDetails.to_json()

# convert the object into a dict
payment_method_details_dict = payment_method_details_instance.to_dict()
# create an instance of PaymentMethodDetails from a dict
payment_method_details_form_dict = payment_method_details.from_dict(payment_method_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


