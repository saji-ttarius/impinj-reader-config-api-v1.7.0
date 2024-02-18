# TagInventoryEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epc** | [**Epc**](Epc.md) |  | [optional] 
**epc_hex** | [**EpcHex**](EpcHex.md) |  | [optional] 
**tid** | [**Tid**](Tid.md) |  | [optional] 
**tid_hex** | [**TidHex**](TidHex.md) |  | [optional] 
**xpc_hex** | [**XpcHex**](XpcHex.md) |  | [optional] 
**antenna_port** | [**AntennaPort**](AntennaPort.md) |  | [optional] 
**antenna_name** | [**AntennaName**](AntennaName.md) |  | [optional] 
**transmit_power_cdbm** | [**TransmitPowerCdbm**](TransmitPowerCdbm.md) |  | [optional] 
**peak_rssi_cdbm** | **int** | The peak received power of the EPC backscatter in cdBm. We will give the client the opportunity to enable Impinj&#39;s high-precision mode to receive more accurate data.  | [optional] 
**frequency** | **int** | The frequency that was used to read the tag, in kHz. | [optional] 
**pc** | **str** | The PC word (16-bits) backscattered by the inventoried tag. | [optional] 
**last_seen_time** | **datetime** | The UTC time at which the tag was last seen.  | [optional] 
**phase_angle** | **float** | The phase angle in degrees of the tag that was read, accurate to two decimal places.  | [optional] 
**tag_access_password_write_response** | [**TagModificationResponse**](TagModificationResponse.md) |  | [optional] 
**tag_security_modes_write_response** | [**TagModificationResponse**](TagModificationResponse.md) |  | [optional] 
**tag_authentication_response** | [**TagAuthenticationResponse**](TagAuthenticationResponse.md) |  | [optional] 
**tag_memory_data** | [**list[TagMemoryData]**](TagMemoryData.md) | This array will be provided if the tagMemoryReads parameter is specified for the &#x60;InventoryAntennaConfiguration&#x60; for the antenna generating this event.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


