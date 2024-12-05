from import_export import resources, fields

from students.models import Student


class StudentResource(resources.ModelResource):
    full_name = fields.Field()

    class Meta:
        model = Student
        fields = ('id', 'name', 'faculty', 'resume', 'created_at')
        export_order = ('id', 'full_name', 'faculty', 'created_at')

    def get_export_queryset(self, queryset, request):
        return queryset.filter(faculty=2)

    def dehydrate_full_name(self, student):
        return f"{student.name} ({student.faculty})"

    def get_faculty(self, student):
        return student.faculty.upper()