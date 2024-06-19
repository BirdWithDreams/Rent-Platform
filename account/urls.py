from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('<str:username>/', views.user, name='account'),
    path('comment/<str:username>/', views.add_review, name='add_review'),
]