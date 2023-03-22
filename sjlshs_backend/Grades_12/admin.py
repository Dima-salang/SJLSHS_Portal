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
                model = FirstSem_1stQ
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'PR2', 'CPAR', 'PHILOSOPHY', 'PE',
                             'UCSP', 'EAPP', 'SPECIALIZED',
                               'SPECIALIZED_2',
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = FirstSem_1stQ.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'
        
class FirstSem2ndQResource(resources.ModelResource):
        class Meta:
                model = FirstSem_2ndQ
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'PR2', 'CPAR', 'PHILOSOPHY', 'PE',
                             'UCSP', 'EAPP', 'SPECIALIZED',
                               'SPECIALIZED_2',
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = FirstSem_2ndQ.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'
        
class SecondSem3rdQResource(resources.ModelResource):
        class Meta:
                model = SecondSem_3rdQ
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'PR2', 'CPAR', 'PHILOSOPHY', 'PE4',
                             'UCSP', 'EAPP', 'SPECIALIZED',
                               'SPECIALIZED_2',
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = SecondSem_3rdQ.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'

class SecondSem4thQResource(resources.ModelResource):
        class Meta:
                model = SecondSem_4thQ
                exclude = ['id',]
                import_id_fields = ['last_name']
                skip_unchanged = True
                report_skipped = False
                clean_model_instance = True
                fields = ('last_name', 'first_name',
                           'PR2', 'CPAR', 'PHILOSOPHY', 'PE4',
                             'UCSP', 'EAPP', 'SPECIALIZED',
                               'SPECIALIZED_2',
                                 'AVERAGE', 'lrn')

        

        def before_export(self, queryset, *args, **kwargs):
                queryset = SecondSem_4thQ.objects.none()
                print(queryset)
                return queryset


        def get_display_name(self):
                return 'Custom Grade Resource'

class FirstQAdmin(ImportExportModelAdmin):
        resource_class = FirstSem1stQResource
        
        
        
class SecondQAdmin(ImportExportModelAdmin):
        resource_class = FirstSem2ndQResource
        
        
        
class ThirdQAdmin(ImportExportModelAdmin):
        resource_class = SecondSem3rdQResource
        
        
        
class FourthQAdmin(ImportExportModelAdmin):
        resource_class = SecondSem4thQResource
        
        

admin.site.register(FirstSem_1stQ, FirstQAdmin)
admin.site.register(FirstSem_2ndQ, SecondQAdmin)
admin.site.register(SecondSem_3rdQ, ThirdQAdmin)
admin.site.register(SecondSem_4thQ, FourthQAdmin)

