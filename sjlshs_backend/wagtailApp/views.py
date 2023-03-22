from django.shortcuts import render
from wagtail.models import Page

# Create your views here.
def home_page(request):
    home_page = Page.objects.get(slug='student-orgs')  # assuming 'home' is the slug for your home page
    return render(request, 'home_page.html', {'home_page': home_page})



def SSG_page(request):
    ssg_page = Page.objects.get(slug='sljlshs-supreme-student-government')  # assuming 'home' is the slug for your home page
    return render(request, 'ssg_page.html', {'ssg_page': ssg_page})