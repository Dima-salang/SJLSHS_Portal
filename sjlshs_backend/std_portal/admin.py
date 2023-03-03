from django.contrib import admin
# Register your models here.


from .models import Post, Modules, Schedule

class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, instance, form, change):
        if not change:
            obj.Author = request.user_id
        obj.save()


admin.site.register(Post)
admin.site.register(Modules)
admin.site.register(Schedule)

