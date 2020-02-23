from django.contrib import admin
from django.urls import path, include
from .views import account_registration_view

urlpatterns = [
    path("register/", account_registration_view, name = "account_registration_view" )
]