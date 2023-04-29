import typing_extensions

from beoremote-cli.paths import PathValues
from beoremote-cli.apis.paths.beo_notify_notifications import BeoNotifyNotifications
from beoremote-cli.apis.paths.beo_device_regional_settings import BeoDeviceRegionalSettings
from beoremote-cli.apis.paths.beo_zone_zone_sound_volume_speaker_level import BeoZoneZoneSoundVolumeSpeakerLevel
from beoremote-cli.apis.paths.beo_zone_zone_sound_volume_speaker_muted import BeoZoneZoneSoundVolumeSpeakerMuted
from beoremote-cli.apis.paths.beo_device_power_management_standby import BeoDevicePowerManagementStandby
from beoremote-cli.apis.paths.beo_zone_zone_sound_volume_speaker_continuous_level_action import BeoZoneZoneSoundVolumeSpeakerContinuousLevelAction
from beoremote-cli.apis.paths.beo_zone_zone_active_sources import BeoZoneZoneActiveSources
from beoremote-cli.apis.paths.beo_zone_zone_sound_mode_active import BeoZoneZoneSoundModeActive
from beoremote-cli.apis.paths.beo_zone_zone_sources import BeoZoneZoneSources
from beoremote-cli.apis.paths.beo_device_terms_and_conditions import BeoDeviceTermsAndConditions
from beoremote-cli.apis.paths.beo_zone_zone_sound_adjustment import BeoZoneZoneSoundAdjustment
from beoremote-cli.apis.paths.beo_zone_zone_source_activation import BeoZoneZoneSourceActivation
from beoremote-cli.apis.paths.beo_zone_zone_sound_volume_speaker_default_level import BeoZoneZoneSoundVolumeSpeakerDefaultLevel
from beoremote-cli.apis.paths.beo_zone_zone_sound_volume_speaker_range import BeoZoneZoneSoundVolumeSpeakerRange
from beoremote-cli.apis.paths.beo_zone_zone_sound_mode_1 import BeoZoneZoneSoundMode1
from beoremote-cli.apis.paths.beo_zone_zone_play_queue_ import BeoZoneZonePlayQueue
from beoremote-cli.apis.paths.beo_zone_zone_stream import BeoZoneZoneStream
from beoremote-cli.apis.paths.beo_zone_zone_stream_play import BeoZoneZoneStreamPlay
from beoremote-cli.apis.paths.beo_zone_zone_stream_pause import BeoZoneZoneStreamPause
from beoremote-cli.apis.paths.beo_zone_zone_stream_skip import BeoZoneZoneStreamSkip
from beoremote-cli.apis.paths.beo_zone_zone_stream_next import BeoZoneZoneStreamNext
from beoremote-cli.apis.paths.beo_zone_zone_stream_stop import BeoZoneZoneStreamStop
from beoremote-cli.apis.paths.beo_zone_zone_stream_forward import BeoZoneZoneStreamForward
from beoremote-cli.apis.paths.beo_zone_zone_stream_rewind import BeoZoneZoneStreamRewind
from beoremote-cli.apis.paths.beo_zone_zone_play_queue import BeoZoneZonePlayQueue
from beoremote-cli.apis.paths.beo_zone_zone_active_sources_primary_experience import BeoZoneZoneActiveSourcesPrimaryExperience

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.BEO_NOTIFY_NOTIFICATIONS: BeoNotifyNotifications,
        PathValues.BEO_DEVICE_REGIONAL_SETTINGS: BeoDeviceRegionalSettings,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_LEVEL: BeoZoneZoneSoundVolumeSpeakerLevel,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_MUTED: BeoZoneZoneSoundVolumeSpeakerMuted,
        PathValues.BEO_DEVICE_POWER_MANAGEMENT_STANDBY: BeoDevicePowerManagementStandby,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_CONTINUOUS_LEVEL_ACTION: BeoZoneZoneSoundVolumeSpeakerContinuousLevelAction,
        PathValues.BEO_ZONE_ZONE_ACTIVE_SOURCES: BeoZoneZoneActiveSources,
        PathValues.BEO_ZONE_ZONE_SOUND_MODE_ACTIVE: BeoZoneZoneSoundModeActive,
        PathValues.BEO_ZONE_ZONE_SOURCES: BeoZoneZoneSources,
        PathValues.BEO_DEVICE_TERMS_AND_CONDITIONS: BeoDeviceTermsAndConditions,
        PathValues.BEO_ZONE_ZONE_SOUND_ADJUSTMENT: BeoZoneZoneSoundAdjustment,
        PathValues.BEO_ZONE_ZONE_SOURCE_ACTIVATION: BeoZoneZoneSourceActivation,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_DEFAULT_LEVEL: BeoZoneZoneSoundVolumeSpeakerDefaultLevel,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_RANGE: BeoZoneZoneSoundVolumeSpeakerRange,
        PathValues.BEO_ZONE_ZONE_SOUND_MODE_1: BeoZoneZoneSoundMode1,
        PathValues.BEO_ZONE_ZONE_PLAY_QUEUE_: BeoZoneZonePlayQueue,
        PathValues.BEO_ZONE_ZONE_STREAM: BeoZoneZoneStream,
        PathValues.BEO_ZONE_ZONE_STREAM_PLAY: BeoZoneZoneStreamPlay,
        PathValues.BEO_ZONE_ZONE_STREAM_PAUSE: BeoZoneZoneStreamPause,
        PathValues.BEO_ZONE_ZONE_STREAM_SKIP: BeoZoneZoneStreamSkip,
        PathValues.BEO_ZONE_ZONE_STREAM_NEXT: BeoZoneZoneStreamNext,
        PathValues.BEO_ZONE_ZONE_STREAM_STOP: BeoZoneZoneStreamStop,
        PathValues.BEO_ZONE_ZONE_STREAM_FORWARD: BeoZoneZoneStreamForward,
        PathValues.BEO_ZONE_ZONE_STREAM_REWIND: BeoZoneZoneStreamRewind,
        PathValues.BEO_ZONE_ZONE_PLAY_QUEUE: BeoZoneZonePlayQueue,
        PathValues.BEO_ZONE_ZONE_ACTIVE_SOURCES_PRIMARY_EXPERIENCE: BeoZoneZoneActiveSourcesPrimaryExperience,
    }
)

path_to_api = PathToApi(
    {
        PathValues.BEO_NOTIFY_NOTIFICATIONS: BeoNotifyNotifications,
        PathValues.BEO_DEVICE_REGIONAL_SETTINGS: BeoDeviceRegionalSettings,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_LEVEL: BeoZoneZoneSoundVolumeSpeakerLevel,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_MUTED: BeoZoneZoneSoundVolumeSpeakerMuted,
        PathValues.BEO_DEVICE_POWER_MANAGEMENT_STANDBY: BeoDevicePowerManagementStandby,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_CONTINUOUS_LEVEL_ACTION: BeoZoneZoneSoundVolumeSpeakerContinuousLevelAction,
        PathValues.BEO_ZONE_ZONE_ACTIVE_SOURCES: BeoZoneZoneActiveSources,
        PathValues.BEO_ZONE_ZONE_SOUND_MODE_ACTIVE: BeoZoneZoneSoundModeActive,
        PathValues.BEO_ZONE_ZONE_SOURCES: BeoZoneZoneSources,
        PathValues.BEO_DEVICE_TERMS_AND_CONDITIONS: BeoDeviceTermsAndConditions,
        PathValues.BEO_ZONE_ZONE_SOUND_ADJUSTMENT: BeoZoneZoneSoundAdjustment,
        PathValues.BEO_ZONE_ZONE_SOURCE_ACTIVATION: BeoZoneZoneSourceActivation,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_DEFAULT_LEVEL: BeoZoneZoneSoundVolumeSpeakerDefaultLevel,
        PathValues.BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_RANGE: BeoZoneZoneSoundVolumeSpeakerRange,
        PathValues.BEO_ZONE_ZONE_SOUND_MODE_1: BeoZoneZoneSoundMode1,
        PathValues.BEO_ZONE_ZONE_PLAY_QUEUE_: BeoZoneZonePlayQueue,
        PathValues.BEO_ZONE_ZONE_STREAM: BeoZoneZoneStream,
        PathValues.BEO_ZONE_ZONE_STREAM_PLAY: BeoZoneZoneStreamPlay,
        PathValues.BEO_ZONE_ZONE_STREAM_PAUSE: BeoZoneZoneStreamPause,
        PathValues.BEO_ZONE_ZONE_STREAM_SKIP: BeoZoneZoneStreamSkip,
        PathValues.BEO_ZONE_ZONE_STREAM_NEXT: BeoZoneZoneStreamNext,
        PathValues.BEO_ZONE_ZONE_STREAM_STOP: BeoZoneZoneStreamStop,
        PathValues.BEO_ZONE_ZONE_STREAM_FORWARD: BeoZoneZoneStreamForward,
        PathValues.BEO_ZONE_ZONE_STREAM_REWIND: BeoZoneZoneStreamRewind,
        PathValues.BEO_ZONE_ZONE_PLAY_QUEUE: BeoZoneZonePlayQueue,
        PathValues.BEO_ZONE_ZONE_ACTIVE_SOURCES_PRIMARY_EXPERIENCE: BeoZoneZoneActiveSourcesPrimaryExperience,
    }
)
