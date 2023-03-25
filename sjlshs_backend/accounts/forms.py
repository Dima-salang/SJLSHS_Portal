
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import StudentUser, Db_Students
from django.forms import ModelForm
from django_otp.forms import OTPAuthenticationForm, OTPAuthenticationFormMixin



class CustomCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = StudentUser
        fields = ('lrn', 'last_name', 'first_name', 'grade_year', 'birthday', 'username', 'email', 'image_id', 'password1', 'password2')
        widgets = {
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'image_id': forms.ClearableFileInput(attrs={'multiple': True})
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


class CustomOTPAuthenticationForm(AuthenticationForm):
    lrn = forms.CharField(required=True, label='LRN', max_length=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lrn'] = forms.CharField(required=True, label="LRN")


    def clean(self):
        # Call the parent clean method to get cleaned data
        cleaned_data = super().clean()
        # Check if the lrn field is empty
        if not cleaned_data.get('lrn'):
            self.add_error('lrn', 'Please enter your LRN.')
        return cleaned_data
    