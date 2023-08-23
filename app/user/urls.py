"""URLs for user API"""
from django.urls import path

from user import views

app_name= 'user'

urlpatter=[
    path('create/', views.CreateUserView.as_view(), name='create'),
]
