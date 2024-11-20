from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['title', 'description']

    @action(detail=False, methods=['GET'], url_path='by-salary')
    def get_by_salary(self, request):
        min_salary = request.query_params.get('min_salary')
        max_salary = request.query_params.get('max_salary')
        if min_salary is None or max_salary is None:
            return Response({'error': 'Parameters min_salary and max_salary are required'}, status=400)
        vacancies = Vacancy.objects.filter(salary__gte=min_salary, salary__lte=max_salary)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
