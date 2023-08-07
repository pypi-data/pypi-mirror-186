from extras.plugins import PluginMenuItem
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


PTUEvent_buttons = [
    PluginMenuButton(
        link='plugins:ptuevents:ptuevent_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
PTUEvent_rel_buttons = [
    PluginMenuButton(
        link='plugins:ptuevents:ptueventrelation_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

appsystem_buttons = [
    PluginMenuButton(
        link='plugins:ptuevents:ptappsystem_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:ptuevents:ptuevent_list',
        link_text='Events',
        buttons=PTUEvent_buttons
    ),
    PluginMenuItem(
        link='plugins:ptuevents:ptueventrelation_list',
        link_text='Event Relations',
        buttons=PTUEvent_rel_buttons
    ),
    PluginMenuItem(
        link='plugins:ptuevents:ptappsystem_list',
        link_text='App Systems',
        buttons=appsystem_buttons
    ),
)
