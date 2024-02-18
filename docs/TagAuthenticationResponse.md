# TagAuthenticationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_hex** | **str** | The challenge message that was sent to the tag. | [optional] 
**response_hex** | **str** | The authentication response that was received from the tag. If a value other than success was received from the tag, responseHex will contain an empty string.  | 
**tid_hex** | **str** | Present if 64 bits of TID information, which excludes TID words 0 and 2, was returned with the authentication response received from the tag.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


