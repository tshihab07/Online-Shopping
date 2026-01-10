from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User                     # database model for user

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Last Name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Enter Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Your Password'
    }))