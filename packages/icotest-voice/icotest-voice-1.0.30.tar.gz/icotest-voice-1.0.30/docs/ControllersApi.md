# icotest_voice.ControllersApi

All URIs are relative to *https://localhost/icotest_voice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_controller**](ControllersApi.md#delete_controller) | **DELETE** /controllers | DELETE Controller
[**get_controllers**](ControllersApi.md#get_controllers) | **GET** /controllers | GET controllers
[**post_controller_heartbeat**](ControllersApi.md#post_controller_heartbeat) | **POST** /controllers/{controller_id}/heartbeat | POST Controller heartbeat
[**put_controller**](ControllersApi.md#put_controller) | **PUT** /controllers | PUT controller


# **delete_controller**
> delete_controller(controller_id)

DELETE Controller

Delete an existing controller. WARNING: all devices and requests belonging to this controller, will also be deleted.

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
    api_instance = icotest_voice.ControllersApi(api_client)
    controller_id = 'ac331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the controller

    try:
        # DELETE Controller
        api_instance.delete_controller(controller_id)
    except ApiException as e:
        print("Exception when calling ControllersApi->delete_controller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | [**str**](.md)| the unique id of the controller | 

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

# **get_controllers**
> list[Controller] get_controllers(controller_id=controller_id)

GET controllers

Get a list of registered controllers

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
    api_instance = icotest_voice.ControllersApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of the controller (optional)

    try:
        # GET controllers
        api_response = api_instance.get_controllers(controller_id=controller_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ControllersApi->get_controllers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | [**str**](.md)| the unique id of the controller | [optional] 

### Return type

[**list[Controller]**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_controller_heartbeat**
> post_controller_heartbeat(controller_id)

POST Controller heartbeat

Controller heartbeat

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
    api_instance = icotest_voice.ControllersApi(api_client)
    controller_id = 'cc331ccb-5841-44ec-9d32-4f4fe0c3c16c' # str | the unique id of a controller

    try:
        # POST Controller heartbeat
        api_instance.post_controller_heartbeat(controller_id)
    except ApiException as e:
        print("Exception when calling ControllersApi->post_controller_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller_id** | [**str**](.md)| the unique id of a controller | 

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

# **put_controller**
> put_controller(controller=controller)

PUT controller

Add or update a controller

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
    api_instance = icotest_voice.ControllersApi(api_client)
    controller = {"controller_id":"10cda64a-0dce-4663-8b47-6ec1867f9568","description":"example controller","location":"server 1 rack 1","callback_url":"https://server:port","created":"2021-06-24T14:15:22Z","last_contact":"2021-06-24T14:15:22Z"} # Controller | The model of a controller (optional)

    try:
        # PUT controller
        api_instance.put_controller(controller=controller)
    except ApiException as e:
        print("Exception when calling ControllersApi->put_controller: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **controller** | [**Controller**](Controller.md)| The model of a controller | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

