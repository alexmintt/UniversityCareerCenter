from django.urls import path

from students import views

urlpatterns = [
    path('<int:pk>/', views.detail_view, name='student-detail-view'),
    path('', views.list_view, name='student-list-view'),
    path('search/', views.student_search, name='student-search'), 
    path('create/', views.create_view, name='student-create-view'),
    path('<int:pk>/edit/', views.list_view, name='student-edit-view'),
    path('<int:pk>/delete/', views.delete_view, name='student-delete-view'),
    path('<int:student_id>/resume/create/', views.create_or_update_resume_view, name='resume_create'),
    path('<int:student_id>/resume/<int:resume_id>/edit/', views.create_or_update_resume_view, name='resume_edit'),
    path('<int:student_id>/resume/<int:resume_id>/delete/', views.delete_resume, name='resume_delete'),
    path('certificates/<int:pk>/delete/', views.delete_certificate, name='certificate_delete'),
]