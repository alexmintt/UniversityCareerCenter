from datetime import datetime

from django.db.models import Q
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from students.models import Student, Faculty, Resume
from students.serializers import StudentSerializer, FacultySerializer, ResumeSerializer
from vacancy.serializers import VacancySerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['faculty']
    search_fields = ['name', 'faculty', 'resume']

    @action(detail=False, methods=['GET'], url_path='by-faculty')
    def get_by_faculty(self, request):
        faculty = request.query_params.get('faculty')

        if faculty is None:
            return Response({'error': 'Parameter course is required'}, status=400)
        students = Student.objects.filter(faculty=faculty)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], url_path='update-resume')
    def update_resume(self, request):
        student = self.get_object()
        student.resume = request.data.get('resume')
        student.save()
        return Response({'status': 'success'})

    @action(detail=True, methods=['GET'], url_path='vacancies')
    def get_vacancies(self, request, pk):
        student = self.get_object()
        vacancies = student.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_graduated(self, request):
        students = Student.objects.filter(graduation_year__lt=datetime.now().year)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'text', 'skills']
