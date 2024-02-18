# TagReportingConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reporting_interval_seconds** | **int** | The reporting interval is the duration after which a tag persisting in the field of view is reported again. Set to zero to disable the feature.  | [optional] 
**tag_cache_size** | **int** | The maximum number of unique tags expected in the field of view during the reporting interval.  | [optional] 
**antenna_identifier** | **str** | TagInventoryEvent field to use to identify antenna. | [optional] [default to 'antennaPort']
**tag_identifier** | **str** | TagInventoryEvent field to use to identify unique tag. | [optional] [default to 'epc']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


