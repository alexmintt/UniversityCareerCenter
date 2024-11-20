from import_export import resources, fields

from vacancy.models import Vacancy


class VacancyResource(resources.ModelResource):
    formatted_salary = fields.Field()  # Custom field to include formatted salary

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'company', 'salary', 'description', 'requirements', 'created_at')
        export_order = ('id', 'title', 'company', 'formatted_salary', 'created_at')

    # Custom field logic for formatted salary
    def dehydrate_formatted_salary(self, vacancy):
        return f"${vacancy.salary:,.2f}"  # Format salary as currency
