<a name="__pageTop"></a>
# beoremote-cli.apis.tags.mute_api.MuteApi

All URIs are relative to *http://beoproduct.local:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mute_state**](#get_mute_state) | **get** /BeoZone/Zone/Sound/Volume/Speaker/Muted | Product  Mute
[**put_mute_state**](#put_mute_state) | **put** /BeoZone/Zone/Sound/Volume/Speaker/Muted | Product Mute

# **get_mute_state**
<a name="get_mute_state"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mute_state()

Product  Mute

Poll if the product speakers are muted or not.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import mute_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mute_api.MuteApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Product  Mute
        api_response = api_instance.get_mute_state()
        pprint(api_response)
    except beoremote-cli.ApiException as e:
        print("Exception when calling MuteApi->get_mute_state: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_mute_state.ApiResponseFor200) | OK

#### get_mute_state.ApiResponseFor200
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
**muted** | bool,  | BoolClass,  |  | [optional] 
**[_capabilities](#_capabilities)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[_links](#_links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# _capabilities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[editable](#editable)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# editable

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# _links

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[/relation/modify](#/relation/modify)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# /relation/modify

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**href** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_mute_state**
<a name="put_mute_state"></a>
> put_mute_state()

Product Mute

Toggle the product mute state on/off.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import mute_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mute_api.MuteApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Product Mute
        api_response = api_instance.put_mute_state()
    except beoremote-cli.ApiException as e:
        print("Exception when calling MuteApi->put_mute_state: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_mute_state.ApiResponseFor200) | OK

#### put_mute_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

