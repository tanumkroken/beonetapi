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


class DayLightSaving(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The product daylight saving data.
    """


    class MetaOapg:
        
        class properties:
            daylightSaving = schemas.StrSchema
            inDaylightSaving = schemas.BoolSchema
            __annotations__ = {
                "daylightSaving": daylightSaving,
                "inDaylightSaving": inDaylightSaving,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["daylightSaving"]) -> MetaOapg.properties.daylightSaving: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inDaylightSaving"]) -> MetaOapg.properties.inDaylightSaving: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["daylightSaving", "inDaylightSaving", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["daylightSaving"]) -> typing.Union[MetaOapg.properties.daylightSaving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inDaylightSaving"]) -> typing.Union[MetaOapg.properties.inDaylightSaving, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["daylightSaving", "inDaylightSaving", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        daylightSaving: typing.Union[MetaOapg.properties.daylightSaving, str, schemas.Unset] = schemas.unset,
        inDaylightSaving: typing.Union[MetaOapg.properties.inDaylightSaving, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DayLightSaving':
        return super().__new__(
            cls,
            *_args,
            daylightSaving=daylightSaving,
            inDaylightSaving=inDaylightSaving,
            _configuration=_configuration,
            **kwargs,
        )
