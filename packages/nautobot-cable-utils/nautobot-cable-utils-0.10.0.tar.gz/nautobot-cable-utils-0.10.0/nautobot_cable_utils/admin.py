from django.contrib import admin

from nautobot_cable_utils.models import CablePlug


@admin.register(CablePlug)
class CablePlugAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ("name",)
