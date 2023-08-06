from . import serializers, filters
from nautobot.core.api.views import APIRootView
from nautobot.extras.api.views import CustomFieldModelViewSet
from nautobot_sfp_inventory.models import SFPType, SFP


class SFPInventoryRootView(APIRootView):

    def get_view_name(self):
        return "SFP Inventory"


class SFPTypeViewSet(CustomFieldModelViewSet):
    queryset = SFPType.objects.all()
    serializer_class = serializers.SFPTypeSerializer
    filterset_class = filters.SFPTypeFilterSet


class SFPViewSet(CustomFieldModelViewSet):
    queryset = SFP.objects.all()
    serializer_class = serializers.SFPSerializer
    filterset_class = filters.SFPFilterSet
