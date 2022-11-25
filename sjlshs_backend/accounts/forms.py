
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StudentUser

class CustomCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'birthday', 'username', 'email', 'password1', 'password2')
    
class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'email', 'birthday',)