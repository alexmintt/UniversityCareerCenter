from rest_framework import serializers

from application.models import Application
from students.models import Student
from students.serializers import StudentSerializer
from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class ApplicationSerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer(many=False, read_only=True)
    vacancy_id = serializers.IntegerField(write_only=True)
    student = StudentSerializer(many=False, read_only=True)
    student_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Application
        fields = '__all__'

    def validate_status(self, value):
        if value not in ['approved', 'pending', 'rejected']:
            raise serializers.ValidationError("Invalid status")
        return value

    def create(self, validated_data):
        vacancy_id = validated_data.pop('vacancy_id')
        student_id = validated_data.pop('student_id')

        student = Student.objects.get(id=student_id)
        vacancy = Vacancy.objects.get(id=vacancy_id)

        application = Application.objects.create(student=student, vacancy=vacancy, **validated_data)
        application.save()
        return application

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)

        student_id = validated_data.pop('student_id', None)
        vacancy_id = validated_data.pop('vacancy_id', None)
        if vacancy_id:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            instance.vacancy = vacancy

        if student_id:
            student = Student.objects.get(id=student_id)
            instance.student = student

        instance.save()

        return instance
