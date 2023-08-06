from nautobot.extras.plugins import PluginTemplateExtension
from .models import SFP
from .tables import SFPTable


class DeviceSFPTable(PluginTemplateExtension):
    """Template extension to display animal count on the right side of the page."""

    model = 'dcim.device'

    def right_page(self):
        used_sfps = SFP.objects.filter(
            assigned_device=self.context['object']
        )

        used_sfps_table = SFPTable(used_sfps)

        return self.render('nautobot_sfp_inventory/inc/assigned_sfps.html', extra_context={
            'used_sfps_table': used_sfps_table,
        })


template_extensions = [DeviceSFPTable]
