from django.urls import path

from students import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('student/<int:pk>/', views.detail_view, name='student-detail-view'),
    path('student/', views.list_view, name='student-list-view'),

]