from django import forms

from authentication.models import CustomUser


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
