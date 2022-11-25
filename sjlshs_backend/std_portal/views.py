from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Post, GradePost
from .forms import ClassSchedule
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.http import HttpResponse


def home_page_view(request):
    return render(request, "home.html", {})


class PortalHomeView(ListView):
    model = Post
    template_name = "portal-home.html"
    

class PortalGradeView(ListView):
    grades = GradePost.objects.all
    model = GradePost
    template_name = "portal-grades.html"


def uploadfile(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document_file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'portal-sched.html', {})

        



