# InventoryAntennaConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antenna_name** | [**AntennaName**](AntennaName.md) |  | [optional] 
**antenna_port** | [**AntennaPort**](AntennaPort.md) |  | 
**transmit_power_cdbm** | [**TransmitPowerCdbm**](TransmitPowerCdbm.md) |  | 
**rf_mode** | [**RfMode**](RfMode.md) |  | 
**inventory_session** | [**InventorySession**](InventorySession.md) |  | 
**inventory_search_mode** | [**InventorySearchMode**](InventorySearchMode.md) |  | 
**estimated_tag_population** | **int** | The estimated number of tags in the antenna&#39;s field of view. | 
**filtering** | [**InventoryFilterConfiguration**](InventoryFilterConfiguration.md) |  | [optional] 
**power_sweeping** | [**TransmitPowerSweepConfiguration**](TransmitPowerSweepConfiguration.md) |  | [optional] 
**fast_id** | [**FastId**](FastId.md) |  | [optional] 
**protected_mode_pin_hex** | **str** | The PIN used to inventory tags in protected mode. By default, only tags with the specified PIN will respond. If the \&quot;filtering\&quot; property is provided, default behavior will be overridden and tags will respond according to the provided filters regardless of their protected state.  Note: Unprotected tags may also respond if they have the value of the PIN stored in their user memory.  Note: Active filter verification is incompatible with inventory of tags in Protected Mode.  | [optional] 
**receive_sensitivity_dbm** | **int** | The receive sensitivity in dBm. This setting will limit the reported tags to those with an RSSI greater than this value. To have the reader report tags at its greatest sensitivity do not specify this parameter.  | [optional] 
**tag_authentication** | [**TagAuthentication**](TagAuthentication.md) |  | [optional] 
**tag_memory_reads** | [**list[TagMemoryRead]**](TagMemoryRead.md) | When specified, the reader will perform additional access operations and return additional data from the tag, at the cost of slower tag throughput.  | [optional] 
**tag_access_password_hex** | **str** | The tag access password to use when executing access commands that require a password to complete.  If not specified, the value of &#x60;protectedModePinHex&#x60; will be used.  | [optional] 
**tag_access_password_write_hex** | **str** | When specified, the reader will write the access password to all inventoried tags.  The status of this operation will be reported in a TagInventoryEvent.  | [optional] 
**tag_security_modes_write** | [**TagSecurityModes**](TagSecurityModes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


