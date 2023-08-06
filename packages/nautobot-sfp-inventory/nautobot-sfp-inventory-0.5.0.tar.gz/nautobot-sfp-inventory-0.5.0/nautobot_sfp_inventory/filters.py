import django_filters
from django.db.models import Q

from nautobot.dcim.models import Device, Manufacturer
from nautobot.extras.filters import CreatedUpdatedFilterSet, CustomFieldModelFilterSet
from .models import SFPType, SFP
from nautobot.utilities.filters import BaseFilterSet, TagFilter
from nautobot.tenancy.models import Tenant


class SFPTypeFilterSet(BaseFilterSet, CreatedUpdatedFilterSet, CustomFieldModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    tag = TagFilter()

    class Meta:
        model = SFPType
        fields = ["id", "name", "slug"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(name__icontains=value) | Q(slug__icontains=value) \
            | Q(comments__icontains=value)
        return queryset.filter(qs_filter)


class SFPFilterSet(BaseFilterSet, CreatedUpdatedFilterSet, CustomFieldModelFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        field_name="tenant",
        queryset=Tenant.objects.all(),
        label="Tenant (ID)",
    )
    tenant = django_filters.ModelMultipleChoiceFilter(
        field_name="tenant__slug",
        queryset=Tenant.objects.all(),
        to_field_name="slug",
        label="Tenant (Slug)",
    )
    type_id = django_filters.ModelMultipleChoiceFilter(
        field_name="type",
        queryset=SFPType.objects.all(),
        label="Type (ID)",
    )
    type = django_filters.ModelMultipleChoiceFilter(
        field_name="type__slug",
        queryset=SFPType.objects.all(),
        to_field_name="slug",
        label="Type (Slug)",
    )
    assigned_device_id = django_filters.ModelMultipleChoiceFilter(
        field_name="assigned_device",
        queryset=Device.objects.all(),
        label="Assigned Device (ID)",
    )
    assigned_device = django_filters.ModelMultipleChoiceFilter(
        field_name="assigned_device__name",
        queryset=Device.objects.all(),
        to_field_name="name",
        label="Assigned Device (Name)",
    )
    supplier_id = django_filters.ModelMultipleChoiceFilter(
        field_name="supplier",
        queryset=Manufacturer.objects.all(),
        label="Manufacturer (ID)",
    )
    supplier = django_filters.ModelMultipleChoiceFilter(
        field_name="supplier__slug",
        queryset=Manufacturer.objects.all(),
        to_field_name="slug",
        label="Manufacturer (Slug)",
    )

    assigned = django_filters.BooleanFilter(
        method="_assigned",
        label="Assigned",
    )

    tag = TagFilter()

    class Meta:
        model = SFP
        fields = ["id", "serial_number", "dc_tag", "asset_tag"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(serial_number__icontains=value) | Q(dc_tag__icontains=value) \
            | Q(asset_tag__icontains=value) | Q(comments__icontains=value)
        return queryset.filter(qs_filter)

    def _assigned(self, queryset, name, value):
        return queryset.filter(assigned=value)
