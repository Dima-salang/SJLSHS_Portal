from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .resources import GradeResource

# Register your models here.

class GradeResource(resources.ModelResource):

    class Meta:
        model = GradeTest
        import_id_fields = ['lrn',]
        exclude = ['id',]
        export_order = ['lrn',]



class GradeAdmin(ImportExportModelAdmin):
        resouce_classes = [GradeResource]
        import_id_fields = ['lrn',]
        exclude = ['id',]
        pass




admin.site.register(GradePost)
admin.site.register(GradePost2nd)
admin.site.register(GradePost3rd)
admin.site.register(GradePost4th)
admin.site.register(GradeTest, GradeAdmin)

