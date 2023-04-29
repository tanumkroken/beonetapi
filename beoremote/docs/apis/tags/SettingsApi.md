<a name="__pageTop"></a>
# beoremote-cli.apis.tags.settings_api.SettingsApi

All URIs are relative to *http://beoproduct.local:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_region_settings**](#get_region_settings) | **get** /BeoDevice/regionalSettings | Product Regional Settings

# **get_region_settings**
<a name="get_region_settings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_region_settings()

Product Regional Settings

The product region profile settings.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import settings_api
from beoremote-cli.model.language import Language
from beoremote-cli.model.country import Country
from beoremote-cli.model.day_light_saving import DayLightSaving
from beoremote-cli.model.date_time import DateTime
from beoremote-cli.model.date_time_mode import DateTimeMode
from beoremote-cli.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Product Regional Settings
        api_response = api_instance.get_region_settings()
        pprint(api_response)
    except beoremote-cli.ApiException as e:
        print("Exception when calling SettingsApi->get_region_settings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_region_settings.ApiResponseFor200) | OK

#### get_region_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[profile](#profile)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**version** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[_links](#_links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[regionalSettings](#regionalSettings)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# _links

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[self](#self)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# self

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# regionalSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dateTime** | [**DateTime**]({{complexTypePrefix}}DateTime.md) | [**DateTime**]({{complexTypePrefix}}DateTime.md) |  | [optional] 
**dateTimeMode** | [**DateTimeMode**]({{complexTypePrefix}}DateTimeMode.md) | [**DateTimeMode**]({{complexTypePrefix}}DateTimeMode.md) |  | [optional] 
**daylightSaving** | [**DayLightSaving**]({{complexTypePrefix}}DayLightSaving.md) | [**DayLightSaving**]({{complexTypePrefix}}DayLightSaving.md) |  | [optional] 
**timeZone** | [**DayLightSaving**]({{complexTypePrefix}}DayLightSaving.md) | [**DayLightSaving**]({{complexTypePrefix}}DayLightSaving.md) |  | [optional] 
**country** | [**Country**]({{complexTypePrefix}}Country.md) | [**Country**]({{complexTypePrefix}}Country.md) |  | [optional] 
**region** | [**Region**]({{complexTypePrefix}}Region.md) | [**Region**]({{complexTypePrefix}}Region.md) |  | [optional] 
**language** | [**Language**]({{complexTypePrefix}}Language.md) | [**Language**]({{complexTypePrefix}}Language.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

