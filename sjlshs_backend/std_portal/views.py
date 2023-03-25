from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from accounts.models import StudentUser, Db_Students
from .models import Post, Modules, Schedule
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django_otp.decorators import otp_required
from wagtail.models import Page
from wagtailApp.models import ArticleIndexPage, ArticlePage
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse



def home_page_view(request):
    page_articles = Page.objects.get(slug='supreme-student-government')
    
    return render(request, "home.html", {'page_articles': page_articles})


class PortalHomeView(ListView):
    model = Post
    template_name = "portal-home.html"



class PortalRedirectView(TemplateView):
    template_name = 'portal-redirect.html'

def update_users(request):
    auth_checks = 0
    queryset = Db_Students.objects.all()
    user = settings.AUTH_USER_MODEL
    for student in queryset:
        if request.user.lrn == student.lrn:
            auth_checks += 50
        if request.user.last_name == student.last_name:
            auth_checks += 10
        if request.user.email == student.email:
            auth_checks += 10
        if auth_checks >= 70:
            request.user.section = student.section
            request.user.strand = student.strand

            request.user.save()
    return render(request, 'login-redirect.html', {})



class PortalPersonalView(TemplateView):
    model = StudentUser
    template_name = 'portal-personal.html'
    

class PortalAnnouncements(ListView):
    model = Post
    template_name = "portal-announcements.html"
    paginate_by = 5 # Set the number of items to display per page
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Post.objects.all()
        else:
            queryset = Post.objects.filter(Q(Section=user.section) | Q(Section=3))
        return queryset
    


class PortalSched(ListView):
    model = Schedule
    template_name = 'portal-sched.html'


class PortalModuleRedirect(TemplateView):
    template_name = 'portal-modules-redirect.html'


class PortalModuleRedirectG12(TemplateView):
    template_name = 'portal-modules-redirectG12.html'


class PortalModules(ListView):
    template_name = 'portal-modules.html'

class PortalModulesUCSP(ListView):
    model = Modules
    template_name = 'portal-modules-ucsp.html'



        



