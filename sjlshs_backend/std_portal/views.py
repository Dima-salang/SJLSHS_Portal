from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from accounts.models import StudentUser, Db_Students
from .models import Post, Modules, Schedule
from django.conf import settings
from django_otp.decorators import otp_required
from wagtail.models import Page
from django.db.models import Q
from django.http import JsonResponse
import spacy
# Create your views here.

nlp = spacy.load('C:\\Users\\Luis\\PycharmProjects\\SJLSHS_Portal\\SJLSHS_Portal\\sjlshs_backend\\std_portal\\litext')

def home_page_view(request):
    ssg_page = Page.objects.get(slug='supreme-student-government')
    news_page = ssg_page.get_children().filter(slug='news').first()
    events_page = ssg_page.get_children().filter(slug='events').first()
    announcements_page = ssg_page.get_children().filter(slug='announcements').first()
    news_articles = news_page.get_children().specific().live().order_by('-first_published_at')
    event_posts = events_page.get_children().specific().live().order_by('-first_published_at')
    announcement_posts = announcements_page.get_children().specific().live().order_by('-first_published_at')
    return render(request, 'home.html', {'recent_events': event_posts,
                                'recent_news': news_articles,
                                'recent_announcements': announcement_posts})                               


class PortalHomeView(ListView):
    model = Post
    template_name = "portal-home.html"



class PortalRedirectView(TemplateView):
    template_name = 'portal-redirect.html'

@otp_required
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


def chatbot_view(request):
    if request.method == 'POST':
        
        message = request.POST.get('message', '')
        predicted_category = predict_category(message)
        
        # Use the predicted category to generate a response
        if predicted_category == 'enrollment':
            response = """Enrollment is open from October 1 to 15. If you are an incoming grade 11, kindly visit the admission page of the website for admission.
                         If you are an incoming grade 12 student, please coordinate with your adviser for Grade 12 enrollment.
                         Bring these requirements at the prescribe enrollment period: 
                         1x1 ID picture
                         Photocopy of PSA Birth Certificate
                         Certificate of Good Moral
                         Your F138 from last school year"""
        elif predicted_category == 'schedule':
            response = 'You can find the class schedule on our website.'
        elif predicted_category == 'course':
            response = 'SJLSHS offers the STEM, HUMSS, ABM, and TVL. Please visit our website for more information.'
        elif predicted_category == 'fee':
            response = 'SJLSHS is a public educational institution. There are no tuition fees.'
        elif predicted_category == 'tvl_strands':
            response = """TVL Strands include ICT, SMAW, HE, and Automation."""
        elif predicted_category == 'organizations':
            response = """SJLSHS on fostering a friendly and lively school community. There are many organizations that you can join, such as:
                        Supreme Student Government
                        Litexian Achievers Club
                        Barkada-Kontra Droga
                        Yes-O"""
        elif predicted_category == 'school_contact':
            response = """SJLSHS can be found at Blk 40 Lt 1 Opel Street Litex Village
                        You can contact school at (02)3959192 and the school registrar at litexvillageshs@gmail.com
                        You can look for Sir Merwin Vergara during school hours for enrollment purposes.
                        For more information, you can see more contact details at the bottom of the SJLSHS website."""
        else:
            response = 'I am sorry, I do not understand. Please try asking me something else.'
        
        print(response)
        return JsonResponse({'message': response})

def predict_category(text):
    doc = nlp(text)
    label_scores = doc.cats
    predicted_label = max(label_scores, key=label_scores.get)
    return predicted_label

    



        



