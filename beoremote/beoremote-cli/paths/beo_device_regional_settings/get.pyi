# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from beoremote-cli import api_client, exceptions
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

from beoremote-cli.model.language import Language
from beoremote-cli.model.country import Country
from beoremote-cli.model.day_light_saving import DayLightSaving
from beoremote-cli.model.date_time import DateTime
from beoremote-cli.model.date_time_mode import DateTimeMode
from beoremote-cli.model.region import Region



class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class profile(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        name = schemas.StrSchema
                        version = schemas.IntSchema
                        
                        
                        class _links(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class _self(
                                        schemas.DictSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            class properties:
                                                href = schemas.StrSchema
                                                __annotations__ = {
                                                    "href": href,
                                                }
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["href", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *_args: typing.Union[dict, frozendict.frozendict, ],
                                            href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> '_self':
                                            return super().__new__(
                                                cls,
                                                *_args,
                                                href=href,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                                    __annotations__ = {
                                        "self": _self,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["self", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["self", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> '_links':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class regionalSettings(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                
                                    @staticmethod
                                    def dateTime() -> typing.Type['DateTime']:
                                        return DateTime
                                
                                    @staticmethod
                                    def dateTimeMode() -> typing.Type['DateTimeMode']:
                                        return DateTimeMode
                                
                                    @staticmethod
                                    def daylightSaving() -> typing.Type['DayLightSaving']:
                                        return DayLightSaving
                                
                                    @staticmethod
                                    def timeZone() -> typing.Type['DayLightSaving']:
                                        return DayLightSaving
                                
                                    @staticmethod
                                    def country() -> typing.Type['Country']:
                                        return Country
                                
                                    @staticmethod
                                    def region() -> typing.Type['Region']:
                                        return Region
                                
                                    @staticmethod
                                    def language() -> typing.Type['Language']:
                                        return Language
                                    __annotations__ = {
                                        "dateTime": dateTime,
                                        "dateTimeMode": dateTimeMode,
                                        "daylightSaving": daylightSaving,
                                        "timeZone": timeZone,
                                        "country": country,
                                        "region": region,
                                        "language": language,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> 'DateTime': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["dateTimeMode"]) -> 'DateTimeMode': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["daylightSaving"]) -> 'DayLightSaving': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["timeZone"]) -> 'DayLightSaving': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'Country': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["region"]) -> 'Region': ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["language"]) -> 'Language': ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["dateTime", "dateTimeMode", "daylightSaving", "timeZone", "country", "region", "language", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union['DateTime', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["dateTimeMode"]) -> typing.Union['DateTimeMode', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["daylightSaving"]) -> typing.Union['DayLightSaving', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["timeZone"]) -> typing.Union['DayLightSaving', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union['Country', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union['Region', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union['Language', schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dateTime", "dateTimeMode", "daylightSaving", "timeZone", "country", "region", "language", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                dateTime: typing.Union['DateTime', schemas.Unset] = schemas.unset,
                                dateTimeMode: typing.Union['DateTimeMode', schemas.Unset] = schemas.unset,
                                daylightSaving: typing.Union['DayLightSaving', schemas.Unset] = schemas.unset,
                                timeZone: typing.Union['DayLightSaving', schemas.Unset] = schemas.unset,
                                country: typing.Union['Country', schemas.Unset] = schemas.unset,
                                region: typing.Union['Region', schemas.Unset] = schemas.unset,
                                language: typing.Union['Language', schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'regionalSettings':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    dateTime=dateTime,
                                    dateTimeMode=dateTimeMode,
                                    daylightSaving=daylightSaving,
                                    timeZone=timeZone,
                                    country=country,
                                    region=region,
                                    language=language,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "name": name,
                            "version": version,
                            "_links": _links,
                            "regionalSettings": regionalSettings,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["regionalSettings"]) -> MetaOapg.properties.regionalSettings: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "version", "_links", "regionalSettings", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["regionalSettings"]) -> typing.Union[MetaOapg.properties.regionalSettings, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "version", "_links", "regionalSettings", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    version: typing.Union[MetaOapg.properties.version, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    regionalSettings: typing.Union[MetaOapg.properties.regionalSettings, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'profile':
                    return super().__new__(
                        cls,
                        *_args,
                        name=name,
                        version=version,
                        _links=_links,
                        regionalSettings=regionalSettings,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "profile": profile,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile"]) -> MetaOapg.properties.profile: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["profile", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile"]) -> typing.Union[MetaOapg.properties.profile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["profile", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        profile: typing.Union[MetaOapg.properties.profile, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            profile=profile,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_region_settings_oapg(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_region_settings_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_region_settings_oapg(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_region_settings_oapg(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Product Regional Settings
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetRegionSettings(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_region_settings(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_region_settings(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_region_settings(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_region_settings(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_region_settings_oapg(
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_region_settings_oapg(
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

