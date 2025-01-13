from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2', ]

class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=100 )
    password = forms.CharField()