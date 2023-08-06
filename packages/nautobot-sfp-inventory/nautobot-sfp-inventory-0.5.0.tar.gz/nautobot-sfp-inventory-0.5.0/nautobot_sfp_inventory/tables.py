from django_tables2 import Column

from nautobot.utilities.tables import ButtonsColumn, ToggleColumn, BaseTable
from nautobot.utilities.tables import BooleanColumn
from .models import SFPType, SFP
import django_tables2 as tables

from nautobot.tenancy.tables import TenantColumn


class SFPTypeTable(BaseTable):
    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(SFPType)
    total_sfps = tables.Column(verbose_name="Total SFPs")
    unassigned_sfps = tables.Column(verbose_name="Unassigned SFPs")
    assigned_sfps = tables.Column(verbose_name="Assigned SFPs")

    class Meta(BaseTable.Meta):
        model = SFPType
        fields = (
            "pk",
            "name",
            "slug",
            "total_sfps",
            "assigned_sfps",
            "unassigned_sfps",
            "actions"
        )
        default_columns = (
            "pk",
            "name",
            "total_sfps",
            "assigned_sfps",
            "unassigned_sfps",
            "actions",
        )
        order_by = ("name",)


class SFPTable(BaseTable):
    pk = ToggleColumn()
    serial_number = tables.Column(linkify=True)

    tenant = TenantColumn()
    actions = ButtonsColumn(SFP)
    assigned = BooleanColumn()

    class Meta(BaseTable.Meta):
        model = SFP
        fields = (
            "pk",
            "serial_number",
            "type",
            "dc_tag",
            "asset_tag",
            "tenant",
            "supplier",
            "assigned",
            "assigned_device",
            "actions"
        )
        default_columns = (
            "pk",
            "serial_number",
            "type",
            "dc_tag",
            "asset_tag",
            "tenant",
            "supplier",
            "assigned",
            "assigned_device",
            "actions"
        )
        order_by = ("serial_number",)


class SFPByTenantTable(tables.Table):
    class Meta:
        attrs = {
            "class": "table table-hover table-headings",
        }

    tenant__name = Column(verbose_name="Name")
    total_count = Column(verbose_name="Total Count")
    used_count = Column(verbose_name="Used Count")
    unused_count = Column(verbose_name="Unused Count")


class SFPBySupplierTable(tables.Table):
    class Meta:
        attrs = {
            "class": "table table-hover table-headings",
        }

    supplier__name = Column(verbose_name="Name")
    total_count = Column(verbose_name="Total Count")
    used_count = Column(verbose_name="Used Count")
    unused_count = Column(verbose_name="Unused Count")
