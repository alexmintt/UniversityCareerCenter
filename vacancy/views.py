from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from vacancy.models import Vacancy, Company
from vacancy.serializers import VacancySerializer, CompanySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "description"]
    filterset_fields = ["title", "description"]

    @action(detail=False, methods=["GET"], url_path="by-salary")
    def get_by_salary(self, request):
        min_salary = request.query_params.get("min_salary")
        max_salary = request.query_params.get("max_salary")
        if min_salary is None or max_salary is None:
            return Response(
                {"error": "Parameters min_salary and max_salary are required"},
                status=400,
            )
        vacancies = Vacancy.objects.filter(
            salary__gte=min_salary, salary__lte=max_salary
        )
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="remote")
    def find_remote_vacancies(self, request):
        vacancies = Vacancy.objects.filter(
            Q(description__icontains="Remote")
            | (Q(title__icontains="Developer") & ~Q(title__icontains="Intern"))
        )
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="reverse-lazy")
    def reverse_lazy_example(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)

        reverse_lazy_url = reverse_lazy("vacancy-list", request=request)
        reverse_url = reverse("vacancy-list")

        return Response(
            {
                "reverse_lazy": reverse_lazy_url,
                "reverse": reverse_url,
                "data": serializer.data,
            }
        )


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "description", "address"]
    filterset_fields = ["name", "description", "address"]


def list(request):
    vacancies = Vacancy.objects.all().order_by('-title')
    return render(request, "vacancy_list.html", {"vacancies": vacancies})
