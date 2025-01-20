from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import format_html
from import_export.admin import ExportMixin
from weasyprint import HTML

from students.models import Student, Faculty, Resume
from students.resource import StudentResource

class StudentInline(admin.TabularInline):
    """
Inline to manage students associated with a resume.
    """
    model = Student.resume.through
    extra = 1
    verbose_name = "Студент"
    verbose_name_plural = "Студенты"
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "id", 'pdf_button', 'short_text_preview')
    search_fields = ("title",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_display_links = ("title",)
    date_hierarchy = 'updated_at'
    inlines = [StudentInline]



    @admin.display(description="Short Text Preview")
    def short_text_preview(self, obj):
        """
Display the first 50 characters of the resume text.
        """
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text


    def pdf_button(self, obj):
        """
        Adds a PDF generation button in the list display.
        """
        url = reverse('admin:generate_resume_pdf', args=[obj.id])  # Reverse the custom admin URL
        return format_html('<a class="btn btn-sm btn-primary" href="{}">Generate PDF</a>', url)

    pdf_button.short_description = "Generate PDF"

    def get_urls(self):
        """
        Add a custom URL to handle PDF generation.
        """
        from django.urls import path

        urls = super().get_urls()
        custom_urls = [
            path('<int:resume_id>/generate-pdf/', self.admin_site.admin_view(self.generate_pdf), name='generate_resume_pdf'),
        ]
        return custom_urls + urls
    def generate_pdf(self, request, resume_id):
        """
        Generates a PDF for a single resume.
        """
        # Fetch the specific resume
        resume = Resume.objects.get(pk=resume_id)

        # Render HTML to a string
        html_string = render_to_string('students/resume/pdf_template.html', {'resumes': [resume]})

        # Convert HTML to PDF
        pdf_file = HTML(string=html_string).write_pdf()

        # Prepare the response
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{resume.title}.pdf"'
        return response

    generate_pdf.short_description = "Generate PDF for selected resumes"


admin.site.register(Resume, ResumeAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "id")
    search_fields = ("name",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_display_links = ("name",)


admin.site.register(Faculty, FacultyAdmin)


class StudentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StudentResource
    filter_horizontal = ['resume']
    list_display = (
        "name",
        "enrollment_year",
        "graduation_year",
        "faculty",
        "created_at",
        "id",
    )
    list_filter = ("enrollment_year", "graduation_year", "faculty")
    search_fields = ("name", "faculty__name")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_display_links = ("name", "faculty")


admin.site.register(Student, StudentAdmin)
