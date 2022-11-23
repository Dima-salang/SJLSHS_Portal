from django.contrib import admin

# Register your models here.


from .models import Student, Post, Grades1stSem

admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Grades1stSem)