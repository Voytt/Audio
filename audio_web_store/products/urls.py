from django.contrib import admin
from django.urls import path, include
from .views import products_home_view

urlpatterns = [
    path("", products_home_view, name = "products_home_view" )
]