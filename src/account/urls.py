# from django.contrib import admin
from django.urls import path
from .views import profile_view

app_name = 'account'
urlpatterns = [
    path('user/', profile_view, name='profile'),
]
