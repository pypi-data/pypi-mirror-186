from django.db.models import Q, Count
from django.urls import reverse

from nautobot.core.views import generic
from . import tables, forms
from .models import SFPType, SFP
from .filters import SFPTypeFilterSet, SFPFilterSet
from .tables import SFPTable, SFPByTenantTable, SFPBySupplierTable


class SFPTypeListView(generic.ObjectListView):
    queryset = SFPType.objects.annotate(
        unassigned_sfps=Count('sfps', filter=Q(sfps__assigned=False)),
        assigned_sfps=Count('sfps', filter=Q(sfps__assigned=True)),
        total_sfps=Count('sfps'),
    )
    table = tables.SFPTypeTable

    filterset = SFPTypeFilterSet
    filterset_form = forms.SFPTypeFilterForm


class SFPTypeView(generic.ObjectView):
    queryset = SFPType.objects.all()

    def get_extra_context(self, request, instance):
        used_sfps = SFP.objects.filter(
            assigned=True,
            type=instance,
        )

        unused_sfps = SFP.objects.filter(
            assigned=False,
            type=instance,
        )

        unused_sfp_table = SFPTable(unused_sfps)

        sfps_by_tenant = SFPByTenantTable(
            SFP.objects.prefetch_related('tenant').values("tenant__name").annotate(
                total_count=Count("tenant__name", filter=Q(type=instance)),
                used_count=Count("tenant__name", filter=Q(assigned=True, type=instance)),
                unused_count=Count("tenant__name", filter=Q(assigned=False, type=instance)),
            ).exclude(total_count=0).order_by("tenant__name")
        )

        sfps_by_supplier = SFPBySupplierTable(
            SFP.objects.prefetch_related('supplier').values("supplier__name").annotate(
                total_count=Count("supplier__name", filter=Q(type=instance)),
                used_count=Count("supplier__name", filter=Q(assigned=True, type=instance)),
                unused_count=Count("supplier__name", filter=Q(assigned=False, type=instance)),
            ).exclude(total_count=0).order_by("supplier__name")
        )

        return {
            "unused_sfp_table": unused_sfp_table,
            "sfps_by_tenant": sfps_by_tenant,
            "sfps_by_supplier": sfps_by_supplier,
            "count_total_sfps": len(used_sfps) + len(unused_sfps),
            "count_used_sfps": len(used_sfps),
            "count_unused_sfps": len(unused_sfps),
        }


class SFPTypeEditView(generic.ObjectEditView):
    queryset = SFPType.objects.all()
    model_form = forms.SFPTypeForm


class SFPTypeDeleteView(generic.ObjectDeleteView):
    queryset = SFPType.objects.all()


class SFPTypeBulkImportView(generic.BulkImportView):
    queryset = SFPType.objects.all()
    model_form = forms.SFPTypeCSVForm
    table = tables.SFPTypeTable


class SFPTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = SFPType.objects.all()
    table = tables.SFPTypeTable


class SFPListView(generic.ObjectListView):
    queryset = SFP.objects.all()
    table = tables.SFPTable

    filterset = SFPFilterSet
    filterset_form = forms.SFPFilterForm

    def extra_context(self):
        return {
            "bulk_edit_url": reverse("plugins:nautobot_sfp_inventory:sfp_bulk_edit")
        }


class SFPView(generic.ObjectView):
    queryset = SFP.objects.all()


class SFPEditView(generic.ObjectEditView):
    queryset = SFP.objects.all()
    model_form = forms.SFPForm
    template_name = "nautobot_sfp_inventory/sfp_add.html"


class SFPDeleteView(generic.ObjectDeleteView):
    queryset = SFP.objects.all()


class SFPBulkCreateView(generic.BulkCreateView):
    queryset = SFP.objects.all()
    form = forms.SFPBulkCreateForm
    model_form = forms.SFPForm
    pattern_target = "serial_number"
    template_name = "nautobot_sfp_inventory/sfp_bulk_add.html"


class SFPBulkEditView(generic.BulkEditView):
    queryset = SFP.objects.all()
    filterset = SFPFilterSet
    table = SFPTable
    form = forms.SFPBulkEditForm


class SFPBulkImportView(generic.BulkImportView):
    queryset = SFP.objects.all()
    model_form = forms.SFPCSVForm
    table = tables.SFPTable


class SFPBulkDeleteView(generic.BulkDeleteView):
    queryset = SFP.objects.all()
    table = tables.SFPTable
