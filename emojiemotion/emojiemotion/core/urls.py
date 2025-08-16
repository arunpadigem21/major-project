from django.contrib import admin
from django.urls import path
from core import views  # <-- your app name here

urlpatterns = [
   
    path('', views.home, name='home'),  # this line is crucial for the root URL
]
