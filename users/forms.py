from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # form interacts with the user model to create a new instanve or user
        fields = ['username', 'email', 'password1', 'password2']