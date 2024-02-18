# IpConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_mode** | **str** | The addressing mode used for this interface. If the &#x60;addressMode&#x60; is set to &#x60;dynamic&#x60;, the optional &#x60;staticAddress&#x60;, &#x60;staticPrefix&#x60;, and &#x60;staticGateway&#x60; provided with the request will be saved on the reader, but not used.  When the &#x60;addressMode&#x60; is set to &#x60;static&#x60;, the values for &#x60;staticAddress&#x60;, &#x60;staticPrefix&#x60;, and &#x60;staticGateway&#x60; will be used for the network interface configuration. If the values for those fields are not provided with the request, the previously set values will be used. If no values are found for &#39;staticAddress&#39; and &#x60;staticPrefix&#x60;, an error response will be returned. If no value for &#39;staticGateway&#39; is found, the reader&#39;s gateway will not be configured and the reader can only be accessed within the local network.  | 
**static_address** | **str** | The IP address to use when addressMode is set to &#x60;static&#x60;. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952.  | [optional] 
**static_prefix** | **int** | The network prefix length to use when addressMode is set to &#x60;static&#x60;. A typical value is 24 for IPv4 and 64 for IPv6.  | [optional] 
**static_gateway** | **str** | The gateway to use when the &#x60;addressMode&#x60; is set to &#x60;static&#x60;. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


