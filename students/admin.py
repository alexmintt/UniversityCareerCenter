from django.contrib import admin

from students.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'faculty', 'created_at', 'id')
    list_filter = ('course', 'faculty')
    search_fields = ('name', 'faculty')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display_links = ('name', 'faculty')

admin.site.register(Student, StudentAdmin)