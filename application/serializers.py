from rest_framework import serializers

from application.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validated_data):
        application = Application.objects.create(**validated_data)
        application.save()
        return application
