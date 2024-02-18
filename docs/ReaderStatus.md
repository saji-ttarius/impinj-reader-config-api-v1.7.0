# ReaderStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_preset** | [**ReaderStatusActivePreset**](ReaderStatusActivePreset.md) |  | [optional] 
**status** | **str** | Indicates whether an RFID operation is currenty running on the reader (running), is currently not running an RFID operation, but is waiting to be triggered (armed), or is not running an RFID operation and is not waiting to be triggered (idle).  | [optional] 
**time** | **datetime** | The current, system time on the reader. | [optional] 
**serial_number** | **str** | The serial number of the reader. | [optional] 
**mqtt_broker_connection_status** | **str** | The connection status to the MQTT broker. | [optional] 
**mqtt_tls_authentication** | **str** | The Secure-MQTT authentication and encryption status. \\ none -- server not authenticated, no encryption \\ server -- server authenticated, TLS encryption  | [optional] 
**kafka_cluster_connection_status** | **str** | The connection status to the Kafka cluster. connected -- The device is connected to at least one broker in the Kafka cluster. disconnected -- The device is not connected to any brokers within the Kafka cluster.  | [optional] 
**event_webhook_status** | [**WebhookStatus**](WebhookStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


