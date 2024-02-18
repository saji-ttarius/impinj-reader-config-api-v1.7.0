# KafkaConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Used to enable or disable Kafka output. | [optional] [default to False]
**bootstraps** | [**list[KafkaBootstrapServerConfiguration]**](KafkaBootstrapServerConfiguration.md) | A list of Kafka bootstrap server configurations to connect and push messages to. Device will connect to broker and utilize metadata to determine additional brokers within the cluster that aren&#39;t included in this list.  | 
**client_id** | **str** | A string used to uniquely identify this device to the Kafka broker. | 
**event_topic** | **str** | The base topic where the device will publish events. | 
**partition_key** | **str** | A string specifying the message key, used for partitioning. If this is not specified, will randomly select partition.  | [optional] [default to '']
**event_batch_limit** | **int** | An integer specifying maximum number of events/messages batched in one message set. The eventBatchLingerMilliseconds value and the client&#39;s internal buffer size will impact actual number of messages contained within one message set.  | [optional] 
**event_batch_linger_milliseconds** | **int** | An integer specifying the amount of time, in milliseconds, to wait to send batch messages when eventBatchLimit has not yet been reached. A value of 0 will send each message as it is available.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


