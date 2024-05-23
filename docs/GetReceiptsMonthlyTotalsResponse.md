# GetReceiptsMonthlyTotalsResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MonthlyTotal]**](MonthlyTotal.md) |  | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.get_receipts_monthly_totals_response import GetReceiptsMonthlyTotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReceiptsMonthlyTotalsResponse from a JSON string
get_receipts_monthly_totals_response_instance = GetReceiptsMonthlyTotalsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReceiptsMonthlyTotalsResponse.to_json())

# convert the object into a dict
get_receipts_monthly_totals_response_dict = get_receipts_monthly_totals_response_instance.to_dict()
# create an instance of GetReceiptsMonthlyTotalsResponse from a dict
get_receipts_monthly_totals_response_from_dict = GetReceiptsMonthlyTotalsResponse.from_dict(get_receipts_monthly_totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


