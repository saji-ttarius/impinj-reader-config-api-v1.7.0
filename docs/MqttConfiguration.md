# MqttConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Used to enable or disable MQTT output. | [optional] [default to False]
**broker_hostname** | **str** | The hostname to use for connecting to the MQTT broker. | 
**broker_port** | **int** | The TCP port to use for connecting to the MQTT broker. | [optional] 
**clean_session** | **bool** | This flag is used for determining the client&#39;s session type. When set to &#x60;true&#x60;, the broker will remove all information about this device when it disconnects. When set to &#x60;false&#x60;, the broker considers this device to be a durable client and preserves the appropriate state across client sessions.  | [optional] [default to False]
**client_id** | **str** | A string used to uniquely identify this device to the MQTT broker. This identifier is used for session management, allowing clients to be durable across several disconnects and reconnects.  | 
**event_buffer_size** | **int** | Number of events that can be stored on the reader waiting for delivery to the MQTT broker.  | [optional] 
**event_per_second_limit** | **int** | Maximum number of events that may be delivered per second.  This setting can be used to throttle the delivery of events during peak transmission times such as recovery after a network outage.  Care should be taken to not set this value lower than the normal event generation rate of the reader or the queue will fill up and events will be purged.  A value of Zero (0) means that no eventsPerSecondLimit is applied.  | [optional] 
**event_pending_delivery_limit** | **int** | Maximum number of events concurrently processed by the mqtt delivery layer. When eventQualityOfService is greater than Zero (0) this will limit the rate of delivery to the MQTT broker.  | [optional] 
**event_quality_of_service** | **int** | The QoS level of the MQTT connection. The different levels can be described as follows, according to the MQTT specification:  #### QoS 0: At most once delivery  The message is delivered according to the capabilities of the underlying network. No response is sent by the receiver and no retry is performed by the sender. The message arrives at the receiver either once or not at all.  #### QoS 1: At least once delivery  This quality of service ensures that the message arrives at the receiver at least once, possibly multiple times.  #### QoS 2: Exactly once delivery  This is the highest quality of service, for use when neither loss nor duplication of messages are acceptable. There is an increased overhead associated with this quality of service.  | [optional] 
**event_topic** | **str** | The base topic where the device will publish events. | 
**keep_alive_interval_seconds** | **int** | Specifies how often the device should check-in with the broker by sending a control packet. From the MQTT specification:  &gt; If the Keep Alive value is non-zero and the Server does not receive a Control Packet &gt; from the Client within one and a half times the Keep Alive time period, it MUST &gt; disconnect the Network Connection to the Client as if the network had failed.  | [optional] 
**tls_enabled** | **bool** | Specifies whether MQTT client should initiate secure connections to the broker. When set to &#x60;true&#x60;, CA certificate(s) that signed the broker&#39;s server certificate must be installed on the reader to allow for server authentication unless the server certificate could be traced back to a well-known root CA pre-installed on the reader.  | [optional] [default to False]
**username** | **str** | The username to use when authenticating with the broker. | [optional] [default to '']
**password** | **str** | The password to use when authenticating with the broker. | [optional] [default to '']
**will_topic** | **str** | The topic to which status messages are sent. If this parameter is unset or an empty string, no status messages will be sent. See &#x60;willMessage&#x60;, &#x60;connectMessage&#x60;, and &#x60;disconnectMessage&#x60; (the status messages).  | [optional] [default to '']
**will_message** | **str** | The status message to be sent by the broker to the &#x60;willTopic&#x60; if the reader disconnects ungracefully. This normally means something unusual has happened such a power outage, network error, or firmware error.  | [optional] [default to 'connection lost']
**will_quality_of_service** | **int** | The Quality of Service (QoS) of status messages. See &#x60;willMessage&#x60;, &#x60;connectMessage&#x60;, and &#x60;disconnectMessage&#x60; (the status messages). See &#x60;eventQualityOfService&#x60; for details on how the different quality of service levels affect message transmission.  | [optional] 
**connect_message** | **str** | The status message to send to the &#x60;willTopic&#x60; when the reader connects or reconnects to the broker.  | [optional] [default to 'connected']
**disconnect_message** | **str** | The status message to send to the &#x60;willTopic&#x60; when the reader disconnects from the broker gracefully. A graceful disconnect includes disabling the IoT Interface, disabling MQTT output, or rebooting the reader.  | [optional] [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


