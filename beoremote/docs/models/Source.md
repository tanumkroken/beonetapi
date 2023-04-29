# beoremote-cli.model.source.Source

The product source data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The product source data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**friendlyName** | str,  | str,  |  | [optional] 
**[sourceType](#sourceType)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**category** | str,  | str,  |  | [optional] 
**inUse** | bool,  | BoolClass,  |  | [optional] 
**profile** | str,  | str,  |  | [optional] 
**linkable** | bool,  | BoolClass,  |  | [optional] 
**recommendedIrMapping** | [**RecommendedIrMapping**](RecommendedIrMapping.md) | [**RecommendedIrMapping**](RecommendedIrMapping.md) |  | [optional] 
**contentProtection** | [**ContentProtection**](ContentProtection.md) | [**ContentProtection**](ContentProtection.md) |  | [optional] 
**embeddedBinary** | [**EmbeddedBinary**](EmbeddedBinary.md) | [**EmbeddedBinary**](EmbeddedBinary.md) |  | [optional] 
**product** | [**Product**](Product.md) | [**Product**](Product.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sourceType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

