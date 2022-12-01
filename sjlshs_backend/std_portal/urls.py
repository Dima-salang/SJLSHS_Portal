from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('portal-home/', views.PortalHomeView.as_view(), name="portal-home"),
    path('portal-grade/', views.PortalGradeView.as_view(), name="portal-grade"),
    path('portal-personal/', views.PortalPersonalView.as_view(), name="portal-personal"),
    path('portal-announcements', views.PortalAnnouncements.as_view(), name="portal-announcements"),
    path('portal-sched/', views.PortalSched.as_view(), name='portal-sched'),
    path('portal-modules/', views.PortalModules.as_view(), name='portal-modules'),
    path('portal-redirect/', views.PortalLoginRedirect.as_view(), name='login-redirect')

]