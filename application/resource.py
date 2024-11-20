from import_export import resources, fields

from application.models import Application


class ApplicationResource(resources.ModelResource):
    student_name = fields.Field()
    vacancy_title = fields.Field()

    class Meta:
        model = Application
        fields = ('id', 'student', 'vacancy', 'status', 'student_name', 'vacancy_title', 'id')
        export_order = ('id', 'student_name', 'vacancy_title', 'status')

    def dehydrate_student_name(self, application):
        return application.student.name

    def dehydrate_vacancy_title(self, application):
        return application.vacancy.title

    def get_export_queryset(self, queryset, request):
        return queryset.filter(status='approved')