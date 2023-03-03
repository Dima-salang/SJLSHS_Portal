from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from io import StringIO
from django.core.files import File
import csv



# Register your models here.

class CustomGradeResouce(resources.Resource):
        class Meta:
                model = GradeTest
                exclude = ['id']

        def before_export(self, queryset, *args, **kwargs):
                queryset = GradeTest.objects.none
                return queryset



class GradeAdmin(ImportExportModelAdmin):
        resource_class = CustomGradeResouce
        




admin.site.register(GradePost)
admin.site.register(GradePost2nd)
admin.site.register(GradePost3rd)
admin.site.register(GradePost4th)
admin.site.register(GradeTest, GradeAdmin)


