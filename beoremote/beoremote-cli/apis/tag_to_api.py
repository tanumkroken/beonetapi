import typing_extensions

from beoremote-cli.apis.tags import TagValues
from beoremote-cli.apis.tags.active_sources_api import ActiveSourcesApi
from beoremote-cli.apis.tags.volume_api import VolumeApi
from beoremote-cli.apis.tags.mute_api import MuteApi
from beoremote-cli.apis.tags.notifications_api import NotificationsApi
from beoremote-cli.apis.tags.power_api import PowerApi
from beoremote-cli.apis.tags.queue_api import QueueApi
from beoremote-cli.apis.tags.settings_api import SettingsApi
from beoremote-cli.apis.tags.sound_api import SoundApi
from beoremote-cli.apis.tags.sources_api import SourcesApi
from beoremote-cli.apis.tags.stream_api import StreamApi
from beoremote-cli.apis.tags.terms_api import TermsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACTIVE_SOURCES: ActiveSourcesApi,
        TagValues.VOLUME: VolumeApi,
        TagValues.MUTE: MuteApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.POWER: PowerApi,
        TagValues.QUEUE: QueueApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.SOUND: SoundApi,
        TagValues.SOURCES: SourcesApi,
        TagValues.STREAM: StreamApi,
        TagValues.TERMS: TermsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACTIVE_SOURCES: ActiveSourcesApi,
        TagValues.VOLUME: VolumeApi,
        TagValues.MUTE: MuteApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.POWER: PowerApi,
        TagValues.QUEUE: QueueApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.SOUND: SoundApi,
        TagValues.SOURCES: SourcesApi,
        TagValues.STREAM: StreamApi,
        TagValues.TERMS: TermsApi,
    }
)
