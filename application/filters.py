from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend

from application.models import Application


class IsOwnerFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset: QuerySet[Application], view):
        return queryset.filter(student__user=request.user.id)
