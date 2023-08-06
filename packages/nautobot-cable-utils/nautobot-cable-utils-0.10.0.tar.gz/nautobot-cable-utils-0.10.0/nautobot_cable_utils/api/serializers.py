from rest_framework.serializers import ModelSerializer

from nautobot.core.api import BaseModelSerializer
from nautobot.dcim.api.nested_serializers import NestedCableSerializer, NestedManufacturerSerializer
from nautobot.extras.api.customfields import CustomFieldModelSerializer
from nautobot.tenancy.api.nested_serializers import NestedTenantSerializer
from rest_framework import serializers

from nautobot_cable_utils.models import CableTemplate, CablePlug


class NestedCablePlugSerializer(BaseModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_cable_utils-api:cableplug-detail")

    class Meta:
        model = CablePlug
        fields = ["id", "url", "name"]


class CablePlugSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_cable_utils-api:cableplug-detail")

    class Meta:
        model = CablePlug
        fields = [
            "id",
            "url",
            "name",
            "display",
        ]


class CableTemplateSerializer(CustomFieldModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_cable_utils-api:cabletemplate-detail")
    owner = NestedTenantSerializer()
    cable = NestedCableSerializer()
    plug = NestedCablePlugSerializer()
    supplier = NestedManufacturerSerializer()

    class Meta:
        model = CableTemplate
        fields = [
            "id",
            "url",
            "name",
            "display",
            "label",
            "type",
            "plug",
            "color",
            "supplier",
            "procurement_ident",
            "length",
            "length_unit",
            "cable",
            "owner",
        ]
