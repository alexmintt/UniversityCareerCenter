from django.contrib import admin
from import_export.admin import ExportMixin

from vacancy.models import Vacancy
from .models import Application
from .resource import ApplicationResource


class ApplicationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ApplicationResource
    list_display = ("student", "vacancy", "status", "id")
    list_filter = ("status",)
    search_fields = ("student__name", "vacancy__title")
    list_editable = ("status",)
    ordering = ("status",)
    list_display_links = ("student", "vacancy")
    raw_id_fields = ("student", "vacancy")


admin.site.register(Application, ApplicationAdmin)
