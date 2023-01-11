from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #path('activate/<uidb64>/<token>', views.SignUpView.activate, name='activate'),
    path('teachers/dashboard/', views.TeacherDashboardView, name='tc-dashboard'),
    path('teachers/view/student-info<int:uid>', views.StudentInfoView, name='student-info'),

]