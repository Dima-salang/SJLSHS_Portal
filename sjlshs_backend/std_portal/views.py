from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse


def home_page_view(request):
    return render(request, "home.html", {})
