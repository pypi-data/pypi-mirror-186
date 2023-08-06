import django_filters
from django.db.models import Q

from nautobot.dcim.models import Manufacturer
from nautobot.extras.filters import NautobotFilterSet
from nautobot.tenancy.models import Tenant

from .models import CableTemplate, CablePlug


class CableTemplateFilterSet(NautobotFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    owner_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label="Owner (ID)",
    )
    owner = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        field_name="owner__slug",
        to_field_name="slug",
        label="Owner (Slug)",
    )

    plug_id = django_filters.ModelMultipleChoiceFilter(
        queryset=CablePlug.objects.all(),
        label="Plug (ID)",
    )

    plug = django_filters.ModelMultipleChoiceFilter(
        queryset=CablePlug.objects.all(),
        field_name="plug__name",
        to_field_name="name",
        label="Plug (Name)",
    )

    supplier_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label="Supplier (ID)",
    )

    supplier = django_filters.ModelMultipleChoiceFilter(
        queryset=Manufacturer.objects.all(),
        field_name="supplier__name",
        to_field_name="name",
        label="Supplier (Name)",
    )

    class Meta:
        model = CableTemplate
        fields = ['name', 'type', 'color', "procurement_ident"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
                Q(name__icontains=value) |
                Q(label__icontains=value) |
                Q(procurement_ident__icontains=value)
        )
        return queryset.filter(qs_filter)
