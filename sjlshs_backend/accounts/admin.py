from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm, CustomerUserChangeForm
from .models import StudentUser, TeacherUser, StudentSection




class CustomAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomerUserChangeForm
    list_display = ['email', 'username', 'age']
    model = StudentUser

admin.site.site_header = "SJLSHS Portal"
# Register your models here.

admin.site.register(StudentUser)
admin.site.register(TeacherUser)
admin.site.register(StudentSection)




