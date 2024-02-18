# InventoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_config** | [**InventoryEventConfiguration**](InventoryEventConfiguration.md) |  | [optional] 
**antenna_configs** | [**list[InventoryAntennaConfiguration]**](InventoryAntennaConfiguration.md) |  | 
**channel_frequencies_khz** | **list[int]** | For non frequency hopping regions that allow the choice of operating frequency, this array contains the sequence of frequencies to use. Permissible values are region-dependent and will be included in the JSON schema produced by the reader.  | [optional] 
**start_triggers** | [**list[InventoryStartTrigger]**](InventoryStartTrigger.md) | This property contains an array of triggers that will start the inventory. If any triggers are specified, then the RFID operation will transition to the ARMED state.  When the reader is in the ARMED state, a trigger will transition the reader to the RUNNING state and begin the inventory.  | [optional] 
**stop_triggers** | [**list[InventoryStopTrigger]**](InventoryStopTrigger.md) | This property contains an array of triggers that will stop the inventory.  When the reader is in the RUNNING state, a trigger will transition the reader to the ARMED state and stop the inventory.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


