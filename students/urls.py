from django.urls import path

from students import views

urlpatterns = [
    path('profile/', views.detail_view, name='student-profile'),
    path('search/', views.student_search, name='student-search'), 
    path('create/', views.create_view, name='student-create-view'),
    path('edit/', views.edit_view, name='student-edit-view'),
    path('resume/create/', views.create_or_update_resume_view, name='resume_create'),
    path('resume/<int:resume_id>/edit/', views.create_or_update_resume_view, name='resume_edit'),
    path('resume/<int:resume_id>/delete/', views.delete_resume, name='resume_delete'),
    path('certificates/<int:pk>/delete/', views.delete_certificate, name='certificate_delete'),
]