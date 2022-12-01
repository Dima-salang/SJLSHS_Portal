from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Post, GradePost, StudentUser, Modules, Schedule
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.http import HttpResponse


def home_page_view(request):
    return render(request, "home.html", {})


class PortalHomeView(ListView):
    model = Post
    template_name = "portal-home.html"


class PortalLoginRedirect(TemplateView):
    model = StudentUser
    template_name = "login-redirect.html"
    

class PortalGradeView(ListView):
    model = GradePost
    template_name = "portal-grades.html"



class PortalPersonalView(TemplateView):
    model = StudentUser
    template_name = 'portal-personal.html'


class PortalAnnouncements(ListView):
    model = Post
    template_name = "portal-announcements.html"

class PortalSched(ListView):
    model = Schedule
    template_name = 'portal-sched.html'

class PortalModules(ListView):
    model = Modules
    template_name = 'portal-modules.html'

        



