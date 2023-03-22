
# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.resources import ModelResource
from io import StringIO 
from django.core.files import File
import csv



# Register your models here.



from import_export.admin import ImportExportModelAdmin

class FirstSem1stQResource(resources.ModelResource):
        class Meta:
                model = FirstSem_1stQ_11
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'ORALCOMM', 'KOMUNIKASYON', 'GENMATH', 'ELS',
                             'PERDEV', 'LITERATURE', 'PR1', 'SPECIALIZED',
                               'SPECIALIZED_2', 'PE',
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = FirstSem_1stQ_11.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'
        
class FirstSem2ndQResource(resources.ModelResource):
        class Meta:
                model = FirstSem_2ndQ_11
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'ORALCOMM', 'KOMUNIKASYON', 'GENMATH', 'ELS',
                             'PERDEV', 'LITERATURE', 'PR1', 'SPECIALIZED',
                               'SPECIALIZED_2', 'PE',
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = FirstSem_2ndQ_11.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'
        
class SecondSem3rdQResource(resources.ModelResource):
        class Meta:
                model = SecondSem_3rdQ_11
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'READING_WRITING', 'PAGBASA', 'STATS_PROB', 'PHYSCI',
                             'EMPOWERMENT', 'SPECIALIZED',
                               'SPECIALIZED_2', 'PE2'
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = SecondSem_3rdQ_11.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'

class SecondSem4thQResource(resources.ModelResource):
        class Meta:
                model = SecondSem_4thQ_11
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'READING_WRITING', 'PAGBASA', 'STATS_PROB', 'PHYSCI',
                             'EMPOWERMENT', 'SPECIALIZED',
                               'SPECIALIZED_2', 'PE2'
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = SecondSem_4thQ_11.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'

class FirstQAdmin(ImportExportModelAdmin):
        resource_class = FirstSem1stQResource
        
        def get_queryset(self, request):
                qs = super().get_queryset(request)
                return qs.none()
        
class SecondQAdmin(ImportExportModelAdmin):
        resource_class = FirstSem2ndQResource
        
        def get_queryset(self, request):
                qs = super().get_queryset(request)
                return qs.none()
        
class ThirdQAdmin(ImportExportModelAdmin):
        resource_class = SecondSem3rdQResource
        
        def get_queryset(self, request):
                qs = super().get_queryset(request)
                return qs.none()
        
class FourthQAdmin(ImportExportModelAdmin):
        resource_class = SecondSem4thQResource
        
        def get_queryset(self, request):
                qs = super().get_queryset(request)
                return qs.none()

admin.site.register(FirstSem_1stQ_11, FirstQAdmin)
admin.site.register(FirstSem_2ndQ_11, SecondQAdmin)
admin.site.register(SecondSem_3rdQ_11, ThirdQAdmin)
admin.site.register(SecondSem_4thQ_11, FourthQAdmin)
