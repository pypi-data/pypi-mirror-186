# icotest_voice.DevicesApi

All URIs are relative to *https://localhost/icotest_voice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices | DELETE Device
[**get_devices**](DevicesApi.md#get_devices) | **GET** /devices | GET devices
[**get_devices_status**](DevicesApi.md#get_devices_status) | **GET** /devices/{device_id}/status | GET device status
[**get_host_config**](DevicesApi.md#get_host_config) | **GET** /host/config | Your GET endpoint
[**post_device_deregister**](DevicesApi.md#post_device_deregister) | **POST** /devices/{device_id}/deregister | POST deregister device
[**post_device_make_call**](DevicesApi.md#post_device_make_call) | **POST** /devices/{device_id}/make_call | POST make call
[**post_device_register**](DevicesApi.md#post_device_register) | **POST** /devices/{device_id}/register | POST register device
[**post_devices_end_call**](DevicesApi.md#post_devices_end_call) | **POST** /devices/{device_id}/end_call | POST end call
[**post_devices_heartbeat**](DevicesApi.md#post_devices_heartbeat) | **POST** /devices/{device_id}/heartbeat | POST Device heartbeat
[**post_devices_receive_call**](DevicesApi.md#post_devices_receive_call) | **POST** /devices/{device_id}/receive_call | POST receive call
[**post_devices_scan**](DevicesApi.md#post_devices_scan) | **POST** /devices/{controller_id}/scan | POST device scan
[**post_devices_send_command**](DevicesApi.md#post_devices_send_command) | **POST** /devices/{device_id}/send_command | POST send command
[**put_device**](DevicesApi.md#put_device) | **PUT** /devices | PUT device
[**put_devices_status**](DevicesApi.md#put_devices_status) | **PUT** /devices/{device_id}/status | PUT device status
[**put_host_config**](DevicesApi.md#put_host_config) | **PUT** /host/config | 


# **delete_device**
> delete_device(device_id)

DELETE Device

Delete an existing device

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a device

    try:
        # DELETE Device
        api_instance.delete_device(device_id)
    except ApiException as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| the unique id of a device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> list[Device] get_devices(controller_id=controller_id, device_id=device_id, device_type=device_type, serial_no=serial_no, management_status=management_status)

GET devices

Get a list of available devices

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    controller_id = '10cda64a-0dce-4663-8b47-6ec1867f9568' # str | the unique id of the controller (optional)
device_id = '5ad25725-8be0-489d-9b26-c0299a76e136' # str | the unique id of the device (optional)
device_type = 'handset' # str | type of device (optional)
serial_no = 'serial-123456' # str | serial number (optional)
management_status = True # bool | management status (optional)

    try:
        # GET devices
        api_response = api_instance.get_devices(controller_id=controller_id, device_id=device_id, device_type=device_type, serial_no=serial_no, management_status=management_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | [**str**](.md)| the unique id of the controller | [optional] 
 **device_id** | [**str**](.md)| the unique id of the device | [optional] 
 **device_type** | **str**| type of device | [optional] 
 **serial_no** | **str**| serial number | [optional] 
 **management_status** | **bool**| management status | [optional] 

### Return type

[**list[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_status**
> object get_devices_status(device_id, valid_time_offset=valid_time_offset)

GET device status

Get device status within a certain time offset

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'device_id_example' # str | the unique id of the device
valid_time_offset = 56 # int | the valid time offset for the request (optional)

    try:
        # GET device status
        api_response = api_instance.get_devices_status(device_id, valid_time_offset=valid_time_offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| the unique id of the device | 
 **valid_time_offset** | **int**| the valid time offset for the request | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_config**
> HostConfig get_host_config()

Your GET endpoint

get configuration of host (IP address, name, etc.)

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    
    try:
        # Your GET endpoint
        api_response = api_instance.get_host_config()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_host_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HostConfig**](HostConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No connection to host |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device_deregister**
> str post_device_deregister(device_id)

POST deregister device

Post request to perform a device deregister from base station

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the device

    try:
        # POST deregister device
        api_response = api_instance.post_device_deregister(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_device_deregister: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| the unique id of the device | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device_make_call**
> str post_device_make_call(device_id, call_type, phone_number, call_duration=call_duration, outgoing_recording_file=outgoing_recording_file, playback_file=playback_file, playback_loop=playback_loop, wait_time=wait_time)

POST make call

Post request to make an internal or external call

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'device_id_example' # str | the unique id of the device
call_type = 'call_type_example' # str | internal or external call
phone_number = '1' # str | the number to call
call_duration = 56 # int | the duration of the call in seconds (0 is unlimited) (optional)
outgoing_recording_file = 'outgoing_call.wav' # str | the filename of the recorded call (optional)
playback_file = 'audio_playback.wav' # str | the filename of the playback file (optional)
playback_loop = true # bool | whether to play the playback file in a loop (optional)
wait_time = 30 # int | the duration of the wait time in seconds for the callee to respond (optional)

    try:
        # POST make call
        api_response = api_instance.post_device_make_call(device_id, call_type, phone_number, call_duration=call_duration, outgoing_recording_file=outgoing_recording_file, playback_file=playback_file, playback_loop=playback_loop, wait_time=wait_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_device_make_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| the unique id of the device | 
 **call_type** | **str**| internal or external call | 
 **phone_number** | **str**| the number to call | 
 **call_duration** | **int**| the duration of the call in seconds (0 is unlimited) | [optional] 
 **outgoing_recording_file** | **str**| the filename of the recorded call | [optional] 
 **playback_file** | **str**| the filename of the playback file | [optional] 
 **playback_loop** | **bool**| whether to play the playback file in a loop | [optional] 
 **wait_time** | **int**| the duration of the wait time in seconds for the callee to respond | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_device_register**
> str post_device_register(device_id, channel_number=channel_number, pin_code=pin_code)

POST register device

Post request to perform a device register to base station

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the device
channel_number = 56 # int | the number of the channel (optional)
pin_code = '1234' # str | the 4-digit PIN code (optional)

    try:
        # POST register device
        api_response = api_instance.post_device_register(device_id, channel_number=channel_number, pin_code=pin_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_device_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| the unique id of the device | 
 **channel_number** | **int**| the number of the channel | [optional] 
 **pin_code** | **str**| the 4-digit PIN code | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_end_call**
> str post_devices_end_call(device_id, reason=reason)

POST end call

Post request to end a call

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the device
reason = 'reason_example' # str | reason for ending call (optional)

    try:
        # POST end call
        api_response = api_instance.post_devices_end_call(device_id, reason=reason)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_devices_end_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| the unique id of the device | 
 **reason** | **str**| reason for ending call | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_heartbeat**
> post_devices_heartbeat(device_id)

POST Device heartbeat

Device heartbeat

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the device

    try:
        # POST Device heartbeat
        api_instance.post_devices_heartbeat(device_id)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_devices_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| the unique id of the device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_receive_call**
> str post_devices_receive_call(device_id, ring_count=ring_count, call_duration=call_duration, incoming_recording_file=incoming_recording_file, playback_file=playback_file, playback_loop=playback_loop, wait_time=wait_time)

POST receive call

Post request to receive a call

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'device_id_example' # str | the unique id of the device
ring_count = 3 # int | number of rings before call is picked up (optional)
call_duration = 56 # int | the duration of the call in seconds (0 is unlimited) (optional)
incoming_recording_file = 'incoming_call.wav' # str | the filename of the recorded call (optional)
playback_file = 'audio_playback.wav' # str | the filename of the playback file (optional)
playback_loop = true # bool | whether to play the playback file in a loop (optional)
wait_time = 30 # int | the duration of the wait time in seconds for the caller to make a call (optional)

    try:
        # POST receive call
        api_response = api_instance.post_devices_receive_call(device_id, ring_count=ring_count, call_duration=call_duration, incoming_recording_file=incoming_recording_file, playback_file=playback_file, playback_loop=playback_loop, wait_time=wait_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_devices_receive_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| the unique id of the device | 
 **ring_count** | **int**| number of rings before call is picked up | [optional] 
 **call_duration** | **int**| the duration of the call in seconds (0 is unlimited) | [optional] 
 **incoming_recording_file** | **str**| the filename of the recorded call | [optional] 
 **playback_file** | **str**| the filename of the playback file | [optional] 
 **playback_loop** | **bool**| whether to play the playback file in a loop | [optional] 
 **wait_time** | **int**| the duration of the wait time in seconds for the caller to make a call | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_scan**
> str post_devices_scan(controller_id)

POST device scan

Scan to discover new devices

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the controller

    try:
        # POST device scan
        api_response = api_instance.post_devices_scan(controller_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_devices_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | [**str**](.md)| the unique id of the controller | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_devices_send_command**
> str post_devices_send_command(device_id, command=command)

POST send command

Post request to send a command to device. This will be sent as numbers during an external call

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'bc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the device
command = 'command_example' # str | command to send (optional)

    try:
        # POST send command
        api_response = api_instance.post_devices_send_command(device_id, command=command)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->post_devices_send_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| the unique id of the device | 
 **command** | **str**| command to send | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_device**
> put_device(device=device)

PUT device

Add or update a device

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device = {"device_id":"bc331ccb-5841-44ec-9d32-4f4fe0c3c16c","serial_no":"serial-123456","device_type":"handset","url":"/dev/ttyACM1","created":"2019-08-24T14:15:22Z","updated":"2019-08-24T14:15:22Z","controller_id":"cc331ccb-5841-44ec-9d32-4f4fe0c3c16c","device_status":{},"callback_port":0,"management_status":true} # Device | the model of a device (optional)

    try:
        # PUT device
        api_instance.put_device(device=device)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)| the model of a device | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_status**
> put_devices_status(device_id, body=body)

PUT device status

Put device status

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    device_id = 'device_id_example' # str | the unique id of the device
body = {"battery_level":4,"date_generated":"2021-02-18T11:21:33.839384","handset_number":4,"registered":true,"registration_status":1,"rfpi":"030B469EC8","signal_level":"98","software_version":"SW:4.0.19.1,EEP:2.0,ATE:2.0.0"} # object | The model of a device (optional)

    try:
        # PUT device status
        api_instance.put_devices_status(device_id, body=body)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_devices_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| the unique id of the device | 
 **body** | **object**| The model of a device | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_host_config**
> put_host_config(host_config=host_config)



put a host configuration (IP address, name, etc.)

### Example

```python
from __future__ import print_function
import time
import icotest_voice
from icotest_voice.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/icotest_voice
# See configuration.py for a list of all supported configuration parameters.
configuration = icotest_voice.Configuration(
    host = "https://localhost/icotest_voice"
)


# Enter a context with an instance of the API client
with icotest_voice.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = icotest_voice.DevicesApi(api_client)
    host_config = icotest_voice.HostConfig() # HostConfig |  (optional)

    try:
        api_instance.put_host_config(host_config=host_config)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_host_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_config** | [**HostConfig**](HostConfig.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | No connection to host |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

