from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import IsOwnerFilterBackend

from application.models import Application
from application.serializers import ApplicationSerializer


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [ filters.SearchFilter, IsOwnerFilterBackend]
    search_fields = ['vacancy__title', 'student__username']


    @action(detail=True, methods=['GET'])
    def approve(self, request, pk=None):
        application = self.get_object()
        application.approve()
        application.save()
        return Response({'status': 'approved'})

    @action(detail=False, methods=['get'])
    def approved_or_pending(self, request):
        queryset = Application.objects.filter((Q(status='approved') | Q(status='pending')) & ~Q(status='rejected')
                                              )
        serializer = ApplicationSerializer(queryset, many=True)
        return Response(serializer.data)

