from rest_framework import serializers

from students.models import Student, Faculty
from vacancy.serializers import VacancySerializer


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name')

    def validate_name(self, value):
        if Faculty.objects.filter(name=value).exists():
            raise serializers.ValidationError("Faculty already exists.")

        return value

    def create(self, validated_data):
        faculty = Faculty.objects.create(**validated_data)
        return faculty

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(many=False, read_only=True)
    faculty_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = ('id', 'faculty_id', 'name', 'faculty', 'enrollment_year', 'graduation_year', 'resume')

    def validate(self, data):
        if data['enrollment_year'] > data['graduation_year']:
            raise serializers.ValidationError("Enrolled year must be before graduated year.")
        return data

    def create(self, validated_data):
        faculty_id = validated_data.pop('faculty_id')
        faculty = Faculty.objects.get(id=faculty_id)
        student = Student.objects.create(faculty=faculty, **validated_data)
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.enrollment_year = validated_data.get('enrollment_year', instance.enrollment_year)
        instance.graduation_year = validated_data.get('graduation_year', instance.graduation_year)
        instance.resume = validated_data.get('resume', instance.resume)

        faculty_id = validated_data.pop('faculty_id', None)
        if faculty_id:
            faculty = Faculty.objects.get(id=faculty_id)
            instance.faculty = faculty
        instance.save()
        return instance
