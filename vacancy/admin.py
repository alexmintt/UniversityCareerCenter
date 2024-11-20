from django.contrib import admin

from vacancy.models import Vacancy

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'created_at', 'id')
    list_filter = ('company', 'created_at')
    search_fields = ('title', 'company')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display_links = ('title', 'company')

admin.site.register(Vacancy, VacancyAdmin)