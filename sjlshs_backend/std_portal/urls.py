from django.urls import path
from django_otp.decorators import otp_required
from . import views
from .views import update_users

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('portal-home/', otp_required(views.PortalHomeView.as_view()), name="portal-home"),
    path('portal-personal/', otp_required(views.PortalPersonalView.as_view()), name="portal-personal"),
    path('portal-announcements', otp_required(views.PortalAnnouncements.as_view()), name="portal-announcements"),
    path('portal-sched/', otp_required(views.PortalSched.as_view()), name='portal-sched'),
    path('portal-module-redirectG12', otp_required(views.PortalModuleRedirectG12.as_view()), name='portal-modules-redirectG12'),
    path('portal-modules/', otp_required(views.PortalModules.as_view()), name='portal-modules'),
    path('portal-modules-ucsp/', otp_required(views.PortalModulesUCSP.as_view()), name='portal-modules-ucsp'),
    path('portal-redirect/', update_users, name='login-redirect'),
    path('portal-maps-redirect/', views.PortalRedirectView.as_view(), name='portal-maps-redirect'),
    path('litext/', views.chatbot_view, name='litext'),
    path('portal-modules-filter/', otp_required(views.search), name='portal-modules-filter'),
]