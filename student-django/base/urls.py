from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.getRoutes),
    path('students/', views.getStudents),
    # path('lecturers/', views.getLecturers),
    path('students/<id>', views.getStudentDetail),
]
