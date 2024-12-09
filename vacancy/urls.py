from django.urls import path

from vacancy import views

urlpatterns = [
    path('', views.list, name='vacancy-list-view'),
]