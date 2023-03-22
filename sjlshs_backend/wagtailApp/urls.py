from django.urls import path
from .views import home_page, SSG_page

urlpatterns = [
    path('organizations/', home_page, name='student-orgs'),
    path('pages/sljlshs-supreme-student-government/', SSG_page, name='SSG_Page'),
]

    