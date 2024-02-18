# CertificateInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_id** | [**CertificateId**](CertificateId.md) |  | [optional] 
**issuer** | **str** | Identifies the CA that has signed and issued the certificate. | [optional] 
**subject** | **str** | Identifies the entity associated with the public key on the certificate. | [optional] 
**not_before** | **datetime** | The starting date in which the certificate is considered valid. | [optional] 
**not_after** | **datetime** | The ending date in which the certificate is considered valid. | [optional] 
**intended_purposes** | [**list[ExtendedKeyUsage]**](ExtendedKeyUsage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


