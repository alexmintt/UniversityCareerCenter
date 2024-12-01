from rest_framework import serializers

from students.models import Student, Faculty
from vacancy.serializers import VacancySerializer


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('name', 'id')


    def validate_name(self, value):
        if value in Faculty.objects.values_list('name', flat=True):
            raise serializers.ValidationError("Faculty already exists.")


class StudentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(many=False)
    vacancies = VacancySerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['enrolled_year'] > data['graduated_year']:
            raise serializers.ValidationError("Enrolled year must be before graduated year.")
        return data

