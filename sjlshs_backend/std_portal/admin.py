from django.contrib import admin
# Register your models here.


from .models import Post, Modules, Schedule

class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.Author:
            instance.Author = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Post)
admin.site.register(Modules)
admin.site.register(Schedule)

