from django.urls import path

from vacancy import views

urlpatterns = [
    path("<int:pk>/", views.detail, name="vacancy-detail"),
    path("<int:pk>/delete/", views.delete_application, name="application-delete"),
]
