from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


from .models import Post, Modules, Schedule

class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('Body',)

    exclude = ('Author',)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.Author = request.user.get_full_name()
        obj.save()


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(Author=request.user)
            
        

admin.site.register(Post, PostAdmin)
admin.site.register(Modules)
admin.site.register(Schedule)

