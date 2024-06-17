from django import forms

from .models import Offers


class OfferCreateForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = [

            'title',
            'category',
            'description',
            'price',
            'tags',
            'image',

        ]


