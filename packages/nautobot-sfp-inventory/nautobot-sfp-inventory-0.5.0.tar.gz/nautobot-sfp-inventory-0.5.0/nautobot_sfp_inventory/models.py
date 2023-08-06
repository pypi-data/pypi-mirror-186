from django.db import models
from django.urls import reverse

from nautobot.core.fields import AutoSlugField
from nautobot.extras.utils import extras_features
from nautobot.core.models.generics import PrimaryModel


@extras_features(
    "custom_fields",
    "relationships",
)
class SFPType(PrimaryModel):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from="name")

    comments = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "SFP Type"
        verbose_name_plural = "SFP Types"

    def __str__(self):
        return self.name

    @property
    def display(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:nautobot_sfp_inventory:sfptype", args=[self.pk])


class SFP(PrimaryModel):
    serial_number = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Serial Number"
    )

    type = models.ForeignKey(
        to="nautobot_sfp_inventory.SFPType",
        on_delete=models.CASCADE,
        related_name="sfps"
    )

    dc_tag = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=True,
        verbose_name="DC Tag"
    )

    asset_tag = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=True,
        verbose_name="Asset Tag"
    )

    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="sfps",
        blank=True,
        null=True,
    )

    supplier = models.ForeignKey(
        to="dcim.Manufacturer",
        on_delete=models.PROTECT,
        related_name="sfps",
        null=True,
    )

    procurement_ident = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Procurement Identifier"
    )

    end_of_manufacturer_support = models.DateField(
        blank=True,
        null=True,
    )

    comments = models.TextField(blank=True)

    assigned = models.BooleanField(
        default=False
    )

    assigned_device = models.ForeignKey(
        to="dcim.Device",
        on_delete=models.SET_NULL,
        related_name="sfps",
        blank=True,
        null=True,
        verbose_name="Assigned Device"
    )

    class Meta:
        ordering = ["serial_number"]
        verbose_name = "SFP"
        verbose_name_plural = "SFPs"

    def __str__(self):
        return self.serial_number

    @property
    def display(self):
        return self.serial_number

    def get_absolute_url(self):
        return reverse("plugins:nautobot_sfp_inventory:sfp", args=[self.pk])

    def save(self, *args, **kwargs):
        if self.assigned_device:
            self.assigned = True

        super().save(*args, **kwargs)
