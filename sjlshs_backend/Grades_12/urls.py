from django.urls import path
from . import views


urlpatterns = [
    path('grades/12/', views.GradeView, name='portal-grade'),
]