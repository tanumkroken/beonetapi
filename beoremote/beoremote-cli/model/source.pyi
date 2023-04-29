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


class Source(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The product source data.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            friendlyName = schemas.StrSchema
            
            
            class sourceType(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        type = schemas.StrSchema
                        __annotations__ = {
                            "type": type,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sourceType':
                    return super().__new__(
                        cls,
                        *_args,
                        type=type,
                        _configuration=_configuration,
                        **kwargs,
                    )
            category = schemas.StrSchema
            inUse = schemas.BoolSchema
            profile = schemas.StrSchema
            linkable = schemas.BoolSchema
        
            @staticmethod
            def recommendedIrMapping() -> typing.Type['RecommendedIrMapping']:
                return RecommendedIrMapping
        
            @staticmethod
            def contentProtection() -> typing.Type['ContentProtection']:
                return ContentProtection
        
            @staticmethod
            def embeddedBinary() -> typing.Type['EmbeddedBinary']:
                return EmbeddedBinary
        
            @staticmethod
            def product() -> typing.Type['Product']:
                return Product
            __annotations__ = {
                "id": id,
                "friendlyName": friendlyName,
                "sourceType": sourceType,
                "category": category,
                "inUse": inUse,
                "profile": profile,
                "linkable": linkable,
                "recommendedIrMapping": recommendedIrMapping,
                "contentProtection": contentProtection,
                "embeddedBinary": embeddedBinary,
                "product": product,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["friendlyName"]) -> MetaOapg.properties.friendlyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceType"]) -> MetaOapg.properties.sourceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inUse"]) -> MetaOapg.properties.inUse: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile"]) -> MetaOapg.properties.profile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkable"]) -> MetaOapg.properties.linkable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommendedIrMapping"]) -> 'RecommendedIrMapping': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentProtection"]) -> 'ContentProtection': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["embeddedBinary"]) -> 'EmbeddedBinary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product"]) -> 'Product': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "friendlyName", "sourceType", "category", "inUse", "profile", "linkable", "recommendedIrMapping", "contentProtection", "embeddedBinary", "product", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["friendlyName"]) -> typing.Union[MetaOapg.properties.friendlyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceType"]) -> typing.Union[MetaOapg.properties.sourceType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inUse"]) -> typing.Union[MetaOapg.properties.inUse, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile"]) -> typing.Union[MetaOapg.properties.profile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkable"]) -> typing.Union[MetaOapg.properties.linkable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommendedIrMapping"]) -> typing.Union['RecommendedIrMapping', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentProtection"]) -> typing.Union['ContentProtection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["embeddedBinary"]) -> typing.Union['EmbeddedBinary', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product"]) -> typing.Union['Product', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "friendlyName", "sourceType", "category", "inUse", "profile", "linkable", "recommendedIrMapping", "contentProtection", "embeddedBinary", "product", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        friendlyName: typing.Union[MetaOapg.properties.friendlyName, str, schemas.Unset] = schemas.unset,
        sourceType: typing.Union[MetaOapg.properties.sourceType, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        inUse: typing.Union[MetaOapg.properties.inUse, bool, schemas.Unset] = schemas.unset,
        profile: typing.Union[MetaOapg.properties.profile, str, schemas.Unset] = schemas.unset,
        linkable: typing.Union[MetaOapg.properties.linkable, bool, schemas.Unset] = schemas.unset,
        recommendedIrMapping: typing.Union['RecommendedIrMapping', schemas.Unset] = schemas.unset,
        contentProtection: typing.Union['ContentProtection', schemas.Unset] = schemas.unset,
        embeddedBinary: typing.Union['EmbeddedBinary', schemas.Unset] = schemas.unset,
        product: typing.Union['Product', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Source':
        return super().__new__(
            cls,
            *_args,
            id=id,
            friendlyName=friendlyName,
            sourceType=sourceType,
            category=category,
            inUse=inUse,
            profile=profile,
            linkable=linkable,
            recommendedIrMapping=recommendedIrMapping,
            contentProtection=contentProtection,
            embeddedBinary=embeddedBinary,
            product=product,
            _configuration=_configuration,
            **kwargs,
        )

from beoremote-cli.model.content_protection import ContentProtection
from beoremote-cli.model.embedded_binary import EmbeddedBinary
from beoremote-cli.model.product import Product
from beoremote-cli.model.recommended_ir_mapping import RecommendedIrMapping