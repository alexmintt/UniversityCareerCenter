from django.contrib import admin

from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'vacancy', 'status', 'id')
    list_filter = ('status',)
    search_fields = ('student__name', 'vacancy__title')
    list_editable = ('status',)
    ordering = ('status',)
    list_display_links = ('student', 'vacancy')

admin.site.register(Application, ApplicationAdmin)