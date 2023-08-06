from nautobot.extras.plugins import PluginMenuItem, PluginMenuButton
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(link='plugins:nautobot_sfp_inventory:sfptype_list', link_text="SFP Types", buttons=[
        PluginMenuButton('plugins:nautobot_sfp_inventory:sfptype_add', "Add SFP Type", "mdi mdi-plus-thick",
                         ButtonColorChoices.GREEN),
        PluginMenuButton('plugins:nautobot_sfp_inventory:sfptype_import', "Import SFP Types",
                         "mdi mdi-database-import-outline", ButtonColorChoices.BLUE),
    ]),
    PluginMenuItem(link='plugins:nautobot_sfp_inventory:sfp_list', link_text="SFPs", buttons=[
        PluginMenuButton('plugins:nautobot_sfp_inventory:sfp_add', "Add SFP", "mdi mdi-plus-thick",
                         ButtonColorChoices.GREEN),
        PluginMenuButton('plugins:nautobot_sfp_inventory:sfp_import', "Import SFP",
                         "mdi mdi-database-import-outline", ButtonColorChoices.BLUE),
    ]),
)
