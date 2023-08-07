from extras.plugins import PluginConfig


class NetBoxPTUEventsConfig(PluginConfig):
    name = 'ptuevents'
    verbose_name = 'Unacceptable events'
    description = 'Add events related fields to devices and virtual machines, adds application systems'
    version = '0.1'
    base_url = 'ptuevents'
    author = 'Oleg Senchenko'
    author_email = 'senchenkoob@mail.ru'


config = NetBoxPTUEventsConfig
