from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Blog

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=255)
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']