from django.contrib import admin

# Register your models here.


from .models import Post, Modules, Schedule


admin.site.register(Post)
admin.site.register(Modules)
admin.site.register(Schedule)
