from rest_framework import serializers

from vacancy.models import Vacancy, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate_name(self, value):
        instance = getattr(self, 'instance', None)
        pk = getattr(instance, 'pk', None)

        if pk:
            if Company.objects.filter(name=value).exclude(pk=pk).exists():
                raise serializers.ValidationError("Company already exists.")
        else:
            if Company.objects.filter(name=value).exists():
                raise serializers.ValidationError("Company already exists.")
        return value


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'

    def validate_title(self, value):
        instance = getattr(self, 'instance', None)
        pk = getattr(instance, 'pk', None)

        if pk:
            if Vacancy.objects.filter(title=value).exclude(pk=pk).exists():
                raise serializers.ValidationError("Faculty already exists.")
        else:
            if Vacancy.objects.filter(title=value).exists():
                raise serializers.ValidationError("Faculty already exists.")
        return value

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(**validated_data)

        company_id = validated_data.get('company_id')
        company = Company.objects.get(id=company_id)
        vacancy.company = company

        vacancy.save()

        return vacancy

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        company_id = validated_data.get('company_id', instance)
        if company_id:
            company = Company.objects.get(id=company_id)
            instance.company = company
        instance.save()

        return instance
