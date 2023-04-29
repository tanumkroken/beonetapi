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


class TimeZone(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Product time-zone data.
    """


    class MetaOapg:
        
        class properties:
            timeZone = schemas.StrSchema
            inTimeZone = schemas.StrSchema
            __annotations__ = {
                "timeZone": timeZone,
                "inTimeZone": inTimeZone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeZone"]) -> MetaOapg.properties.timeZone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inTimeZone"]) -> MetaOapg.properties.inTimeZone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timeZone", "inTimeZone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeZone"]) -> typing.Union[MetaOapg.properties.timeZone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inTimeZone"]) -> typing.Union[MetaOapg.properties.inTimeZone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timeZone", "inTimeZone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timeZone: typing.Union[MetaOapg.properties.timeZone, str, schemas.Unset] = schemas.unset,
        inTimeZone: typing.Union[MetaOapg.properties.inTimeZone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeZone':
        return super().__new__(
            cls,
            *_args,
            timeZone=timeZone,
            inTimeZone=inTimeZone,
            _configuration=_configuration,
            **kwargs,
        )
