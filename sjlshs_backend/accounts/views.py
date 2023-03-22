from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
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
from django.dispatch import receiver
from django.contrib.auth import authenticate
from django.contrib import messages
from django_otp.forms import OTPTokenForm, OTPAuthenticationForm
from django_otp import devices_for_user
from two_factor.views import LoginView
# Create your views here.

User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Get the newly created user instance
        user = form.instance

        # Call the signal to create the email device for the user
        #receiver(create_email_otp_device, sender=User, instance=user, created=True)
        #print("Signup: Email Created")
        return response

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


# def verify_otp(request):
#     user = request.user
#     print(user)
#     devices = list(devices_for_user(user))
#     device = devices[0] if devices else None
#     print(device)

#     if request.method == 'POST':
#         form = OTPTokenForm(user, request.POST)
#         print(form)
#         print(request.POST.get('otp_token'))
#         print(form.errors)
#         if form.is_valid():
#             print("form valid")
#             token = form.cleaned_data['otp_token']
#             print("acquired token:", token)
#             if device and user.verify_otp(token):
#                 print("token verified")
#                 del request.session['otp_challenge']
#                 print("deleted session challenge")
#                 print("redirecting")
#                 return redirect('login-redirect')
                
#             else:
#                 print("invalid OTP token")
#                 messages.error(request, "Invalid OTP Token")
#                 print("form errors:", form.errors)
#         else:
#             print("invalid otp token")
#             messages.error(request, "Invalid OTP Token")
#             print("form errors:", form.errors)
#     else:
#         print("else statement")
#         form = OTPTokenForm(request.user, request.POST)
#         print(request.user)
#         if not form.is_valid():
#             print("form is not valid", form.errors)
#         print(form.errors)

#     return render(request, 'registration/verify_otp.html', {'form': form})

# from django.urls import reverse
# from django.contrib.auth.decorators import login_required


# class MyLoginView(LoginView):
#     success_url = reverse_lazy('login-redirect')

#     def form_valid(self, form):
#         # check if the user has an email device
#         if self.request.user.emailaddress_set.filter(device_type='email').exists():
#             # redirect to OTP verification page
#             return redirect(reverse_lazy('two_factor:login'))
#         else:
#             # proceed with normal authentication
#             return super().form_valid(form)
            
    
