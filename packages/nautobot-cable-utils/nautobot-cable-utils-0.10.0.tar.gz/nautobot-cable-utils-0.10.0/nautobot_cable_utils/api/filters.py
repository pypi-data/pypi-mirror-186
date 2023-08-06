import django_filters
from django.db.models import Q

from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot_cable_utils.models import CableTemplate, CablePlug
from nautobot.utilities.filters import BaseFilterSet


class CablePlugFilterSet(
    BaseFilterSet,
    CreatedUpdatedFilterSet,
):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(Q(name__icontains=value))

    class Meta:
        model = CablePlug
        fields = ["id", "name"]


class CableTemplateFilterSet(
    BaseFilterSet,
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
            Q(name__icontains=value) | Q(label__icontains=value)
        )

    class Meta:
        model = CableTemplate
        fields = [
            "id",
            "name",
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
