from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('myoffers/', views.my_offers, name='my_offers'),
    path('add/', views.add_offer, name='offer_constructor'),
    path('edit/<uuid:offer>/', views.edit_offer, name='offer_edit')
]
