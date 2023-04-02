
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import StudentUser, Db_Students
from django.forms import ModelForm



class CustomCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'grade_year', 'birthday', 'username', 'email', 'image_id', 'password1', 'password2', 'data_privacy_agreed')
        widgets = {
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'image_id': forms.ClearableFileInput(attrs={'multiple': True}),
            'data_privacy_agreed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                
                })
        }
        enctype = 'multipart/form-data'

    def save(self, commit=True):
            user = super().save(commit=False)
            user.is_active = False  # Set is_active to False
            if commit:
                user.save()
            return user

        
    
class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'email', 'birthday', 'grade_year', 'strand')



class StudentInfoForm(ModelForm):
    class Meta:
        model = StudentUser
        fields = 'lrn', 'last_name', 'first_name', 'age', 'birthday', 'email', 'grade_year', 'section', 'strand'


