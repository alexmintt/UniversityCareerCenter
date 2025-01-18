"""
URL configuration for UniversityCareerCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from application.views import ApplicationsViewSet
from students.view_sets import StudentViewSet, FacultyViewSet, ResumeViewSet
from vacancy.views import VacancyViewSet, CompanyViewSet

router = DefaultRouter()

router.register(r"students", StudentViewSet)
router.register(r"faculties", FacultyViewSet)
router.register(r"companies", CompanyViewSet)
router.register(r"applications", ApplicationsViewSet)
router.register(r"vacancies", VacancyViewSet)
router.register(r"resume", ResumeViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="University Career Center API",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path("api-auth/", include("rest_framework.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("admin/", admin.site.urls),
    # path("api/", include(router.urls)),
    path("accounts/", include("allauth.urls")),
    path("", include("vacancy.urls")),
    path("students/", include("students.urls")),
    path("auth/", include("auth_app.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    
]
