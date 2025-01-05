from django.contrib import admin
from import_export.admin import ExportMixin

from application.models import Application
from vacancy.models import Vacancy, Company
from vacancy.resource import VacancyResource


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "id")
    search_fields = ("name",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_display_links = ("name",)


admin.site.register(Company, CompanyAdmin)


class VacancyAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = VacancyResource
    list_display = ("title", "company", "salary", "created_at", "id")
    list_filter = ("company", "created_at")
    search_fields = ("title", "company__name")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_display_links = ("title", "company")
    inlines = [ApplicationInline]


admin.site.register(Vacancy, VacancyAdmin)
