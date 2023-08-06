from nautobot.core.api import WritableNestedSerializer
from nautobot.dcim.api.nested_serializers import NestedManufacturerSerializer, NestedDeviceSerializer
from nautobot.extras.api.customfields import CustomFieldModelSerializer
from nautobot.tenancy.api.nested_serializers import NestedTenantSerializer
from rest_framework import serializers
from nautobot_sfp_inventory.models import SFPType, SFP


class NestedSFPTypeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_sfp_inventory-api:sfptype-detail")

    class Meta:
        model = SFPType
        fields = ["id", "url", "name", "slug", "display"]


class SFPTypeSerializer(CustomFieldModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_sfp_inventory-api:sfptype-detail")

    class Meta:
        model = SFPType
        fields = [
            "id",
            "url",
            "name",
            "slug",
            "display",
            "comments",
            "custom_fields",
            "created",
            "last_updated",
        ]


class SFPSerializer(CustomFieldModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_sfp_inventory-api:sfp-detail")
    tenant = NestedTenantSerializer()
    type = NestedSFPTypeSerializer()
    supplier = NestedManufacturerSerializer(required=False, allow_null=True)
    assigned_device = NestedDeviceSerializer(required=False, allow_null=True)

    class Meta:
        model = SFP
        fields = [
            "id",
            "url",
            "serial_number",
            "display",
            "type",
            "dc_tag",
            "asset_tag",
            "tenant",
            "assigned",
            "assigned_device",
            "supplier",
            "procurement_ident",
            "end_of_manufacturer_support",
            "comments",
            "custom_fields",
            "created",
            "last_updated",
        ]
