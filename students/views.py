from django.db.models import Q
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['course']
    search_fields = ['name', 'faculty', 'resume']

    @action(detail=False, methods=['GET'], url_path='by-course') # GET http://localhost:8000/api/students/by-course?course=1
    def get_by_course(self, request):
        course = request.query_params.get('course')

        if course is None:
            return Response({'error': 'Parameter course is required'}, status=400)
        students = Student.objects.filter(course=course)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], url_path='update-resume')
    def update_resume(self, request):
        student = self.get_object()
        student.resume = request.data.get('resume')
        student.save()
        return Response({'status': 'success'})

    @action(detail=False, methods=['GET'])
    def get_bachelors(self, request):
        students = Student.objects.filter((Q(course__gte=1) | Q(course__lte=4)) & ~Q(course__gte=5))
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
