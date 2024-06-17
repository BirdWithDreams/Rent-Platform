from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser



class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',



        ]

        # Q9m#Zp5fEe!4BeB