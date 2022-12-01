
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentUser

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
        fields = ('lrn', 'last_name', 'first_name', 'email', 'birthday', 'grade_year')