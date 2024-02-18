# EventWebhookConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Used to enable or disable webhook publishing. | [optional] [default to False]
**server_configuration** | [**WebhookServerConfiguration**](WebhookServerConfiguration.md) |  | [optional] 
**retry** | [**WebhookRetryConfiguration**](WebhookRetryConfiguration.md) |  | [optional] 
**event_batch_limit** | **int** | The max number of events sent in a batch.  | [optional] 
**event_batch_linger_milliseconds** | **int** | The next batch will be sent when the linger time has elapsed since the last batch was sent successfully. If no events have queued for delivery when the linger time elapses, an empty batch will be sent.  | [optional] 
**event_buffer_size** | **int** | The minimum number of events that will be queued on the reader waiting for delivery. When the queue exceeds this size, events will periodically be purged and an \&quot;OverflowEvent\&quot; will be inserted into the queue in place of the purged events.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


