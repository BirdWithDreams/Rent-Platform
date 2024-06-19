from django import forms

from authentication.models import CustomUser
from .models import Feedbacks


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'card',
            'location',
            'city'

        ]

        # Q9m#Zp5fEe!4BeB


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = [
            'score',
            'comment',
        ]
