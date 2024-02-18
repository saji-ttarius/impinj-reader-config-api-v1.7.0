# swagger_client.DefaultApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_stream_get**](DefaultApi.md#data_stream_get) | **GET** /data/stream | Get HTTP stream
[**device_gpos_get**](DefaultApi.md#device_gpos_get) | **GET** /device/gpos | Retrieve GPO configurations.
[**device_gpos_put**](DefaultApi.md#device_gpos_put) | **PUT** /device/gpos | Update GPO configurations.
[**http_stream_get**](DefaultApi.md#http_stream_get) | **GET** /http-stream | Retrieve HTTP stream settings
[**http_stream_put**](DefaultApi.md#http_stream_put) | **PUT** /http-stream | Update HTTP stream settings
[**kafka_get**](DefaultApi.md#kafka_get) | **GET** /kafka | Retrieve Kafka settings
[**kafka_put**](DefaultApi.md#kafka_put) | **PUT** /kafka | Update Kafka settings
[**mqtt_get**](DefaultApi.md#mqtt_get) | **GET** /mqtt | Retrieve MQTT settings
[**mqtt_put**](DefaultApi.md#mqtt_put) | **PUT** /mqtt | Update MQTT settings
[**openapi_json_get**](DefaultApi.md#openapi_json_get) | **GET** /openapi.json | Get OpenAPI Document
[**profiles_get**](DefaultApi.md#profiles_get) | **GET** /profiles | Retrieve profiles
[**profiles_inventory_presets_get**](DefaultApi.md#profiles_inventory_presets_get) | **GET** /profiles/inventory/presets | Retrieve inventory presets
[**profiles_inventory_presets_preset_id_delete**](DefaultApi.md#profiles_inventory_presets_preset_id_delete) | **DELETE** /profiles/inventory/presets/{presetId} | Delete inventory preset
[**profiles_inventory_presets_preset_id_get**](DefaultApi.md#profiles_inventory_presets_preset_id_get) | **GET** /profiles/inventory/presets/{presetId} | Retrieve inventory preset detail
[**profiles_inventory_presets_preset_id_put**](DefaultApi.md#profiles_inventory_presets_preset_id_put) | **PUT** /profiles/inventory/presets/{presetId} | Create or replace inventory preset
[**profiles_inventory_presets_preset_id_start_post**](DefaultApi.md#profiles_inventory_presets_preset_id_start_post) | **POST** /profiles/inventory/presets/{presetId}/start | Start inventory preset
[**profiles_inventory_presets_schema_get**](DefaultApi.md#profiles_inventory_presets_schema_get) | **GET** /profiles/inventory/presets-schema | Retrieve inventory schema
[**profiles_inventory_start_post**](DefaultApi.md#profiles_inventory_start_post) | **POST** /profiles/inventory/start | Start transient inventory preset
[**profiles_inventory_tag_get**](DefaultApi.md#profiles_inventory_tag_get) | **GET** /profiles/inventory/tag | Checks for the presence of a tag in the field of view of an antenna.
[**profiles_stop_post**](DefaultApi.md#profiles_stop_post) | **POST** /profiles/stop | Stop preset
[**status_get**](DefaultApi.md#status_get) | **GET** /status | Retrieve status
[**system_access_authentication_get**](DefaultApi.md#system_access_authentication_get) | **GET** /system/access/authentication | Retrieve the reader&#39;s authentication configuration.
[**system_access_authentication_put**](DefaultApi.md#system_access_authentication_put) | **PUT** /system/access/authentication | Update the reader&#39;s authentication configuration.
[**system_access_users_get**](DefaultApi.md#system_access_users_get) | **GET** /system/access/users | Retrieve the list of users.
[**system_access_users_user_id_password_put**](DefaultApi.md#system_access_users_user_id_password_put) | **PUT** /system/access/users/{userId}/password | Update the password for the specified user.
[**system_antenna_hub_disable_post**](DefaultApi.md#system_antenna_hub_disable_post) | **POST** /system/antenna-hub/disable | Disable the antenna-hub feature.
[**system_antenna_hub_enable_post**](DefaultApi.md#system_antenna_hub_enable_post) | **POST** /system/antenna-hub/enable | Enable the antenna-hub feature.
[**system_antenna_hub_get**](DefaultApi.md#system_antenna_hub_get) | **GET** /system/antenna-hub | Retrieve antenna-hub information.
[**system_cap_installation_get**](DefaultApi.md#system_cap_installation_get) | **GET** /system/cap/installation | Retrieve the current installation configuration settings.
[**system_cap_installation_put**](DefaultApi.md#system_cap_installation_put) | **PUT** /system/cap/installation | Update CAP installation configuration settings.
[**system_certificates_ca_certs_cert_id_delete**](DefaultApi.md#system_certificates_ca_certs_cert_id_delete) | **DELETE** /system/certificates/ca/certs/{certId} | Remove CA certificate.
[**system_certificates_ca_certs_cert_id_get**](DefaultApi.md#system_certificates_ca_certs_cert_id_get) | **GET** /system/certificates/ca/certs/{certId} | Retrieve CA certificate.
[**system_certificates_ca_certs_get**](DefaultApi.md#system_certificates_ca_certs_get) | **GET** /system/certificates/ca/certs | Retrieve CA certificates.
[**system_certificates_ca_certs_post**](DefaultApi.md#system_certificates_ca_certs_post) | **POST** /system/certificates/ca/certs | Install CA certificates.
[**system_certificates_cap_certs_cert_id_delete**](DefaultApi.md#system_certificates_cap_certs_cert_id_delete) | **DELETE** /system/certificates/cap/certs/{certId} | Remove CAP authentication certificate.
[**system_certificates_cap_certs_cert_id_get**](DefaultApi.md#system_certificates_cap_certs_cert_id_get) | **GET** /system/certificates/cap/certs/{certId} | Retrieve a CAP authentication certificate.
[**system_certificates_cap_certs_get**](DefaultApi.md#system_certificates_cap_certs_get) | **GET** /system/certificates/cap/certs | Retrieve CAP authentication certificates.
[**system_certificates_cap_certs_post**](DefaultApi.md#system_certificates_cap_certs_post) | **POST** /system/certificates/cap/certs | Install CAP authentication certificates.
[**system_certificates_tls_certs_cert_id_delete**](DefaultApi.md#system_certificates_tls_certs_cert_id_delete) | **DELETE** /system/certificates/tls/certs/{certId} | Remove TLS certificate.
[**system_certificates_tls_certs_cert_id_get**](DefaultApi.md#system_certificates_tls_certs_cert_id_get) | **GET** /system/certificates/tls/certs/{certId} | Retrieve TLS certficate.
[**system_certificates_tls_certs_get**](DefaultApi.md#system_certificates_tls_certs_get) | **GET** /system/certificates/tls/certs | Retrieve TLS certificates.
[**system_certificates_tls_certs_post**](DefaultApi.md#system_certificates_tls_certs_post) | **POST** /system/certificates/tls/certs | Install TLS certificate.
[**system_certificates_tls_csr_post**](DefaultApi.md#system_certificates_tls_csr_post) | **POST** /system/certificates/tls/csr | Create a certificate signing request(CSR).
[**system_certificates_tls_services_tls_service_get**](DefaultApi.md#system_certificates_tls_services_tls_service_get) | **GET** /system/certificates/tls/services/{tlsService} | Retrieve certificate info for the specified service.
[**system_certificates_tls_services_tls_service_put**](DefaultApi.md#system_certificates_tls_services_tls_service_put) | **PUT** /system/certificates/tls/services/{tlsService} | Update certificate info for the specified service.
[**system_diagnostics_debug_bundle_get**](DefaultApi.md#system_diagnostics_debug_bundle_get) | **GET** /system/diagnostics/debug-bundle | Generate and retrieve a diagnostic bundle.
[**system_diagnostics_watchdog_bundle_delete**](DefaultApi.md#system_diagnostics_watchdog_bundle_delete) | **DELETE** /system/diagnostics/watchdog-bundle | Delete core files and diagnostic bundle generated by a watchdog reboot.
[**system_diagnostics_watchdog_bundle_get**](DefaultApi.md#system_diagnostics_watchdog_bundle_get) | **GET** /system/diagnostics/watchdog-bundle | Retrieve diagnostic bundle generated by a watchdog reboot.
[**system_get**](DefaultApi.md#system_get) | **GET** /system | Retrieve details about the reader hardware.
[**system_hostname_get**](DefaultApi.md#system_hostname_get) | **GET** /system/hostname | Retrieve the reader hostname.
[**system_hostname_put**](DefaultApi.md#system_hostname_put) | **PUT** /system/hostname | Update the reader hostname.
[**system_http_get**](DefaultApi.md#system_http_get) | **GET** /system/http | Retrieve the current HTTP server configuration settings.
[**system_http_put**](DefaultApi.md#system_http_put) | **PUT** /system/http | Update HTTP server configuration settings.
[**system_https_get**](DefaultApi.md#system_https_get) | **GET** /system/https | Retrieve the current HTTPS server configuration settings.
[**system_https_put**](DefaultApi.md#system_https_put) | **PUT** /system/https | Update HTTPS server configuration settings.
[**system_image_get**](DefaultApi.md#system_image_get) | **GET** /system/image | Retrieve details about the reader&#39;s firmware.
[**system_image_upgrade_get**](DefaultApi.md#system_image_upgrade_get) | **GET** /system/image/upgrade | Get details about the state of a firmware upgrade.
[**system_image_upgrade_post**](DefaultApi.md#system_image_upgrade_post) | **POST** /system/image/upgrade | Upload an upgrade file for installation.
[**system_mdns_get**](DefaultApi.md#system_mdns_get) | **GET** /system/mdns | Retrieve the current mDNS configuration settings.
[**system_mdns_put**](DefaultApi.md#system_mdns_put) | **PUT** /system/mdns | Update mDNS configuration settings.
[**system_network_dns_domains_get**](DefaultApi.md#system_network_dns_domains_get) | **GET** /system/network/dns/domains | Retrieve the search domains.
[**system_network_dns_domains_put**](DefaultApi.md#system_network_dns_domains_put) | **PUT** /system/network/dns/domains | Update static search domains used by the reader.
[**system_network_dns_servers_get**](DefaultApi.md#system_network_dns_servers_get) | **GET** /system/network/dns/servers | Retrieve the DNS servers from the reader.
[**system_network_dns_servers_put**](DefaultApi.md#system_network_dns_servers_put) | **PUT** /system/network/dns/servers | Update the static DNS servers used by the reader.
[**system_network_interfaces_get**](DefaultApi.md#system_network_interfaces_get) | **GET** /system/network/interfaces | Retrieve the current network information for all interfaces.
[**system_network_interfaces_interface_id_get**](DefaultApi.md#system_network_interfaces_interface_id_get) | **GET** /system/network/interfaces/{interfaceId} | Retrieve the specified network interface state.
[**system_network_interfaces_interface_id_network_protocol_configuration_get**](DefaultApi.md#system_network_interfaces_interface_id_network_protocol_configuration_get) | **GET** /system/network/interfaces/{interfaceId}/{networkProtocol}/configuration | Retrieve the current configuration of a network interface.
[**system_network_interfaces_interface_id_network_protocol_configuration_put**](DefaultApi.md#system_network_interfaces_interface_id_network_protocol_configuration_put) | **PUT** /system/network/interfaces/{interfaceId}/{networkProtocol}/configuration | Update the IP configuration of a network interface.
[**system_network_interfaces_interface_id_put**](DefaultApi.md#system_network_interfaces_interface_id_put) | **PUT** /system/network/interfaces/{interfaceId} | Enable the specified network interface.
[**system_network_interfaces_interface_id_wlan_access_points_get**](DefaultApi.md#system_network_interfaces_interface_id_wlan_access_points_get) | **GET** /system/network/interfaces/{interfaceId}/wlan/access-points | Retrieve a list of the available access points using the specified network interface.
[**system_network_interfaces_interface_id_wlan_connection_get**](DefaultApi.md#system_network_interfaces_interface_id_wlan_connection_get) | **GET** /system/network/interfaces/{interfaceId}/wlan/connection | Retrieve the current WLAN connection status.
[**system_network_interfaces_interface_id_wlan_connection_put**](DefaultApi.md#system_network_interfaces_interface_id_wlan_connection_put) | **PUT** /system/network/interfaces/{interfaceId}/wlan/connection | Request a connection to the specified access point.
[**system_power_get**](DefaultApi.md#system_power_get) | **GET** /system/power | Retrieve the current power configuration.
[**system_power_put**](DefaultApi.md#system_power_put) | **PUT** /system/power | Configure the power source.
[**system_reboot_post**](DefaultApi.md#system_reboot_post) | **POST** /system/reboot | Reboot the system.
[**system_region_get**](DefaultApi.md#system_region_get) | **GET** /system/region | Retrieve region information.
[**system_region_put**](DefaultApi.md#system_region_put) | **PUT** /system/region | Configure the operating region.
[**system_rfid_interface_get**](DefaultApi.md#system_rfid_interface_get) | **GET** /system/rfid/interface | Retrieve the reader API.
[**system_rfid_interface_put**](DefaultApi.md#system_rfid_interface_put) | **PUT** /system/rfid/interface | Configure the reader API.
[**system_rfid_llrp_get**](DefaultApi.md#system_rfid_llrp_get) | **GET** /system/rfid/llrp | Retrieve LLRP status.
[**system_time_get**](DefaultApi.md#system_time_get) | **GET** /system/time | Retrieve information about system time and uptime.
[**system_time_ntp_get**](DefaultApi.md#system_time_ntp_get) | **GET** /system/time/ntp | Retrieve the current state of the NTP service.
[**system_time_ntp_put**](DefaultApi.md#system_time_ntp_put) | **PUT** /system/time/ntp | Configure the NTP service.
[**system_time_ntp_servers_get**](DefaultApi.md#system_time_ntp_servers_get) | **GET** /system/time/ntp/servers | Retrieve NTP servers.
[**system_time_ntp_servers_post**](DefaultApi.md#system_time_ntp_servers_post) | **POST** /system/time/ntp/servers | Add a static NTP server.
[**system_time_ntp_servers_server_id_delete**](DefaultApi.md#system_time_ntp_servers_server_id_delete) | **DELETE** /system/time/ntp/servers/{serverId} | Remove a static NTP server.
[**system_time_ntp_servers_server_id_get**](DefaultApi.md#system_time_ntp_servers_server_id_get) | **GET** /system/time/ntp/servers/{serverId} | Retrieve details on a specific NTP server.
[**system_time_put**](DefaultApi.md#system_time_put) | **PUT** /system/time | Update the system time.
[**webhooks_event_get**](DefaultApi.md#webhooks_event_get) | **GET** /webhooks/event | Get the event webhook configuration.
[**webhooks_event_put**](DefaultApi.md#webhooks_event_put) | **PUT** /webhooks/event | Set the event webhook configuration.


# **data_stream_get**
> ReaderEvent data_stream_get()

Get HTTP stream

Get reader event data as an HTTP stream  **Connecting**  To connect to the reader, form an HTTP request and consume the resulting stream for as long as is practical. The reader will hold the connection open indefinitely, barring reader error, excessive client-side lag, network hiccups, reader maintenance or duplicate logins. In the event there is no new data to stream for an extended period of time, a keep-alive CR-LF character pair will be sent. See /http-stream path.  The method to form an HTTP request and parse the response will be different for every language or framework, so consult the documentation for the HTTP library you are using.  Some HTTP client libraries only return the response body after the connection has been closed by the server. These clients will not work for accessing data via HTTP streaming. You must use an HTTP client that will return response data incrementally. Most robust HTTP client libraries will provide this functionality. The Apache HttpClient will handle this use case, for example.  **Disconnections**  The reader will close a streaming connection for the following reasons:  - A client establishes too many connections with the same credentials. When this occurs, the oldest connection will be terminated.  - A client stops reading data suddenly. If the rate of tag reports being read off of the stream drops suddenly, the connection will be closed.  - A client reads data too slowly. Every streaming connection is backed by a queue of messages to be sent to the client. If this queue grows too large over time, the connection will be closed.  - The reader is rebooted.   **Stalls**   Set a timer, either a 90 second TCP level socket timeout, or a 90 second application level timer on the receipt  of new data. If 90 seconds pass with no data received, including newlines, disconnect and reconnect immediately.  The Streaming API will send a keep-alive periodically to prevent your application from timing out the  connection. You should wait at least 3 cycles to prevent spurious reconnects in the event of network congestion,  local CPU starvation, local GC pauses, etc. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get HTTP stream
    api_response = api_instance.data_stream_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->data_stream_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReaderEvent**](ReaderEvent.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_gpos_get**
> GpoConfigurations device_gpos_get()

Retrieve GPO configurations.

Retrieves the GPO configurations of the reader. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve GPO configurations.
    api_response = api_instance.device_gpos_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_gpos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GpoConfigurations**](GpoConfigurations.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_gpos_put**
> device_gpos_put(gpo_configurations)

Update GPO configurations.

Updates the GPO configurations of the reader. If no configuration is provided for a GPO then the existing configuration will be used. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
gpo_configurations = swagger_client.GpoConfigurations() # GpoConfigurations | 

try:
    # Update GPO configurations.
    api_instance.device_gpos_put(gpo_configurations)
except ApiException as e:
    print("Exception when calling DefaultApi->device_gpos_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpo_configurations** | [**GpoConfigurations**](GpoConfigurations.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_stream_get**
> StreamConfiguration http_stream_get()

Retrieve HTTP stream settings

Retrieves the configuration settings that apply to all HTTP streams.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve HTTP stream settings
    api_response = api_instance.http_stream_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->http_stream_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StreamConfiguration**](StreamConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **http_stream_put**
> http_stream_put(updated_stream_configuration)

Update HTTP stream settings

Updates the HTTP stream settings that apply to all HTTP streams.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
updated_stream_configuration = swagger_client.StreamConfiguration() # StreamConfiguration | The HTTP stream configuration settings

try:
    # Update HTTP stream settings
    api_instance.http_stream_put(updated_stream_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->http_stream_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_stream_configuration** | [**StreamConfiguration**](StreamConfiguration.md)| The HTTP stream configuration settings | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kafka_get**
> KafkaConfiguration kafka_get()

Retrieve Kafka settings

Retrieves the current Kafka configuration settings for pushing messages to a Kafka broker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve Kafka settings
    api_response = api_instance.kafka_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->kafka_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KafkaConfiguration**](KafkaConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kafka_put**
> kafka_put(updated_kafka_configuration)

Update Kafka settings

Updates the Kafka settings used by the device.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
updated_kafka_configuration = swagger_client.KafkaConfiguration() # KafkaConfiguration | The fully defined Kafka configuration settings the device should use when pushing messages to a Kafka broker.

try:
    # Update Kafka settings
    api_instance.kafka_put(updated_kafka_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->kafka_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_kafka_configuration** | [**KafkaConfiguration**](KafkaConfiguration.md)| The fully defined Kafka configuration settings the device should use when pushing messages to a Kafka broker. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mqtt_get**
> MqttConfiguration mqtt_get()

Retrieve MQTT settings

Retrieves the current MQTT configuration settings for publishing data to an MQTT broker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve MQTT settings
    api_response = api_instance.mqtt_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mqtt_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MqttConfiguration**](MqttConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mqtt_put**
> mqtt_put(updated_mqtt_configuration)

Update MQTT settings

Updates the MQTT settings used by the device.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
updated_mqtt_configuration = swagger_client.MqttConfiguration() # MqttConfiguration | The fully defined MQTT configuration settings the device should use when publishing data to an MQTT broker.

try:
    # Update MQTT settings
    api_instance.mqtt_put(updated_mqtt_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->mqtt_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_mqtt_configuration** | [**MqttConfiguration**](MqttConfiguration.md)| The fully defined MQTT configuration settings the device should use when publishing data to an MQTT broker. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_json_get**
> object openapi_json_get()

Get OpenAPI Document

Retrieve the OpenAPI Document for this Reader. The document describes the API using reader-specific capabilities and constraints, such as region-specific transmit power limits and supported RF Modes. It also includes definitions and paths associated with all registered profiles. If the IoT Interface is disabled, this will only contain system endpoints. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get OpenAPI Document
    api_response = api_instance.openapi_json_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->openapi_json_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_get**
> list[str] profiles_get()

Retrieve profiles

Retrieves the profiles (e.g. inventory, location, and direction) supported by this reader.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve profiles
    api_response = api_instance.profiles_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_presets_get**
> list[PresetId] profiles_inventory_presets_get()

Retrieve inventory presets

Retrieves the available presets for running inventory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve inventory presets
    api_response = api_instance.profiles_inventory_presets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_presets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PresetId]**](PresetId.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_presets_preset_id_delete**
> profiles_inventory_presets_preset_id_delete(preset_id)

Delete inventory preset

Removes a user-defined settings preset for executing inventory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
preset_id = 'preset_id_example' # str | The name of a preset.

try:
    # Delete inventory preset
    api_instance.profiles_inventory_presets_preset_id_delete(preset_id)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_presets_preset_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_id** | **str**| The name of a preset. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_presets_preset_id_get**
> InventoryRequest profiles_inventory_presets_preset_id_get(preset_id)

Retrieve inventory preset detail

Retrieves the detailed configuration of the specified preset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
preset_id = 'preset_id_example' # str | The name of a preset.

try:
    # Retrieve inventory preset detail
    api_response = api_instance.profiles_inventory_presets_preset_id_get(preset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_presets_preset_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_id** | **str**| The name of a preset. | 

### Return type

[**InventoryRequest**](InventoryRequest.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_presets_preset_id_put**
> object profiles_inventory_presets_preset_id_put(preset_id, preset_object)

Create or replace inventory preset

Creates or replaces a user-defined inventory preset.  Presets with names that begin with 'default' or 'impinj' may not be created or replaced. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
preset_id = 'preset_id_example' # str | The name of a preset.
preset_object = swagger_client.InventoryRequest() # InventoryRequest | inventory profile configuration

try:
    # Create or replace inventory preset
    api_response = api_instance.profiles_inventory_presets_preset_id_put(preset_id, preset_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_presets_preset_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_id** | **str**| The name of a preset. | 
 **preset_object** | [**InventoryRequest**](InventoryRequest.md)| inventory profile configuration | 

### Return type

**object**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_presets_preset_id_start_post**
> profiles_inventory_presets_preset_id_start_post(preset_id)

Start inventory preset

Starts running the specified inventory preset. The running preset cannot be replaced or deleted. The preset will be automatically restarted if the reader reboots. If the reader is restarted multiple times in quick succcession the saved preset may be stopped to prevent the bad preset from blocking access to the rest interface. If this occurs an ERROR level message will be logged. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
preset_id = 'preset_id_example' # str | The name of a preset.

try:
    # Start inventory preset
    api_instance.profiles_inventory_presets_preset_id_start_post(preset_id)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_presets_preset_id_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_id** | **str**| The name of a preset. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_presets_schema_get**
> PresetsSchema profiles_inventory_presets_schema_get()

Retrieve inventory schema

Deprecated: This path will be removed in a future release. The device-specific schema and capabilities can be observed via the \"/openapi.json\" API path instead.  Retrieves the reader-specific JSON schema used to validate inventory presets. This is a good way to determine reader capabilities such as max transmit power or available RF modes. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve inventory schema
    api_response = api_instance.profiles_inventory_presets_schema_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_presets_schema_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PresetsSchema**](PresetsSchema.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_start_post**
> profiles_inventory_start_post(preset_object)

Start transient inventory preset

Start running inventory using the provided inventory configuration. The configuration is not saved and not restarted if the reader reboots.  Transient presets are recommended for running configuration that is updated frequently or for which there is no benefit to storing the configuration on the reader after the preset has stopped. Transient presets are usually the best choice when performing operations that modify tag memory or are meant to operate on a specific tag. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
preset_object = swagger_client.InventoryRequest() # InventoryRequest | inventory profile configuration

try:
    # Start transient inventory preset
    api_instance.profiles_inventory_start_post(preset_object)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_object** | [**InventoryRequest**](InventoryRequest.md)| inventory profile configuration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_inventory_tag_get**
> TagPresenceResponse profiles_inventory_tag_get(epc=epc, epc_hex=epc_hex, tid=tid, tid_hex=tid_hex, antenna_port=antenna_port, antenna_name=antenna_name)

Checks for the presence of a tag in the field of view of an antenna.

Returns information on whether the specified tag was seen on the specified antenna in the tag reporting interval. Available only if TagReportingConfiguration feature is enabled. Must specify exactly one tag identifier and one antenna identifier. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
epc = 'epc_example' # str | The base64url-encoded EPC of the tag of interest. (optional)
epc_hex = 'epc_hex_example' # str | The hex-encoded EPC of the tag of interest. (optional)
tid = 'tid_example' # str | The base64url-encoded TID of the tag of interest. (optional)
tid_hex = 'tid_hex_example' # str | The hex-encoded TID of the tag of interest. (optional)
antenna_port = 56 # int | The port number of the antenna for the tag of interest. (optional)
antenna_name = 'antenna_name_example' # str | Name for the antenna for the tag of interest. (optional)

try:
    # Checks for the presence of a tag in the field of view of an antenna.
    api_response = api_instance.profiles_inventory_tag_get(epc=epc, epc_hex=epc_hex, tid=tid, tid_hex=tid_hex, antenna_port=antenna_port, antenna_name=antenna_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_inventory_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epc** | **str**| The base64url-encoded EPC of the tag of interest. | [optional] 
 **epc_hex** | **str**| The hex-encoded EPC of the tag of interest. | [optional] 
 **tid** | **str**| The base64url-encoded TID of the tag of interest. | [optional] 
 **tid_hex** | **str**| The hex-encoded TID of the tag of interest. | [optional] 
 **antenna_port** | **int**| The port number of the antenna for the tag of interest. | [optional] 
 **antenna_name** | **str**| Name for the antenna for the tag of interest. | [optional] 

### Return type

[**TagPresenceResponse**](TagPresenceResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles_stop_post**
> profiles_stop_post()

Stop preset

Stops the currently running profile preset. If no preset is currently running, this is a no-op. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Stop preset
    api_instance.profiles_stop_post()
except ApiException as e:
    print("Exception when calling DefaultApi->profiles_stop_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> ReaderStatus status_get()

Retrieve status

Retrieves the reader's current status. This endpoint allow's a user to query what the reader is actively working on, if anything. The information contained here will indicate the last request the reader responded to that resulted in it taking some modem action, such as starting or stopping inventory. Configuration API calls are not included. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve status
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReaderStatus**](ReaderStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_access_authentication_get**
> AuthenticationConfig system_access_authentication_get()

Retrieve the reader's authentication configuration.

Retrieves the reader's authentication configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the reader's authentication configuration.
    api_response = api_instance.system_access_authentication_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_access_authentication_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationConfig**](AuthenticationConfig.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_access_authentication_put**
> system_access_authentication_put(auth_config)

Update the reader's authentication configuration.

Updates the reader's authentication configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
auth_config = swagger_client.AuthenticationConfig() # AuthenticationConfig | The authentication configuration to update.

try:
    # Update the reader's authentication configuration.
    api_instance.system_access_authentication_put(auth_config)
except ApiException as e:
    print("Exception when calling DefaultApi->system_access_authentication_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_config** | [**AuthenticationConfig**](AuthenticationConfig.md)| The authentication configuration to update. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_access_users_get**
> list[UserInfo] system_access_users_get()

Retrieve the list of users.

Retrieves the list of users that can access reader. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the list of users.
    api_response = api_instance.system_access_users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_access_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserInfo]**](UserInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_access_users_user_id_password_put**
> system_access_users_user_id_password_put(user_id, password_info)

Update the password for the specified user.

Updates the password for the specified user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The unique identifier for a user.
password_info = swagger_client.PasswordInfo() # PasswordInfo | 

try:
    # Update the password for the specified user.
    api_instance.system_access_users_user_id_password_put(user_id, password_info)
except ApiException as e:
    print("Exception when calling DefaultApi->system_access_users_user_id_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The unique identifier for a user. | 
 **password_info** | [**PasswordInfo**](PasswordInfo.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_antenna_hub_disable_post**
> StatusResponse system_antenna_hub_disable_post()

Disable the antenna-hub feature.

Disable the antenna-hub feature. System reboot is required for the new configuration to take effect. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Disable the antenna-hub feature.
    api_response = api_instance.system_antenna_hub_disable_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_antenna_hub_disable_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_antenna_hub_enable_post**
> StatusResponse system_antenna_hub_enable_post()

Enable the antenna-hub feature.

Enable the antenna-hub feature. System reboot is required for the new configuration to take effect. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Enable the antenna-hub feature.
    api_response = api_instance.system_antenna_hub_enable_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_antenna_hub_enable_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_antenna_hub_get**
> AntennaHubInfo system_antenna_hub_get(pending=pending)

Retrieve antenna-hub information.

Retrieve the current antenna-hub status, including a list of connected hubs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
pending = true # bool | If set to true, the response will reflect the future antenna-hub state after the next reboot. This will differ from the current state when a request to enable or disable the antenna-hub feature has been made.  (optional)

try:
    # Retrieve antenna-hub information.
    api_response = api_instance.system_antenna_hub_get(pending=pending)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_antenna_hub_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending** | **bool**| If set to true, the response will reflect the future antenna-hub state after the next reboot. This will differ from the current state when a request to enable or disable the antenna-hub feature has been made.  | [optional] 

### Return type

[**AntennaHubInfo**](AntennaHubInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_cap_installation_get**
> CapInstallationConfiguration system_cap_installation_get()

Retrieve the current installation configuration settings.

Retrieve the current Customer Application (CAP) installation configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current installation configuration settings.
    api_response = api_instance.system_cap_installation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_cap_installation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CapInstallationConfiguration**](CapInstallationConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_cap_installation_put**
> system_cap_installation_put(installation_configuration)

Update CAP installation configuration settings.

Updates CAP installation configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
installation_configuration = swagger_client.CapInstallationConfiguration() # CapInstallationConfiguration | The new CAP installation configuration settings.

try:
    # Update CAP installation configuration settings.
    api_instance.system_cap_installation_put(installation_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->system_cap_installation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installation_configuration** | [**CapInstallationConfiguration**](CapInstallationConfiguration.md)| The new CAP installation configuration settings. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_ca_certs_cert_id_delete**
> system_certificates_ca_certs_cert_id_delete(cert_id)

Remove CA certificate.

Removes the specified CA certificate from the reader.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 56 # int | The unique identifier assigned to the certificate by the reader.

try:
    # Remove CA certificate.
    api_instance.system_certificates_ca_certs_cert_id_delete(cert_id)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_ca_certs_cert_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The unique identifier assigned to the certificate by the reader. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_ca_certs_cert_id_get**
> CertificateInfo system_certificates_ca_certs_cert_id_get(cert_id)

Retrieve CA certificate.

Retrieves certficate information for the specified CA certificate. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 56 # int | The unique identifier assigned to the certificate by the reader.

try:
    # Retrieve CA certificate.
    api_response = api_instance.system_certificates_ca_certs_cert_id_get(cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_ca_certs_cert_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The unique identifier assigned to the certificate by the reader. | 

### Return type

[**CertificateInfo**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_ca_certs_get**
> list[CertificateInfo] system_certificates_ca_certs_get()

Retrieve CA certificates.

Retrieves user-installed CA certificates on the reader which includes Root and intermediate CA certificates. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve CA certificates.
    api_response = api_instance.system_certificates_ca_certs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_ca_certs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CertificateInfo]**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_ca_certs_post**
> list[CertificateId] system_certificates_ca_certs_post(cert_file)

Install CA certificates.

Installs CA certificates on the reader. Only PEM format is supported. It is possible to install a certificate bundle which contains multiple certificates. The certificates will be automatically validated prior to installing on the reader.  The certificate ID assigned to each certificate will be returned in the response upon successful installation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_file = '/path/to/file.txt' # file | The certificate file to be installed on the reader.

try:
    # Install CA certificates.
    api_response = api_instance.system_certificates_ca_certs_post(cert_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_ca_certs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_file** | **file**| The certificate file to be installed on the reader. | 

### Return type

[**list[CertificateId]**](CertificateId.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_cap_certs_cert_id_delete**
> system_certificates_cap_certs_cert_id_delete(cert_id)

Remove CAP authentication certificate.

Removes the specified CAP authentication certificate from the reader.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 56 # int | The unique identifier assigned to the certificate by the reader.

try:
    # Remove CAP authentication certificate.
    api_instance.system_certificates_cap_certs_cert_id_delete(cert_id)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_cap_certs_cert_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The unique identifier assigned to the certificate by the reader. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_cap_certs_cert_id_get**
> CertificateInfo system_certificates_cap_certs_cert_id_get(cert_id)

Retrieve a CAP authentication certificate.

Retrieves certificate information for the specified CAP authentication certificate. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 56 # int | The unique identifier assigned to the certificate by the reader.

try:
    # Retrieve a CAP authentication certificate.
    api_response = api_instance.system_certificates_cap_certs_cert_id_get(cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_cap_certs_cert_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The unique identifier assigned to the certificate by the reader. | 

### Return type

[**CertificateInfo**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_cap_certs_get**
> list[CertificateInfo] system_certificates_cap_certs_get()

Retrieve CAP authentication certificates.

Retrieves all installed CAP authentication certificates on the reader. This may include the default certificate, if it has not been removed. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve CAP authentication certificates.
    api_response = api_instance.system_certificates_cap_certs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_cap_certs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CertificateInfo]**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_cap_certs_post**
> list[CertificateId] system_certificates_cap_certs_post(cert_file)

Install CAP authentication certificates.

Installs a single CAP authentication certificate on the reader. Only PEM format is supported. The certificate will be validated prior to installing on the reader.  On success, an array containing a single certificate ID will be returned in the response. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_file = '/path/to/file.txt' # file | The CAP authentication certificate file to be installed on the reader.

try:
    # Install CAP authentication certificates.
    api_response = api_instance.system_certificates_cap_certs_post(cert_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_cap_certs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_file** | **file**| The CAP authentication certificate file to be installed on the reader. | 

### Return type

[**list[CertificateId]**](CertificateId.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_certs_cert_id_delete**
> system_certificates_tls_certs_cert_id_delete(cert_id)

Remove TLS certificate.

Removes the specified certificate from the reader. The private key associated with the certificate will be automatically removed as well. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 56 # int | The unique identifier assigned to the certificate by the reader.

try:
    # Remove TLS certificate.
    api_instance.system_certificates_tls_certs_cert_id_delete(cert_id)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_certs_cert_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The unique identifier assigned to the certificate by the reader. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_certs_cert_id_get**
> CertificateInfo system_certificates_tls_certs_cert_id_get(cert_id)

Retrieve TLS certficate.

Retrieves TLS certficate information for the specified certificate. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_id = 56 # int | The unique identifier assigned to the certificate by the reader.

try:
    # Retrieve TLS certficate.
    api_response = api_instance.system_certificates_tls_certs_cert_id_get(cert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_certs_cert_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_id** | **int**| The unique identifier assigned to the certificate by the reader. | 

### Return type

[**CertificateInfo**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_certs_get**
> list[CertificateInfo] system_certificates_tls_certs_get()

Retrieve TLS certificates.

Retrieves user-installed TLS certificates on the reader which includes server and client certificates. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve TLS certificates.
    api_response = api_instance.system_certificates_tls_certs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_certs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CertificateInfo]**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_certs_post**
> CertificateId system_certificates_tls_certs_post(cert_file, password=password)

Install TLS certificate.

Installs TLS certificate on the reader using either pkcs12 or PEM format.  When installing a certificate using pkcs12 format, the password used to encrypt the bundle must be included in the request.  The certificate ID will be returned in the response upon successful installation. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
cert_file = '/path/to/file.txt' # file | The certificate file to be installed on the reader.
password = 'password_example' # str | The password that was used to create the pkcs12 bundle. (optional)

try:
    # Install TLS certificate.
    api_response = api_instance.system_certificates_tls_certs_post(cert_file, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_certs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_file** | **file**| The certificate file to be installed on the reader. | 
 **password** | **str**| The password that was used to create the pkcs12 bundle. | [optional] 

### Return type

[**CertificateId**](CertificateId.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_csr_post**
> file system_certificates_tls_csr_post(csr_configuration)

Create a certificate signing request(CSR).

Create a CSR file that could be sent to a Certificate Authority(CA) for certificate issuance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
csr_configuration = swagger_client.CsrConfiguration() # CsrConfiguration | The configuration settings to be included in the CSR.

try:
    # Create a certificate signing request(CSR).
    api_response = api_instance.system_certificates_tls_csr_post(csr_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_csr_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_configuration** | [**CsrConfiguration**](CsrConfiguration.md)| The configuration settings to be included in the CSR. | 

### Return type

[**file**](file.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_services_tls_service_get**
> CertificateInfo system_certificates_tls_services_tls_service_get(tls_service)

Retrieve certificate info for the specified service.

Retrieves the certificate info for the specified service. If the specified service has not been configured to use a user-installed certificate, a 204 response will be returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
tls_service = 'tls_service_example' # str | Available services on the reader that use TLS certificates.

try:
    # Retrieve certificate info for the specified service.
    api_response = api_instance.system_certificates_tls_services_tls_service_get(tls_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_services_tls_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_service** | **str**| Available services on the reader that use TLS certificates. | 

### Return type

[**CertificateInfo**](CertificateInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_certificates_tls_services_tls_service_put**
> system_certificates_tls_services_tls_service_put(tls_service, cert_config)

Update certificate info for the specified service.

Updates certificate info for the specified service to use one of the available certificates installed on the reader.  The extended key usage on the certificate must match the intended usage of the service.  For example: If the extended key usage on the certificate only have `server authentication` bit set, then the certificate can not be used for 'client authentication' (e.g `mqtt-client`).  If the extended key usage on the certificate have both `server authentication` and 'client authentication' bits set, then the certificate could be used for both `https-server` and `mqtt-client`.  If the extended key usage on the certificate is not specified, then the certificate could be used for any purpose that the reader supports. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
tls_service = 'tls_service_example' # str | Available services on the reader that use TLS certificates.
cert_config = swagger_client.CertificateConfig() # CertificateConfig | 

try:
    # Update certificate info for the specified service.
    api_instance.system_certificates_tls_services_tls_service_put(tls_service, cert_config)
except ApiException as e:
    print("Exception when calling DefaultApi->system_certificates_tls_services_tls_service_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_service** | **str**| Available services on the reader that use TLS certificates. | 
 **cert_config** | [**CertificateConfig**](CertificateConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_diagnostics_debug_bundle_get**
> file system_diagnostics_debug_bundle_get()

Generate and retrieve a diagnostic bundle.

Generates and retrieves a diagnostic bundle containing current diagnostic information.  The bundle contains - An index.html file containing information about the bundle, including the time it was   generated and the directory structure. - The syslog logs - The journal logs - Core files - The RDD buffer - OS release information - A startup graph - Other reader configuration information This bundle is not stored on the reader. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Generate and retrieve a diagnostic bundle.
    api_response = api_instance.system_diagnostics_debug_bundle_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_diagnostics_debug_bundle_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/gzip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_diagnostics_watchdog_bundle_delete**
> system_diagnostics_watchdog_bundle_delete()

Delete core files and diagnostic bundle generated by a watchdog reboot.

Deletes all core files on the reader and the diagnostic bundle generated by a watchdog reboot, if one exists. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Delete core files and diagnostic bundle generated by a watchdog reboot.
    api_instance.system_diagnostics_watchdog_bundle_delete()
except ApiException as e:
    print("Exception when calling DefaultApi->system_diagnostics_watchdog_bundle_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_diagnostics_watchdog_bundle_get**
> file system_diagnostics_watchdog_bundle_get()

Retrieve diagnostic bundle generated by a watchdog reboot.

Retrieves an existing diagnostic bundle generated before the most recent watchdog reboot, if one exists. When a watchdog reboot occurs, a bundle is generated from the logs and other reader state information before the reboot. At most one such bundle can be stored on the reader at a time. If another watchdog reboot occurs when there is already a bundle stored on the reader, the oldest will be overwritten. The information contained in this bundle is a snapshot of the reader state immediately before the most recent watchdog reboot.  The bundle contains - An index.html file containing information about the bundle, including the time it was   generated and its directory structure. - The syslog logs - The journal logs - Core files - The RDD buffer - OS release information - A startup graph - Other reader configuration and state information 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve diagnostic bundle generated by a watchdog reboot.
    api_response = api_instance.system_diagnostics_watchdog_bundle_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_diagnostics_watchdog_bundle_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/gzip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get**
> SystemInfo system_get()

Retrieve details about the reader hardware.

Retrieve details about the reader hardware.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve details about the reader hardware.
    api_response = api_instance.system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_hostname_get**
> Hostname system_hostname_get()

Retrieve the reader hostname.

Retrieves the current hostname of the reader. Note that this is not a fully qualified domain name. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the reader hostname.
    api_response = api_instance.system_hostname_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_hostname_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Hostname**](Hostname.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_hostname_put**
> system_hostname_put(hostname)

Update the reader hostname.

Updates the reader hostname to the specified value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
hostname = swagger_client.Hostname() # Hostname | The new hostname to be set for the reader. The hostname must conform with RFC-952 and RFC-1123. 

try:
    # Update the reader hostname.
    api_instance.system_hostname_put(hostname)
except ApiException as e:
    print("Exception when calling DefaultApi->system_hostname_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | [**Hostname**](Hostname.md)| The new hostname to be set for the reader. The hostname must conform with RFC-952 and RFC-1123.  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_http_get**
> HttpConfiguration system_http_get()

Retrieve the current HTTP server configuration settings.

Retrieves the current HTTP server configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current HTTP server configuration settings.
    api_response = api_instance.system_http_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_http_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HttpConfiguration**](HttpConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_http_put**
> system_http_put(http_configuration)

Update HTTP server configuration settings.

Updates HTTP server configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
http_configuration = swagger_client.HttpConfiguration() # HttpConfiguration | The new HTTP configuration settings.

try:
    # Update HTTP server configuration settings.
    api_instance.system_http_put(http_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->system_http_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_configuration** | [**HttpConfiguration**](HttpConfiguration.md)| The new HTTP configuration settings. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_https_get**
> HttpsConfiguration system_https_get()

Retrieve the current HTTPS server configuration settings.

Retrieves the current HTTPS server configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current HTTPS server configuration settings.
    api_response = api_instance.system_https_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_https_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HttpsConfiguration**](HttpsConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_https_put**
> system_https_put(https_configuration)

Update HTTPS server configuration settings.

Updates HTTPS server configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
https_configuration = swagger_client.HttpsConfiguration() # HttpsConfiguration | The new HTTPS configuration settings.

try:
    # Update HTTPS server configuration settings.
    api_instance.system_https_put(https_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->system_https_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **https_configuration** | [**HttpsConfiguration**](HttpsConfiguration.md)| The new HTTPS configuration settings. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_get**
> SystemImage system_image_get()

Retrieve details about the reader's firmware.

A successful `GET` request to this endpoint will return detailed information about the firmware installed on the reader. Properties are omitted for uninstalled or unavailable partitions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve details about the reader's firmware.
    api_response = api_instance.system_image_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_image_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemImage**](SystemImage.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_upgrade_get**
> UpgradeStatus system_image_upgrade_get()

Get details about the state of a firmware upgrade.

The state of any upgrades occurring on the reader can be monitored from this endpoint.  Note that once an upgrade has reached the `successful` state, it will take effect the next time the reader is booted. The user must trigger the reboot as the reader won't reboot on its own. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get details about the state of a firmware upgrade.
    api_response = api_instance.system_image_upgrade_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_image_upgrade_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeStatus**](UpgradeStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_upgrade_post**
> system_image_upgrade_post(upgrade_file)

Upload an upgrade file for installation.

In order to perform an upgrade, the upgrade file must be uploaded to the reader using this endpoint. Upon successfully uploading an upgrade file to the reader, the reader will acknowledge receipt of the upgrade file by issuing a `202: Accepted` response.  Following such a response, the client can visit the status URL for the current state of the upgrade operation.  Once an upgrade file has completed transfer with this endpoint, subsequent requests will receive a response of `409: Conflict` until one of the following conditions is met:  - The upgrade was successfully installed, and the reader is awaiting reboot. - The upgrade failed to install.  If an upgrade has been installed, but the reader has not yet been rebooted, a different upgrade file can be installed over the previous upgrade.  Any successfully installed upgrade will take effect the next time the reader is booted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
upgrade_file = '/path/to/file.txt' # file | The upgrade file to be installed on the reader.

try:
    # Upload an upgrade file for installation.
    api_instance.system_image_upgrade_post(upgrade_file)
except ApiException as e:
    print("Exception when calling DefaultApi->system_image_upgrade_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_file** | **file**| The upgrade file to be installed on the reader. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_mdns_get**
> MdnsConfiguration system_mdns_get()

Retrieve the current mDNS configuration settings.

Retrieve the current mDNS configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current mDNS configuration settings.
    api_response = api_instance.system_mdns_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_mdns_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MdnsConfiguration**](MdnsConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_mdns_put**
> StatusResponse system_mdns_put(mdns_configuration)

Update mDNS configuration settings.

Updates mDNS configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
mdns_configuration = swagger_client.MdnsConfiguration() # MdnsConfiguration | The new mDNS configuration settings.

try:
    # Update mDNS configuration settings.
    api_response = api_instance.system_mdns_put(mdns_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_mdns_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mdns_configuration** | [**MdnsConfiguration**](MdnsConfiguration.md)| The new mDNS configuration settings. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_dns_domains_get**
> SearchDomains system_network_dns_domains_get()

Retrieve the search domains.

Retrieves both static and dynamic search domains that are being used by the DNS resolver on the reader. Dynamic search domains are configured automatically via a DHCP server and static search domains are those configured manually. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the search domains.
    api_response = api_instance.system_network_dns_domains_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_dns_domains_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchDomains**](SearchDomains.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_dns_domains_put**
> system_network_dns_domains_put(search_domains)

Update static search domains used by the reader.

Updates the static search domains used by the reader. Up to 12 static search domains are allowed. It is possible to convert the dynamic search domains to static search domains by including them on the list to update. An empty list of search domains would indicate that no static search domains should be used and all previously configured search domains should be removed from the reader. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
search_domains = swagger_client.SearchDomains() # SearchDomains | A list of static search domains to update.

try:
    # Update static search domains used by the reader.
    api_instance.system_network_dns_domains_put(search_domains)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_dns_domains_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_domains** | [**SearchDomains**](SearchDomains.md)| A list of static search domains to update. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_dns_servers_get**
> DnsServers system_network_dns_servers_get()

Retrieve the DNS servers from the reader.

Retrieves both static and dynamic DNS servers that are being used by the DNS resolver on the reader. Dynamic DNS servers are obtained automatically via a DHCP server and static DNS servers are those configured manually by users. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the DNS servers from the reader.
    api_response = api_instance.system_network_dns_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_dns_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DnsServers**](DnsServers.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_dns_servers_put**
> system_network_dns_servers_put(dns_servers)

Update the static DNS servers used by the reader.

Updates the static DNS servers used by the reader. Up to 12 static DNS servers are allowed. It is possible to convert dynamic DNS servers to static DNS servers by including them on the list to update. An empty list of DNS servers would indicate that no static DNS server should be used and all previously configured DNS servers should be removed from the reader. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dns_servers = swagger_client.DnsServers() # DnsServers | A list of static DNS servers to update.

try:
    # Update the static DNS servers used by the reader.
    api_instance.system_network_dns_servers_put(dns_servers)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_dns_servers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_servers** | [**DnsServers**](DnsServers.md)| A list of static DNS servers to update. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_get**
> list[NetworkInterface] system_network_interfaces_get()

Retrieve the current network information for all interfaces.

Retrieves the available network interfaces and their current network information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current network information for all interfaces.
    api_response = api_instance.system_network_interfaces_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetworkInterface]**](NetworkInterface.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_get**
> NetworkInterface system_network_interfaces_interface_id_get(interface_id, pending=pending)

Retrieve the specified network interface state.

Retrieves the specified network interface state. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.
pending = true # bool |  (optional)

try:
    # Retrieve the specified network interface state.
    api_response = api_instance.system_network_interfaces_interface_id_get(interface_id, pending=pending)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 
 **pending** | **bool**|  | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_network_protocol_configuration_get**
> IpConfiguration system_network_interfaces_interface_id_network_protocol_configuration_get(interface_id, network_protocol)

Retrieve the current configuration of a network interface.

Retrieves the current IPv4 or IPv6 configuration of the specified interface. The `networkProtocol` parameter indicates a specific Network Protocol version of the configuration to retrieve. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.
network_protocol = 'network_protocol_example' # str | The network protocol version of the configuration.

try:
    # Retrieve the current configuration of a network interface.
    api_response = api_instance.system_network_interfaces_interface_id_network_protocol_configuration_get(interface_id, network_protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_network_protocol_configuration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 
 **network_protocol** | **str**| The network protocol version of the configuration. | 

### Return type

[**IpConfiguration**](IpConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_network_protocol_configuration_put**
> StatusResponse system_network_interfaces_interface_id_network_protocol_configuration_put(interface_id, network_protocol, ip_configuration)

Update the IP configuration of a network interface.

Updates IPv4 or IPv6 configuration for the specified interface. This endpoint could be used to change the addressing mode between dynamic and static as well as setting the static IP address, prefix length, and gateway. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.
network_protocol = 'network_protocol_example' # str | The network protocol version of the configuration.
ip_configuration = swagger_client.IpConfiguration() # IpConfiguration | 

try:
    # Update the IP configuration of a network interface.
    api_response = api_instance.system_network_interfaces_interface_id_network_protocol_configuration_put(interface_id, network_protocol, ip_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_network_protocol_configuration_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 
 **network_protocol** | **str**| The network protocol version of the configuration. | 
 **ip_configuration** | [**IpConfiguration**](IpConfiguration.md)|  | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_put**
> StatusResponse system_network_interfaces_interface_id_put(interface_id, network_interface_state)

Enable the specified network interface.

Enable the specified network interface. There can be only one enabled and active interface at a time. A reboot is required for the change to take effect. Until the reader is rebooted, the previous enabled interface will stay active. Enabling one interface will automatically disable the other interface after the reader reboot. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.
network_interface_state = swagger_client.NetworkInterfaceState() # NetworkInterfaceState | 

try:
    # Enable the specified network interface.
    api_response = api_instance.system_network_interfaces_interface_id_put(interface_id, network_interface_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 
 **network_interface_state** | [**NetworkInterfaceState**](NetworkInterfaceState.md)|  | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_wlan_access_points_get**
> list[NetworkWlanAccessPoint] system_network_interfaces_interface_id_wlan_access_points_get(interface_id)

Retrieve a list of the available access points using the specified network interface.

Scan for access points using the specified network interface and return a list of available access points along with related information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.

try:
    # Retrieve a list of the available access points using the specified network interface.
    api_response = api_instance.system_network_interfaces_interface_id_wlan_access_points_get(interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_wlan_access_points_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 

### Return type

[**list[NetworkWlanAccessPoint]**](NetworkWlanAccessPoint.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_wlan_connection_get**
> NetworkWlanConnectionStatus system_network_interfaces_interface_id_wlan_connection_get(interface_id)

Retrieve the current WLAN connection status.

Retrieves the current WLAN connection status. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.

try:
    # Retrieve the current WLAN connection status.
    api_response = api_instance.system_network_interfaces_interface_id_wlan_connection_get(interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_wlan_connection_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 

### Return type

[**NetworkWlanConnectionStatus**](NetworkWlanConnectionStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_network_interfaces_interface_id_wlan_connection_put**
> StatusResponse system_network_interfaces_interface_id_wlan_connection_put(interface_id, network_wlan_connection)

Request a connection to the specified access point.

Request a network connection to the specified access point using the specified SSID and a password. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
interface_id = 56 # int | The unique identifier of the network interface assigned by the reader.
network_wlan_connection = swagger_client.NetworkWlanConnection() # NetworkWlanConnection | 

try:
    # Request a connection to the specified access point.
    api_response = api_instance.system_network_interfaces_interface_id_wlan_connection_put(interface_id, network_wlan_connection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_network_interfaces_interface_id_wlan_connection_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **int**| The unique identifier of the network interface assigned by the reader. | 
 **network_wlan_connection** | [**NetworkWlanConnection**](NetworkWlanConnection.md)|  | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_power_get**
> PowerConfiguration system_power_get()

Retrieve the current power configuration.

Retrieves the current power configuration on the reader.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current power configuration.
    api_response = api_instance.system_power_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_power_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PowerConfiguration**](PowerConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_power_put**
> StatusResponse system_power_put(power_source)

Configure the power source.

Configures the power source to the specified value for the reader.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
power_source = swagger_client.PowerSource() # PowerSource | The power source to be configured for the reader.

try:
    # Configure the power source.
    api_response = api_instance.system_power_put(power_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_power_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_source** | [**PowerSource**](PowerSource.md)| The power source to be configured for the reader. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_reboot_post**
> StatusResponse system_reboot_post()

Reboot the system.

A call to this endpoint will cause the system to reboot. Once this request is issued, subsequent calls to any endpoint will fail until the system is again available to service requests.  If an upgrade has been installed on the system, the reader will boot into the newly installed firmware image. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Reboot the system.
    api_response = api_instance.system_reboot_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_reboot_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_region_get**
> RegionInfo system_region_get()

Retrieve region information.

Retrieves the current operating region and a list of selectable regions for the reader. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve region information.
    api_response = api_instance.system_region_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_region_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegionInfo**](RegionInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_region_put**
> StatusResponse system_region_put(operating_region)

Configure the operating region.

Configures the reader operating region to the specified region. This operation changes the reader RF settings. The operating region must match the country/region of operation to comply with local laws and regulations. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
operating_region = swagger_client.OperatingRegion() # OperatingRegion | The operating region to be configured for the reader.

try:
    # Configure the operating region.
    api_response = api_instance.system_region_put(operating_region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_region_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operating_region** | [**OperatingRegion**](OperatingRegion.md)| The operating region to be configured for the reader. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_rfid_interface_get**
> RfidInterface system_rfid_interface_get()

Retrieve the reader API.

Retrieves the application programming interface (API) that is currently being used to control the reader RFID operations. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the reader API.
    api_response = api_instance.system_rfid_interface_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_rfid_interface_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RfidInterface**](RfidInterface.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_rfid_interface_put**
> system_rfid_interface_put(rfid_interface)

Configure the reader API.

Configures the application programming interface (API) that will be used to control the reader RFID operations. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
rfid_interface = swagger_client.RfidInterface() # RfidInterface | The API that will be used to control the reader RFID operations.

try:
    # Configure the reader API.
    api_instance.system_rfid_interface_put(rfid_interface)
except ApiException as e:
    print("Exception when calling DefaultApi->system_rfid_interface_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rfid_interface** | [**RfidInterface**](RfidInterface.md)| The API that will be used to control the reader RFID operations. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_rfid_llrp_get**
> LlrpStatus system_rfid_llrp_get()

Retrieve LLRP status.

Retrieves the current status of the LLRP interface.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve LLRP status.
    api_response = api_instance.system_rfid_llrp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_rfid_llrp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LlrpStatus**](LlrpStatus.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_get**
> TimeInfo system_time_get()

Retrieve information about system time and uptime.

Retrieves information about system time and uptime. System time is in UTC and RFC-3339 compliant format. Uptime indicates how long the system has been running in seconds. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve information about system time and uptime.
    api_response = api_instance.system_time_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TimeInfo**](TimeInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_ntp_get**
> InlineResponse200 system_time_ntp_get()

Retrieve the current state of the NTP service.

Retrieves the current state of the NTP (Network Time Protocol) service on the reader. NTP service is responsible for synchronizing the system time on the reader with external NTP servers in order to keep the system time accurate and synchronized with other devices on the network. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the current state of the NTP service.
    api_response = api_instance.system_time_ntp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_ntp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_ntp_put**
> system_time_ntp_put(ntp_configuration)

Configure the NTP service.

Configures the NTP service on the reader.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
ntp_configuration = swagger_client.NtpConfiguration() # NtpConfiguration | The new NTP service configuration.

try:
    # Configure the NTP service.
    api_instance.system_time_ntp_put(ntp_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_ntp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_configuration** | [**NtpConfiguration**](NtpConfiguration.md)| The new NTP service configuration. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_ntp_servers_get**
> list[NtpServer] system_time_ntp_servers_get()

Retrieve NTP servers.

Retrieves NTP servers currently being used on the reader. These servers could be either statically configured or dynamically discovered via a DHCP server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve NTP servers.
    api_response = api_instance.system_time_ntp_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_ntp_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NtpServer]**](NtpServer.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_ntp_servers_post**
> NtpServer system_time_ntp_servers_post(ntp_server)

Add a static NTP server.

Adds a static NTP server to the reader. A NTP server can be specified by either hostname or IP address. The newly created NTP server object is returned upon a successful completion. The reader allows up to 6 static NTP servers. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
ntp_server = swagger_client.NtpServer() # NtpServer | The static NTP server to add.

try:
    # Add a static NTP server.
    api_response = api_instance.system_time_ntp_servers_post(ntp_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_ntp_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_server** | [**NtpServer**](NtpServer.md)| The static NTP server to add. | 

### Return type

[**NtpServer**](NtpServer.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_ntp_servers_server_id_delete**
> NtpServerInfo system_time_ntp_servers_server_id_delete(server_id)

Remove a static NTP server.

Removes a static NTP server from the reader. Note that dynamic NTP servers connot be removed. Both static and dynamic servers could be used together to improve the reliability and accuracy of the system time. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
server_id = 56 # int | The ID of the static NTP server to be removed.

try:
    # Remove a static NTP server.
    api_response = api_instance.system_time_ntp_servers_server_id_delete(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_ntp_servers_server_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| The ID of the static NTP server to be removed. | 

### Return type

[**NtpServerInfo**](NtpServerInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_ntp_servers_server_id_get**
> NtpServerInfo system_time_ntp_servers_server_id_get(server_id)

Retrieve details on a specific NTP server.

Retrieves details on a specific NTP server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
server_id = 56 # int | The unique identifier assigned to the NTP server by the reader.

try:
    # Retrieve details on a specific NTP server.
    api_response = api_instance.system_time_ntp_servers_server_id_get(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_ntp_servers_server_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| The unique identifier assigned to the NTP server by the reader. | 

### Return type

[**NtpServerInfo**](NtpServerInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_time_put**
> system_time_put(system_time)

Update the system time.

Updates the system time if NTP is disabled. If NTP is enabled, an error is returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
system_time = swagger_client.SystemTime() # SystemTime | The new system time to be set in UTC and RFC-3339 format.

try:
    # Update the system time.
    api_instance.system_time_put(system_time)
except ApiException as e:
    print("Exception when calling DefaultApi->system_time_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_time** | [**SystemTime**](SystemTime.md)| The new system time to be set in UTC and RFC-3339 format. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_event_get**
> EventWebhookConfiguration webhooks_event_get()

Get the event webhook configuration.

Gets the event webhook configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get the event webhook configuration.
    api_response = api_instance.webhooks_event_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_event_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventWebhookConfiguration**](EventWebhookConfiguration.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_event_put**
> webhooks_event_put(event_webhook_configuration)

Set the event webhook configuration.

Sets the event webhook configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
event_webhook_configuration = swagger_client.EventWebhookConfiguration() # EventWebhookConfiguration | 

try:
    # Set the event webhook configuration.
    api_instance.webhooks_event_put(event_webhook_configuration)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_event_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_webhook_configuration** | [**EventWebhookConfiguration**](EventWebhookConfiguration.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

