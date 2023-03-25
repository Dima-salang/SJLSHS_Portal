from django.urls import path

from . import views
from .views import update_users

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('portal-home/', views.PortalHomeView.as_view(), name="portal-home"),
    path('portal-personal/', views.PortalPersonalView.as_view(), name="portal-personal"),
    path('portal-announcements', views.PortalAnnouncements.as_view(), name="portal-announcements"),
    path('portal-sched/', views.PortalSched.as_view(), name='portal-sched'),
    path('portal-module-redirect', views.PortalModuleRedirect.as_view(), name='portal-module-redirect'),
    path('portal-module-redirectG12', views.PortalModuleRedirectG12.as_view(), name='portal-modules-redirectG12'),
    path('portal-modules/', views.PortalModules.as_view(), name='portal-modules'),
    path('portal-modules-ucsp/', views.PortalModulesUCSP.as_view(), name='portal-modules-ucsp'),
    path('portal-redirect/', update_users, name='login-redirect'),
    path('portal-maps-redirect/', views.PortalRedirectView.as_view(), name='portal-maps-redirect'),

]