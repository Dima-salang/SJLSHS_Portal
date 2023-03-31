from django.contrib import admin
from .models import IrregularStudent, SubjectGrade
# Register your models here.
from django.forms import BaseInlineFormSet
from django.forms.models import inlineformset_factory

class SubjectGradeInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = self.queryset.select_related('subject')

class SubjectGradeInline(admin.TabularInline):
    model = SubjectGrade
    formset = SubjectGradeInlineFormSet
    extra = 0

class IrregularStudentAdmin(admin.ModelAdmin):
    inlines = [SubjectGradeInline]


    

admin.site.register(IrregularStudent, IrregularStudentAdmin)    
admin.site.register(SubjectGrade)
