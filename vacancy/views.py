from rest_framework import viewsets

from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
