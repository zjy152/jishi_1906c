
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('index/',views.index),
    path('dev/',views.dev),
    path('dev2/',views.dev2)
]
