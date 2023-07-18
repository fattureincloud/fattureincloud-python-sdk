# City


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** | City postal code | [optional] 
**city** | **str** | City name | [optional] 
**province** | **str** | City province | [optional] 

## Example

```python
from fattureincloud_python_sdk.models.city import City

# TODO update the JSON string below
json = "{}"
# create an instance of City from a JSON string
city_instance = City.from_json(json)
# print the JSON string representation of the object
print City.to_json()

# convert the object into a dict
city_dict = city_instance.to_dict()
# create an instance of City from a dict
city_form_dict = city.from_dict(city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


