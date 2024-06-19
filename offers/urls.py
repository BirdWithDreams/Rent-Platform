from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('user-offers/', views.my_offers, name='user_offers'),
    path('add/', views.add_offer, name='offer_constructor'),
    path('edit/<uuid:offer>/', views.edit_offer, name='offer_edit')
]
