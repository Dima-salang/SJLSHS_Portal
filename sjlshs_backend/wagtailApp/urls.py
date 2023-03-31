from django.urls import path
from .views import home_page, recent_links, career_center_view

urlpatterns = [
    path('organizations/', home_page, name='student-orgs'),
    path('recent_links/', recent_links, name='recent_links'),
    path('career-center/', career_center_view, name='career-center')
]

    