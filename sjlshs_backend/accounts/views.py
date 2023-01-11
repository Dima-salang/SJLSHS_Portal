from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomCreationForm, StudentInfoForm
from .models import StudentUser
from Grades.models import GradePost, GradePost2nd, GradePost3rd, GradePost4th

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    #def form_valid(self, form):

        #if form.is_valid():
            #user = form.save(commit=False)
            #user.is_active = False
            #user.save()

            #curr_site = get_current_site(self.request)
            #mail_subject = 'Activate your account.'
            #message = render_to_string('email_template.html', {
                #'user': user,
                #'domain': curr_site.domain,
                #'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #'token': account_activation_token.make_token(user),
            #})
            #to_email = form.cleaned_data.get('email')
            #email = EmailMessage(mail_subject, message, to=[to_email])
            #email.send()

            #return super().form_valid(form)


    #def activate(request, uidb64, token):
        #User = get_user_model()
        #try:
            #uid = force_bytes(urlsafe_base64_decode(uidb64))
            #user = User.objects.get(pk=uid)
        #except:
            #pass
        #if user is not None and account_activation_token.check_token(user,token):
            #user.is_active = True
            #user.save()
            #login(request, user)
            #return redirect('login-redirect')


                    
def TeacherDashboardView(request):
    students = StudentUser.objects.exclude(groups__name__in=['Teachers'])
    context = {
        'students' : students
    }

    return render(request, 'tc-dashboard.html', context)


def StudentInfoView(request, uid):
    student = StudentUser.objects.get(id=uid)
    form = StudentInfoForm(instance=student)
    if request.method == 'POST':
        form = StudentInfoForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            redirect('accounts/teachers/dashboard')
    contexts = {
        'form' : form
    }

    return render(request, 'tc-student-info.html', contexts)


def StudentGradeView(request, uid):
    fs1q = GradePost.objects.get(pk=uid)
    fs2q = GradePost2nd.objects.get(pk=uid)
    ss3q = GradePost3rd.objects.get(pk=uid)
    ss4q = GradePost4th.objects.get(pk=uid)

            
    
