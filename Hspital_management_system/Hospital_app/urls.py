from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.patient_register, name='register'),

    path('login/', views.patient_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),

    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),


]
