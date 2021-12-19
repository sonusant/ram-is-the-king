from os import truncate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    role = forms.CharField(max_length=30, required=True, help_text='minister or king.')

    class Meta:
        model = User
        fields = ('username',  'role',  'password1', 'password2', )