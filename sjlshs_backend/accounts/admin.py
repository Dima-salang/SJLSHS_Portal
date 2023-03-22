from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm, CustomerUserChangeForm, UserCreationForm
from .models import *
from Grades_12.models import *
from std_portal.models import *
from django.contrib.auth.models import Group
from std_portal.admin import PostAdmin
from postman.models import Message, PendingMessage
from postman.admin import MessageAdmin, PendingMessageAdmin


class TeacherAdminArea(admin.AdminSite):
    site_header = "Teachers' Administration Site"


class StudentUserAdmin(admin.ModelAdmin):
    model = StudentUser

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        print("Function called")
        if request.user.is_superuser:
            print("returned queryset")
            return queryset
        elif request.user.groups.filter(name="Teacher").exists():
            print("returned filter queryset")
            return request.user.teacheruser.get_students()
        else:
            return queryset.none()

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('lrn', 'username', 'password', 'birthday', 'section', 'grade_year', 'strand')})

admin.site.site_header = "SJLSHS Portal"
# Register your models here.

class CustomAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomerUserChangeForm
    list_display = ['lrn', 'last_name', 'first_name', 'section', 'birthday', 'username', 'email', 'strand']
    model = StudentUser
    add_fieldsets = tuple(fields)

CustomAdmin.fieldsets = tuple(fields)


admin.site.register(StudentUser, StudentUserAdmin)
admin.site.register(TeacherUser)
admin.site.register(StudentSection)
admin.site.register(StudentYear)
admin.site.register(Subject)
admin.site.register(Db_Students)
admin.site.register(TrackAndStrand)





teacher_site = TeacherAdminArea(name="TeacherAdminSite")
teacher_site.register(StudentUser, StudentUserAdmin)
teacher_site.register(Post, PostAdmin)
teacher_site.register(Schedule)
teacher_site.register(Message, MessageAdmin)
teacher_site.register(PendingMessage, PendingMessageAdmin)




