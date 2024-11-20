from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_course(self, value):
        if value < 1 or value > 6:
            raise serializers.ValidationError("Course must be between 1 and 6.")
        return value
