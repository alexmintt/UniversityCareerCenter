from django.contrib import admin

from .models import UserLog


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('email', 'date', 'url')
    search_fields = ('email', 'url')
    list_filter = ('date',)
