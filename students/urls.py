from django.urls import path

from students import views

urlpatterns = [
    path('<int:pk>/', views.detail_view, name='student-detail-view'),
    path('', views.list_view, name='student-list-view'),
    path('create/', views.create_view, name='student-create-view'),
    path('<int:pk>/edit/', views.list_view, name='student-edit-view'),
    path('<int:pk>/delete/', views.delete_view, name='student-delete-view'),
]