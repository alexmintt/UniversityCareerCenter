from django.contrib import admin
from import_export.admin import ExportMixin

from vacancy.models import Vacancy
from vacancy.resource import VacancyResource


class VacancyAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = VacancyResource
    list_display = ('title', 'company', 'salary', 'created_at', 'id')
    list_filter = ('company', 'created_at')
    search_fields = ('title', 'company')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display_links = ('title', 'company')

admin.site.register(Vacancy, VacancyAdmin)