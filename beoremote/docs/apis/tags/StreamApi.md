<a name="__pageTop"></a>
# beoremote-cli.apis.tags.stream_api.StreamApi

All URIs are relative to *http://beoproduct.local:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stream**](#get_stream) | **get** /BeoZone/Zone/Stream | Product Stream
[**post_stream_forward**](#post_stream_forward) | **post** /BeoZone/Zone/Stream/Forward | Forward Stream
[**post_stream_next**](#post_stream_next) | **post** /BeoZone/Zone/Stream/Next | Skip Stream
[**post_stream_pause**](#post_stream_pause) | **post** /BeoZone/Zone/Stream/Pause | Pause Stream
[**post_stream_play**](#post_stream_play) | **post** /BeoZone/Zone/Stream/Play | Play Stream
[**post_stream_skip**](#post_stream_skip) | **post** /BeoZone/Zone/Stream/Skip | Skip Stream
[**post_stream_stop**](#post_stream_stop) | **post** /BeoZone/Zone/Stream/Stop | Stop Stream

# **get_stream**
<a name="get_stream"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stream()

Product Stream

Poll the product stream.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Product Stream
        api_response = api_instance.get_stream()
        pprint(api_response)
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->get_stream: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stream.ApiResponseFor200) | OK

#### get_stream.ApiResponseFor200
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
**[features](#features)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# features

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_stream_forward**
<a name="post_stream_forward"></a>
> post_stream_forward()

Forward Stream

Forward to next item in the stream.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Forward Stream
        api_response = api_instance.post_stream_forward()
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->post_stream_forward: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_stream_forward.ApiResponseFor200) | OK

#### post_stream_forward.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_stream_next**
<a name="post_stream_next"></a>
> post_stream_next()

Skip Stream

Skip the playing item in the stream.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Skip Stream
        api_response = api_instance.post_stream_next()
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->post_stream_next: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_stream_next.ApiResponseFor200) | OK

#### post_stream_next.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_stream_pause**
<a name="post_stream_pause"></a>
> post_stream_pause()

Pause Stream

Pause the playing item in the stream

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Pause Stream
        api_response = api_instance.post_stream_pause()
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->post_stream_pause: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_stream_pause.ApiResponseFor200) | OK

#### post_stream_pause.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_stream_play**
<a name="post_stream_play"></a>
> post_stream_play()

Play Stream

Play the current item in the stream

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Play Stream
        api_response = api_instance.post_stream_play()
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->post_stream_play: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_stream_play.ApiResponseFor200) | OK

#### post_stream_play.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_stream_skip**
<a name="post_stream_skip"></a>
> post_stream_skip()

Skip Stream

Skip the playing item in the stream.

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Skip Stream
        api_response = api_instance.post_stream_skip()
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->post_stream_skip: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_stream_skip.ApiResponseFor200) | OK

#### post_stream_skip.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_stream_stop**
<a name="post_stream_stop"></a>
> post_stream_stop()

Stop Stream

Stop the playing item in the stream

### Example

```python
import beoremote-cli
from beoremote-cli.apis.tags import stream_api
from pprint import pprint
# Defining the host is optional and defaults to http://beoproduct.local:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = beoremote-cli.Configuration(
    host = "http://beoproduct.local:8080"
)

# Enter a context with an instance of the API client
with beoremote-cli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stop Stream
        api_response = api_instance.post_stream_stop()
    except beoremote-cli.ApiException as e:
        print("Exception when calling StreamApi->post_stream_stop: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#post_stream_stop.ApiResponseFor200) | OK

#### post_stream_stop.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

