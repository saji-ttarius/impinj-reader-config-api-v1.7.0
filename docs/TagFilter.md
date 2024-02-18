# TagFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies if tags matching the provided criteria should be included or excluded from the set. | 
**tag_memory_bank** | **str** | Specifies which memory bank on the tag is of interest. | 
**bit_offset** | **int** | The index into the memory bank where the mask should be applied, in bits. | 
**mask** | **str** | The pattern to match against, specified as a hexadecimal string. | 
**mask_length** | **int** | When the desired mask&#39;s length is not divisible by four, specify how much of the provided mask should be used, in bits. This means the mask is left-justified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


