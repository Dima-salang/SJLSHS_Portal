from django.contrib import admin

# Register your models here.


from .models import Post, GradePost
from .forms import ClassSchedule

admin.site.register(Post)
admin.site.register(GradePost)