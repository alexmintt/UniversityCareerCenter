from django.contrib import admin
from import_export.admin import ExportMixin

from students.models import Student
from students.resource import StudentResource


# Register your models here.
class StudentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ('name', 'course', 'faculty', 'created_at', 'id')
    list_filter = ('course', 'faculty')
    search_fields = ('name', 'faculty')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display_links = ('name', 'faculty')

admin.site.register(Student, StudentAdmin)