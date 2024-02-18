# NetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_id** | **int** | A unique identifier of the network interface assigned by the reader. | 
**interface_type** | **str** | Network interface device type. | 
**interface_name** | **str** | The name of the network interface. | 
**status** | **str** | The state of the network interface. | 
**enabled** | **bool** | Indicates whether the interface is enabled or disabled. | 
**network_address** | [**list[NetworkAddress]**](NetworkAddress.md) | The current IPv4 and/or IPv6 network addresses on the interface.  | 
**hardware_address** | **str** | The hardware or MAC address associated with the network interface. | 
**pending** | **bool** | Indicates whether there is a pending configuration that requires a reboot to take effect. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


