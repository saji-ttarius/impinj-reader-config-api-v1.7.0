# ReaderEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The hostname of the reader that generated this event. | [optional] 
**event_type** | **str** | The type of the event, should be the same as the name of the property that contains the event with the string \&quot;Event\&quot; stripped off.  For example an event with an eventType of \&quot;tagInventory\&quot; will contain the \&quot;tagInventoryEvent\&quot; property. | 
**timestamp** | **datetime** | The UTC time at which the event was processed and queued for delivery.  | 
**tag_inventory_event** | [**TagInventoryEvent**](TagInventoryEvent.md) |  | [optional] 
**antenna_connected_event** | [**AntennaConnectedEvent**](AntennaConnectedEvent.md) |  | [optional] 
**antenna_disconnected_event** | [**AntennaDisconnectedEvent**](AntennaDisconnectedEvent.md) |  | [optional] 
**inventory_status_event** | [**InventoryStatusEvent**](InventoryStatusEvent.md) |  | [optional] 
**antenna_activation_event** | [**AntennaActivationEvent**](AntennaActivationEvent.md) |  | [optional] 
**overflow_event** | [**OverflowEvent**](OverflowEvent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


