from django import forms
from django.contrib.auth.models import User
from user_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('protfolio', 'profile_pic')