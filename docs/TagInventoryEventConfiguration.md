# TagInventoryEventConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_reporting** | [**TagReportingConfiguration**](TagReportingConfiguration.md) |  | [optional] 
**epc** | **str** | Enable or disable reporting of the epc property. | [optional] [default to 'enabled']
**epc_hex** | **str** | Enable or disable reporting of the epcHex property. | [optional] [default to 'disabled']
**tid** | **str** | Enable or disable reporting of the tid property, fastId must be enabled in an InventoryAntennaConfiguration for tid information to be available for reporting.  | [optional] [default to 'enabled']
**tid_hex** | **str** | Enable or disable reporting of the tidHex property, fastId must be enabled in an InventoryAntennaConfiguration for tid information to be available for reporting.  | [optional] [default to 'disabled']
**xpc_hex** | **str** | Enable or disable reporting Extended Protocol Control words. | [optional] [default to 'disabled']
**antenna_port** | **str** | Enable or disable reporting of the antennaPort. | [optional] [default to 'enabled']
**transmit_power_cdbm** | **str** | Enable or disable reporting of the transmit power. | [optional] [default to 'enabled']
**peak_rssi_cdbm** | **str** | Enable or disable reporting of the peak rssi. | [optional] [default to 'enabled']
**frequency** | **str** | Enable or disable reporting of the frequency. | [optional] [default to 'enabled']
**pc** | **str** | Enable or disable reporting of the PC word. | [optional] [default to 'disabled']
**last_seen_time** | **str** | Enable or disable reporting of lastSeenTime | [optional] [default to 'disabled']
**phase_angle** | **str** | Enable or disable reporting of the phase angle. | [optional] [default to 'disabled']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


