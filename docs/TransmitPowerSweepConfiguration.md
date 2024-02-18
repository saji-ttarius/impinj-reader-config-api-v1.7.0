# TransmitPowerSweepConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_power_cdbm** | **int** | The minimum power at which the first inventory round  will be performed. If the difference between this value and the antenna&#39;s transmit power is not a multiple of the step size, this value will be rounded up.  This value must be less than or equal to the antenna&#39;s transmit power minus the provided step size.  | 
**step_size_cdb** | **int** | The amount of extra power each successive inventory round should use. If the reader cannot precisely provide this step size, it will round to the nearest possible step size.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


