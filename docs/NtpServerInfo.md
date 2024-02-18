# NtpServerInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **int** | The unique identifier assigned to a NTP server by the reader. | 
**server** | **str** | Fully qualified domain name or IP address of the NTP server. Could be either an IPv4 address in dot-decimal format or an IPv6 address compliant with RFC-5952.  | 
**server_type** | **str** | Indicates if this is a static or dynamic NTP server. Static servers are statically added by users. Dynamic servers are those discovered automatically via DHCP servers.  | 
**status** | **str** |  | [optional] 
**poll** | **int** | Shows the rate at which the server is being polled, as a base-2 logarithm of the interval in seconds. Thus, a value of 6 would indicate that a measurement is being made every 64 seconds.  | [optional] 
**stratum** | **int** | Shows the stratum of the server, as reported in its most recently received sample. Stratum 1 indicates a computer with a locally attached reference clock. A computer that is synchronized to a stratum 1 computer is at stratum 2. A computer that is synchronized to a stratum 2 computer is at stratum 3, and so on.  | [optional] 
**reach** | **int** | Shows the server&#39;s reachability register printed as an octal number. The register has 8 bits and is updated on every received or missed packet from the source. A value of 377 indicates that a valid reply was received for all from the last eight transmissions.  | [optional] 
**last_rx** | **str** | Indicates how long ago the last good sample was received from this server. This is normally in seconds. The letters m, h, d or y indicate minutes, hours, days, or years.  | [optional] 
**offset** | **str** | The offset between the local clock and the server at the last measurement. The default measurement unit is in seconds, but it can be suffixed by ns (nanoseconds), us (microseconds), ms (milliseconds) for other measurement units.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


