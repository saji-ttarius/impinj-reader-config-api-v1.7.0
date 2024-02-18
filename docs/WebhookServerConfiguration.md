# WebhookServerConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to which the webhook will be posted. Supported protocols are \&quot;http\&quot; or \&quot;https\&quot;. For \&quot;https\&quot;, TLSv1.2 and greater are supported.  | 
**port** | **int** | The remote port number to connect to instead of the protocol default.  | [optional] 
**authentication** | [**WebhookHttpAuthentication**](WebhookHttpAuthentication.md) |  | [optional] 
**tls** | [**WebhookTlsConfiguration**](WebhookTlsConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


