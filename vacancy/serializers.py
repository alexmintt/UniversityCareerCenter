from rest_framework import serializers

from vacancy.models import Vacancy, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate_name(self, value):
        if Company.objects.filter(name=value).exists():
            raise serializers.ValidationError("Company already exists.")
        return value

class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)

    class Meta:
        model = Vacancy
        fields = '__all__'

    def validate_title(self, value):
        if Vacancy.objects.filter(title=value).exists():
            raise serializers.ValidationError("Title already exists.")
        return value