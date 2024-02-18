# StreamConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_buffer_size** | **int** | Number of events that can be stored on the reader waiting for future delivery.  If the bufferSize is 0 then no buffer is created and no history will be saved.  | [optional] 
**event_per_second_limit** | **int** | Maximum number of events that may be delivered per second. This setting can be used to throttle the delivery of events during peak transmission times such as when replaying history during a new connection. Care should be taken to not set this value lower than the normal event generation rate of the reader or the queue attached to the HTTP stream will fill up and events will be purged. A value of Zero (0) means that no eventsPerSecondLimit is applied.  | [optional] 
**event_age_limit_minutes** | **int** | Maximum age of any event in the history buffer.  Any event older than this will be purged automatically from the buffer without the generation of an OverflowEvent.  Use this value to configure the maximum event lifetime for the history buffer.  | [optional] 
**keep_alive_interval_seconds** | **int** | The keep-alive interval in seconds. If no events (or previous keep-alive) have been transmitted in this amount of time a newline (CRLF) will be sent. If this field is updated and no events are available, a keep-alive will be immediately sent.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


