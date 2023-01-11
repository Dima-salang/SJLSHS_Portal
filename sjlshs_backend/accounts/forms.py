
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentUser, Db_Students
from django.forms import ModelForm

class CustomCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'grade_year', 'birthday', 'username', 'email', 'password1', 'password2')
        widgets = {
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            })
        }

        
    
class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'email', 'birthday', 'grade_year', 'strand')



class StudentInfoForm(ModelForm):
    class Meta:
        model = StudentUser
        fields = 'lrn', 'last_name', 'first_name', 'age', 'birthday', 'email', 'grade_year', 'section', 'strand'
