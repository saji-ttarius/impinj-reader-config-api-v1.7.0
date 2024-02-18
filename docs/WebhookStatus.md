# WebhookStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The general status of the webhook. The \&quot;pending\&quot; state indicates that the webhook is active, but has not published since being enabled or since the last reader reboot. The \&quot;http-error\&quot; state occurs if the server replied with an error code. The \&quot;network-error\&quot; state indicates that the server could not be reached.  | 
**http_status_code** | **int** | The HTTP status code of the most recent webhook request to the server. This property will be absent if the webhook is pending, disabled or experiencing a network error.  | [optional] 
**timestamp** | **datetime** | The time at which the last request was attempted. This property will be absent if the webhook is pending or disabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


