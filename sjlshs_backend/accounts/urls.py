from django.urls import path
from . import views
from django_otp.views import LoginView
from django_otp.forms import OTPTokenForm, OTPAuthenticationForm

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #path('activate/<uidb64>/<token>', views.SignUpView.activate, name='activate'),
    path('teachers/dashboard/', views.TeacherDashboardView, name='tc-dashboard'),
    path('teachers/view/student-info<int:uid>', views.StudentInfoView, name='student-info'),
    path('login/', views.CustomOTPLogInView.as_view(), name='login_otp'),
    # path('send_otp/', views.verify_otp, name='send_otp'),
    # path('token_verification/', views.MyLoginView.as_view(), name='verify_token'),

]