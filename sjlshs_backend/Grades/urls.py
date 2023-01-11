from django.urls import path
from . import views


urlpatterns = [
    path('portal-grade/', views.GradeView, name='portal-grade'),
]