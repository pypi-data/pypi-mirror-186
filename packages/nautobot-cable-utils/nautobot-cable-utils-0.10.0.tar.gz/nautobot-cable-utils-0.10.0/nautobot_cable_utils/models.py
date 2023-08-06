from django.db import models

from nautobot.dcim.choices import CableTypeChoices, CableLengthUnitChoices
from nautobot.dcim.models import Cable
from nautobot.utilities.fields import ColorField
from nautobot.utilities.querysets import RestrictedQuerySet
from nautobot.core.models import BaseModel


class CablePlug(BaseModel):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class CableTemplate(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    label = models.CharField(
        max_length=100,
        blank=True
    )
    type = models.CharField(
        max_length=50,
        choices=CableTypeChoices,
        blank=True
    )
    plug = models.ForeignKey(
        to=CablePlug,
        on_delete=models.CASCADE,
        related_name="cable_templates",
        blank=True,
        null=True,
    )
    color = ColorField(
        blank=True
    )
    length = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    length_unit = models.CharField(
        max_length=50,
        choices=CableLengthUnitChoices,
        blank=True,
    )
    cable = models.OneToOneField(
        Cable,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    owner = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.CASCADE,
        related_name="cable_templates",
        blank=True,
        null=True,
    )

    supplier = models.ForeignKey(
        to="dcim.Manufacturer",
        on_delete=models.PROTECT,
        related_name="cable_templates",
        null=True,
        blank=True,
    )

    procurement_ident = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Procurement Identifier"
    )

    objects = RestrictedQuerySet.as_manager()

    csv_headers = [
        'name', 'owner', 'type', 'plug', 'label', 'color', 'length', 'length_unit', "supplier", "procurement_ident"
    ]

    def __str__(self):
        return self.name


class MeasurementLog(BaseModel):
    link = models.URLField(
        blank=True,
        null=True
    )
    cable = models.OneToOneField(
        Cable,
        on_delete=models.CASCADE,
    )
