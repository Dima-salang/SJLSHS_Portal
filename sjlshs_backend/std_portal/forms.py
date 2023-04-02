from django import forms
from .models import Post, Modules
from django.core.exceptions import ValidationError
from accounts.models import Subject, StudentYear


    

class ModuleFilterForm(forms.Form):
    title_search = forms.CharField(required=False, label="Title")
    grade_level = forms.ModelChoiceField(StudentYear.objects.all(), label='Grade Level', required=False)
    subject = forms.ModelChoiceField(Subject.objects.all(), label='Subject', required=False)

