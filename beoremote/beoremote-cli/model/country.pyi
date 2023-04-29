# coding: utf-8

"""
    beoremote_api

    Control Bang Olufsen products supporting the Net Remote TCP/IP protocol. The API provides control Controls are provided for power, audio, input selection, borrowed sources and transport command and polling for product state and currently playing information.   Supported Audio Products:  - BeoPlay M3 - BeoPlay M5 - BeoPlay A6 - BeoPlay A9 MK2  - BeoSound Essence MK2  - BeoSound Core  - BeoSound Moment  - BeoSound 1 - BeoSound 2 - BeoSound 35 - BeoSound Shape - BeoSound Edge  The protocol is also supported by B&O video products, but this is not coverd by the API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: tanumkroken@astrup.info
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from beoremote-cli import schemas  # noqa: F401


class Country(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The product country data.
    """


    class MetaOapg:
        
        class properties:
            country = schemas.StrSchema
            
            
            class _capabilities(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class editable(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'editable':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        
                        
                        class value(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class country(
                                        schemas.ListSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            items = schemas.StrSchema
                                    
                                        def __new__(
                                            cls,
                                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'country':
                                            return super().__new__(
                                                cls,
                                                _arg,
                                                _configuration=_configuration,
                                            )
                                    
                                        def __getitem__(self, i: int) -> MetaOapg.items:
                                            return super().__getitem__(i)
                                    __annotations__ = {
                                        "country": country,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["country", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                country: typing.Union[MetaOapg.properties.country, list, tuple, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'value':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    country=country,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "editable": editable,
                            "value": value,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["editable"]) -> MetaOapg.properties.editable: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["editable", "value", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["editable"]) -> typing.Union[MetaOapg.properties.editable, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["editable", "value", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    editable: typing.Union[MetaOapg.properties.editable, list, tuple, schemas.Unset] = schemas.unset,
                    value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_capabilities':
                    return super().__new__(
                        cls,
                        *_args,
                        editable=editable,
                        value=value,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "country": country,
                "_capabilities": _capabilities,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_capabilities"]) -> MetaOapg.properties._capabilities: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country", "_capabilities", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_capabilities"]) -> typing.Union[MetaOapg.properties._capabilities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country", "_capabilities", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        _capabilities: typing.Union[MetaOapg.properties._capabilities, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Country':
        return super().__new__(
            cls,
            *_args,
            country=country,
            _capabilities=_capabilities,
            _configuration=_configuration,
            **kwargs,
        )