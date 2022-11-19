from django.contrib import admin

# Register your models here.


from .models import Student
from std_portal.models import Post

admin.site.register(Student)
admin.site.register(Post)