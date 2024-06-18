from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('account.urls')),
    path('offers/', include('offers.urls')),
    path('search/', include('search.urls')),

]