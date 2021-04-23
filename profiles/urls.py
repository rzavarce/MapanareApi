# -*- encoding: utf-8 -*-
from django.urls import path

from .views import UserProfile

urlpatterns = [
    path('profiles/', UserProfile, name='user_profile'),
]
