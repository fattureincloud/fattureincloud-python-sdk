# MonthlyTotal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net** | **float** | Monthly total net amount | [optional] 
**gross** | **float** | Monthly total gross amount | [optional] 
**count** | **float** | Monthly total receipt number | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.monthly_total import MonthlyTotal

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyTotal from a JSON string
monthly_total_instance = MonthlyTotal.from_json(json)
# print the JSON string representation of the object
print MonthlyTotal.to_json()

# convert the object into a dict
monthly_total_dict = monthly_total_instance.to_dict()
# create an instance of MonthlyTotal from a dict
monthly_total_form_dict = monthly_total.from_dict(monthly_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


