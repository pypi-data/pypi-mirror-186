from . import serializers, filters
from nautobot.core.api.views import APIRootView, ModelViewSet
from ..models import CableTemplate, CablePlug


class SFPInventoryRootView(APIRootView):

    def get_view_name(self):
        return "SFP Inventory"


class CableTemplateViewSet(ModelViewSet):
    queryset = CableTemplate.objects.all()
    serializer_class = serializers.CableTemplateSerializer
    filterset_class = filters.CableTemplateFilterSet


class CablePlugViewSet(ModelViewSet):
    queryset = CablePlug.objects.all()
    serializer_class = serializers.CablePlugSerializer
    filterset_class = filters.CablePlugFilterSet
