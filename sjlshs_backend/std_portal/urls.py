from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('portal-home/', views.PortalHomeView.as_view(), name="portal-home"),
    path('portal-grade/', views.PortalGradeView.as_view(), name="portal-grade"),
    path('portal-sched/', views.uploadfile, name='portal-sched'),
    

]