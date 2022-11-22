from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentUser

class CustomCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'birthday', 'username', 'email',)
    
class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'email', 'birthday',)