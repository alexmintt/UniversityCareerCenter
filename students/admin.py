from django.contrib import admin
from import_export.admin import ExportMixin

from students.models import Student, Faculty
from students.resource import StudentResource


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'id')
    search_fields = ('name',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display_links = ('name',)

admin.site.register(Faculty, FacultyAdmin)


class StudentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = ('name', 'enrollment_year', 'graduation_year', 'faculty', 'created_at', 'id')
    list_filter = ('enrollment_year', 'graduation_year', 'faculty')
    search_fields = ('name', 'faculty__name')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display_links = ('name', 'faculty')

admin.site.register(Student, StudentAdmin)