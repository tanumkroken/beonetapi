# coding: utf-8

"""
    beoremote_api

    Control Bang Olufsen products supporting the Net Remote TCP/IP protocol. The API provides control Controls are provided for power, audio, input selection, borrowed sources and transport command and polling for product state and currently playing information.   Supported Audio Products:  - BeoPlay M3 - BeoPlay M5 - BeoPlay A6 - BeoPlay A9 MK2  - BeoSound Essence MK2  - BeoSound Core  - BeoSound Moment  - BeoSound 1 - BeoSound 2 - BeoSound 35 - BeoSound Shape - BeoSound Edge  The protocol is also supported by B&O video products, but this is not coverd by the API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: tanumkroken@astrup.info
    Generated by: https://openapi-generator.tech
"""

from beoremote-cli.paths.beo_zone_zone_sound_volume_speaker_muted.get import GetMuteState
from beoremote-cli.paths.beo_zone_zone_sound_volume_speaker_muted.put import PutMuteState


class MuteApi(
    GetMuteState,
    PutMuteState,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
