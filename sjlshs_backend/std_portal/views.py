from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
from django.http import HttpResponse


def home_page_view(request):
    return render(request, "home.html", {})


class PortalHomeView(ListView):
    model = Post
    template_name = "portal-home.html"
    


