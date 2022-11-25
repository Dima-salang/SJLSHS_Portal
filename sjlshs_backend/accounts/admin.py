from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm, CustomerUserChangeForm, UserCreationForm
from .models import StudentUser, TeacherUser, StudentSection

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('lrn', 'username', 'password', 'birthday', 'section')})

admin.site.site_header = "SJLSHS Portal"
# Register your models here.

class CustomAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomerUserChangeForm
    list_display = ['lrn', 'last_name', 'first_name', 'section', 'birthday', 'username', 'email',]
    model = StudentUser
    add_fieldsets = tuple(fields)

CustomAdmin.fieldsets = tuple(fields)


admin.site.register(StudentUser, CustomAdmin)
admin.site.register(TeacherUser)
admin.site.register(StudentSection)




