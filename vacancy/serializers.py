from rest_framework import serializers

from vacancy.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

    def validate_title(self, value):
        if Vacancy.objects.filter(title=value).exists():
            raise serializers.ValidationError("Title already exists.")
        return value