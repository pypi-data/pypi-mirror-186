from nautobot.extras.plugins import PluginConfig


class SFPInventoryConfig(PluginConfig):
    name = 'nautobot_sfp_inventory'
    verbose_name = 'SFP Inventory'
    description = 'A plugin for SFP inventory management'
    version = '0.5.0'
    author = "Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen"
    author_email = "netzadmin@gwdg.de"
    base_url = 'nautobot_sfp_inventory'

    def ready(self):
        super().ready()

        from nautobot.core.constants import SEARCH_TYPES
        from nautobot_sfp_inventory.filters import SFPFilterSet, SFPTypeFilterSet
        from nautobot_sfp_inventory.models import SFP, SFPType
        from nautobot_sfp_inventory.tables import SFPTable, SFPTypeTable

        SEARCH_TYPES['sfp'] = {
            "queryset": SFP.objects.all(),
            "filterset": SFPFilterSet,
            "table": SFPTable,
            "url": "plugins:nautobot_sfp_inventory:sfp_list"

        }

        SEARCH_TYPES['sfptype'] = {
            "queryset": SFPType.objects.all(),
            "filterset": SFPTypeFilterSet,
            "table": SFPTypeTable,
            "url": "plugins:nautobot_sfp_inventory:sfptype_list"
        }


config = SFPInventoryConfig
