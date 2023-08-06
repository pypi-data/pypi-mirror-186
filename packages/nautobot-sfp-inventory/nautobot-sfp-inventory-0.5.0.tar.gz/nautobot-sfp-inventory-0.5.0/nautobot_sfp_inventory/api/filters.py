import django_filters
from django.db.models import Q

from nautobot.extras.filters import CustomFieldModelFilterSet, CreatedUpdatedFilterSet
from nautobot_sfp_inventory.models import SFPType, SFP
from nautobot.utilities.filters import BaseFilterSet


class SFPTypeFilterSet(
    BaseFilterSet,
    CustomFieldModelFilterSet,
    CreatedUpdatedFilterSet,
):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(Q(name__icontains=value) | Q(slug__icontains=value) | Q(comments__icontains=value))

    class Meta:
        model = SFPType
        fields = ["id", "name", "slug", "comments"]


class SFPFilterSet(
    BaseFilterSet,
    CustomFieldModelFilterSet,
    CreatedUpdatedFilterSet,
):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(serial_number__icontains=value) | Q(dc_tag__icontains=value) | Q(asset_tag__icontains=value) | Q(
                comments__icontains=value))

    class Meta:
        model = SFP
        fields = [
            "id",
            "serial_number",
            "type",
            "dc_tag",
            "asset_tag",
            "assigned_device",
            "tenant",
            "supplier",
            "procurement_ident",
            "end_of_manufacturer_support",
            "comments"
        ]
