from nautobot.dcim.choices import CableStatusChoices
from nautobot.extras.plugins import PluginTemplateExtension

from .models import MeasurementLog
from .models import CableTemplate


class CableCommission(PluginTemplateExtension):
    model = 'dcim.cable'

    def buttons(self):
        cable = self.context['object']
        log = None

        maybe_log = MeasurementLog.objects.filter(cable=cable)
        if maybe_log.exists():
            log = maybe_log.first().link

        cable_template = CableTemplate.objects.filter(cable=cable)

        return self.render('nautobot_cable_utils/inc/buttons.html', {
            'cable': cable,
            'cable_planned': cable.status.slug == CableStatusChoices.STATUS_PLANNED,
            'cable_inventory': cable_template.exists(),
            'log': log,
        })


class DeviceBulkConnect(PluginTemplateExtension):
    model = 'dcim.device'

    def buttons(self):
        device = self.context['object']
        cable_available = None

        if device.get_cables().filter(status__slug="planned").count() > 0:
            cable_available = device.get_cables().filter(status__slug="planned").first().pk

        return self.render('nautobot_cable_utils/inc/buttons_device.html', {
            'device': device,
            'cable_planned': cable_available is not None,
        })


class InterfaceAutoRouteStart(PluginTemplateExtension):
    model = "dcim.interface"

    def buttons(self):
        return self.render(
            'nautobot_cable_utils/inc/buttons_interface.html',
        )


class FrontPortAutoRouteStart(PluginTemplateExtension):
    model = "dcim.frontport"

    def buttons(self):
        return self.render(
            'nautobot_cable_utils/inc/buttons_frontport.html',
        )


template_extensions = [CableCommission, DeviceBulkConnect, InterfaceAutoRouteStart, FrontPortAutoRouteStart]
