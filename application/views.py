from rest_framework import viewsets

from application.models import Application
from application.serializers import ApplicationSerializer


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

