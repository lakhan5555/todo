from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['text']

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username','email','password1','password2']
        