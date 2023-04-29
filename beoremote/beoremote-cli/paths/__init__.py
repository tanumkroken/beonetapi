# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beoremote-cli.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    BEO_NOTIFY_NOTIFICATIONS = "/BeoNotify/Notifications"
    BEO_DEVICE_REGIONAL_SETTINGS = "/BeoDevice/regionalSettings"
    BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_LEVEL = "/BeoZone/Zone/Sound/Volume/Speaker/Level"
    BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_MUTED = "/BeoZone/Zone/Sound/Volume/Speaker/Muted"
    BEO_DEVICE_POWER_MANAGEMENT_STANDBY = "/BeoDevice/powerManagement/standby"
    BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_CONTINUOUS_LEVEL_ACTION = "/BeoZone/Zone/Sound/Volume/Speaker/ContinuousLevelAction"
    BEO_ZONE_ZONE_ACTIVE_SOURCES = "/BeoZone/Zone/ActiveSources"
    BEO_ZONE_ZONE_SOUND_MODE_ACTIVE = "/BeoZone/Zone/Sound/Mode/Active"
    BEO_ZONE_ZONE_SOURCES = "/BeoZone/Zone/Sources"
    BEO_DEVICE_TERMS_AND_CONDITIONS = "/BeoDevice/termsAndConditions"
    BEO_ZONE_ZONE_SOUND_ADJUSTMENT = "/BeoZone/Zone/Sound/Adjustment"
    BEO_ZONE_ZONE_SOURCE_ACTIVATION = "/BeoZone/Zone/SourceActivation"
    BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_DEFAULT_LEVEL = "/BeoZone/Zone/Sound/Volume/Speaker/DefaultLevel"
    BEO_ZONE_ZONE_SOUND_VOLUME_SPEAKER_RANGE = "/BeoZone/Zone/Sound/Volume/Speaker/Range"
    BEO_ZONE_ZONE_SOUND_MODE_1 = "/BeoZone/Zone/Sound/Mode/1"
    BEO_ZONE_ZONE_PLAY_QUEUE_ = "/BeoZone/Zone/PlayQueue/"
    BEO_ZONE_ZONE_STREAM = "/BeoZone/Zone/Stream"
    BEO_ZONE_ZONE_STREAM_PLAY = "/BeoZone/Zone/Stream/Play"
    BEO_ZONE_ZONE_STREAM_PAUSE = "/BeoZone/Zone/Stream/Pause"
    BEO_ZONE_ZONE_STREAM_SKIP = "/BeoZone/Zone/Stream/Skip"
    BEO_ZONE_ZONE_STREAM_NEXT = "/BeoZone/Zone/Stream/Next"
    BEO_ZONE_ZONE_STREAM_STOP = "/BeoZone/Zone/Stream/Stop"
    BEO_ZONE_ZONE_STREAM_FORWARD = "/BeoZone/Zone/Stream/Forward"
    BEO_ZONE_ZONE_STREAM_REWIND = "/BeoZone/Zone/Stream/Rewind"
    BEO_ZONE_ZONE_PLAY_QUEUE = "/BeoZone/Zone/PlayQueue"
    BEO_ZONE_ZONE_ACTIVE_SOURCES_PRIMARY_EXPERIENCE = "/BeoZone/Zone/ActiveSources/primaryExperience"
