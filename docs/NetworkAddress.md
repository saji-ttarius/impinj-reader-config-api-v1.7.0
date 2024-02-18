# NetworkAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**NetworkProtocol**](NetworkProtocol.md) |  | 
**address_mode** | **str** | The addressing mode for the interface. | 
**address** | **str** | The IP address of the interface. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952. The &#x60;protocol&#x60; property provides the expected network protocol version of the address.  | [optional] 
**prefix** | **int** | The network prefix length of the interface. A typical value is 24 for IPv4 and 64 for IPv6.  | [optional] 
**gateway** | **str** | The gateway address of the interface. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


